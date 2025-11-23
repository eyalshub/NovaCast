# tests/core/test_orchestrator_pipeline.py

import pytest
from app.core.orchestrator import Orchestrator
from app.agents.types import IdeationAgentInput

# We'll skip mocking for now and run with real agents.
# Make sure LLM and TTS/Video systems are set up before running!

def test_orchestrator_pipeline_full():
    orchestrator = Orchestrator()

    user_input = IdeationAgentInput(
        topic="How AI is transforming education",
        tone="inspiring",
        audience="students",
        goal="motivate",
        platform="youtube_short",
        style="storytelling",
        max_words=120,
        language="en"
    )

    result = orchestrator.run_pipeline(user_input)

    assert result["idea"], "Idea should not be empty"
    assert isinstance(result["outline"], list) and len(result["outline"]) > 0, "Outline should be a non-empty list"
    assert isinstance(result["script"], str) and len(result["script"]) > 0, "Script should be a non-empty string"
    assert result["audio_path"].endswith(".wav"), "Audio path should be a .wav file"
    assert result["video_path"].endswith(".mp4"), "Video path should be a .mp4 file"

    # Optional debug print
    print("\n🧪 Orchestrator pipeline output:")
    print(f"Idea: {result['idea']}")
    print(f"Outline: {result['outline'][:2]}...")
    print(f"Script: {result['script'][:100]}...")
    print(f"Audio file: {result['audio_path']}")
    print(f"Video file: {result['video_path']}")
