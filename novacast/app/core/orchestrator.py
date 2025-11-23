# novacast/app/core/orchestrator.py

"""
Orchestrator

This class manages the execution flow between different content generation agents.
It supports a pipeline mode (idea → outline → script), and can be extended to support
chat-driven intent-based dispatching later.
"""

from typing import Any, Dict, List

from app.agents.ideation_agent import IdeationAgent
from app.agents.outline_agent import OutlineAgent
from app.agents.script_agent import ScriptAgent
from app.agents.types import OutlineAgentInput


def _preview(val: Any, limit: int = 80) -> str:
    try:
        if isinstance(val, bytes):
            s = val.decode(errors="replace")
        elif isinstance(val, list):
            s = " | ".join(str(x) for x in val[:5])
            if len(val) > 5:
                s += " …"
            return s[:limit] + ("…" if len(s) > limit else "")
        else:
            s = val if isinstance(val, str) else repr(val)
        return s[:limit] + ("…" if len(s) > limit else "")
    except Exception as e:
        return f"<unpreviewable: {e!r}>"


class Orchestrator:
    def __init__(self):
        self.tasks: List[Dict[str, Any]] = []
        self.ideation_agent = IdeationAgent()
        self.outline_agent = OutlineAgent()
        self.script_agent = ScriptAgent()

    def plan(self, task: Dict[str, Any]) -> None:
        self.tasks.append(task)

    def clear_tasks(self) -> None:
        self.tasks.clear()

    def run_pipeline(self, user_input: Any) -> Dict[str, Any]:
        """
        Executes the idea → outline → script → tts → video pipeline based on user input.
        The user_input can be a Pydantic model or a dict.
        """
        # Convert Pydantic input to dict if needed
        if hasattr(user_input, "model_dump"):
            user_input_dict = user_input.model_dump()
        elif isinstance(user_input, dict):
            user_input_dict = user_input
        else:
            raise ValueError("Invalid input type for user_input")

        # Stage 1: Ideation
        idea_result = self.ideation_agent.run(user_input)
        idea = idea_result["idea"]
        self.plan({"name": "generate_idea", "output": idea})

        # Stage 2: Outline
        outline_input = OutlineAgentInput(**{**user_input_dict, "idea": idea})
        outline_result = self.outline_agent.run(outline_input)
        outline = outline_result.sections
        self.plan({"name": "generate_outline", "output": outline})

        # Stage 3: Script
        script = self.script_agent.generate_script("\n".join(
    f"{s.title}\n{s.content}" for s in outline
))
        self.plan({"name": "generate_script", "output": script})

        # Stage 4: Audio
        from app.media.tts_engine import TTSEngine
        tts_engine = TTSEngine()
        try:
            audio_path = tts_engine.synthesize("coqui", script)
            self.plan({"name": "tts_synthesis", "output": audio_path})
        except Exception as e:
            self.plan({"name": "tts_synthesis", "error": f"{e.__class__.__name__}: {e}"})
            raise

        # Stage 5: Video
        from app.media.video_builder import build_media_clip_with_context
        try:
            video_path = build_media_clip_with_context(audio_path, script)
            self.plan({"name": "video_generation", "output": video_path})
        except Exception as e:
            self.plan({"name": "video_generation", "error": f"{e.__class__.__name__}: {e}"})
            raise

        return {
            "input": user_input_dict,
            "idea": idea,
            "outline": outline,
            "script": script,
            "audio_path": audio_path,
            "video_path": video_path
        }

    def print_tasks(self) -> None:
        for task in self.tasks:
            name = task.get("name", "?")
            if "error" in task:
                print(f"[{name}] ✖ {task['error']}")
            else:
                print(f"[{name}] → {_preview(task.get('output'))}")
