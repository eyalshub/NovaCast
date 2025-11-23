# tests/agents/test_ideation_agent.py

import pytest
from app.agents.ideation_agent import IdeationAgent
from app.agents.types import IdeationAgentInput

@pytest.fixture
def ideation_input() -> IdeationAgentInput:
    return IdeationAgentInput(
        topic="How AI is transforming education",
        tone="inspiring",
        audience="teachers and school leaders",
        goal="highlight positive impact",
        platform="YouTube",
        style="short and powerful",
        max_words=50,
        language="English"
    )

def test_ideation_agent_runs(ideation_input):
    print("\n🔍 [TEST] Creating IdeationAgent...")
    agent = IdeationAgent()

    print("📤 [TEST] Sending input to agent:")
    print(ideation_input.model_dump())

    output = agent.run(ideation_input)

    print("📥 [TEST] Received output from agent:")
    print(output)

    assert isinstance(output, dict), "Output should be a dictionary"
    assert "idea" in output, "Output should contain an 'idea' key"
    assert isinstance(output["idea"], str), "'idea' should be a string"
    assert len(output["idea"]) > 10, "Idea should be a non-trivial response"
