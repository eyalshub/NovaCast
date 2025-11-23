# script_agent.py
"""
ScriptAgent

This agent is responsible for generating, refining, analyzing, and managing video or narrative scripts.
It plays a central role in transforming structured ideas or outlines into full-length textual content.

Typical Flow:
- Receives an outline or idea prompt
- Calls LLM to generate a coherent script
- Refines and analyzes it for quality and tone
- Saves and loads scripts from files
"""

from typing import Optional

class ScriptAgent:
    def __init__(self, default_style: str = "neutral"):
        self.style = default_style

    def generate_script(self, prompt: str) -> str:
        """
        Generates a script based on the provided prompt or outline.
        TODO: Replace with LLM (LangChain/Ollama) call.

        Args:
            prompt: A textual idea or outline to turn into a script.

        Returns:
            A generated script string.
        """
        # Placeholder logic
        return f"Generated Script based on: {prompt}"

    def refine_script(self, script: str, feedback: Optional[str] = None) -> str:
        """
        Refines the script based on feedback (e.g. tone, target audience).

        Args:
            script: The original script.
            feedback: Optional feedback to guide rewriting.

        Returns:
            The improved script.
        """
        # TODO: Use LLM with feedback prompt
        return script + (f"\n\n[Refined: {feedback}]" if feedback else "\n\n[Refined]")

    def analyze_script(self, script: str) -> dict:
        """
        Performs basic analysis: word count, estimated duration, and section count.

        Returns:
            A dictionary with script statistics.
        """
        word_count = len(script.split())
        estimated_duration_min = round(word_count / 150, 2)  # ~150 words/minute
        sections = script.count("\n\n")

        return {
            "word_count": word_count,
            "estimated_duration_min": estimated_duration_min,
            "section_count": sections
        }

    def save_script(self, script: str, filename: str = "script.txt") -> None:
        """
        Saves the script content to a file.

        Args:
            script: The script text.
            filename: Target file name.
        """
        with open(filename, "w", encoding="utf-8") as f:
            f.write(script)

    def load_script(self, filename: str = "script.txt") -> str:
        """
        Loads a script from a local file.

        Args:
            filename: The name of the file to read from.

        Returns:
            The loaded script text.
        """
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()

    def set_style(self, style: str) -> None:
        """
        Sets the writing style for future generations (e.g. casual, formal).
        """
        self.style = style

    def get_style(self) -> str:
        return self.style
