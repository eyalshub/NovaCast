# tests/agents/test_outline_agent.py
import pytest
from app.agents.outline_agent import OutlineAgent
from app.agents.types import OutlineAgentInput, OutlineAgentResult

from langchain_core.runnables import Runnable
from langchain_core.output_parsers import StrOutputParser

class FakeLLM(Runnable):
    def invoke(self, input: str, config=None, **kwargs) -> str:
        print("🧪 FakeLLM invoked – returning intentionally invalid output")
        return "<<<INVALID OUTPUT>>>"


def test_outline_agent_fallback():
    """Test fallback behavior when the LLM returns invalid JSON."""
    agent = OutlineAgent()

    # Inject fake LLM and re-create the chain
    agent.llm = FakeLLM()
    agent.chain = agent.template | agent.llm | StrOutputParser()

    input_data = OutlineAgentInput(
        topic="AI in classrooms",
        idea="AI can automate routine tasks for teachers",
        tone="neutral",
        audience="teachers",
        goal="inform",
        platform="youtube_short",
        style="educational",
        max_sections=4,
        language="en",
    )

    print("\n⚙️ Starting fallback test with FakeLLM...")
    result = agent.run(input_data)
    print("📥 Fallback result:\n", result.model_dump())

    assert isinstance(result, OutlineAgentResult)
    assert result.title.startswith("Outline")
    assert len(result.sections) >= 2
    assert all(len(s.bullets) >= 1 for s in result.sections)


def test_outline_agent_basic_list():
    """Test legacy outline list methods still function."""
    agent = OutlineAgent()
    print("\n⚙️ Starting test: legacy outline list")

    outline = agent.create_outline("Data Science")
    print(f"📄 Initial outline:\n{outline}")

    agent.add_section("Applications of Data Science")
    updated = agent.get_outline()
    print(f"➕ After adding section:\n{updated}")
    assert updated[-1] == "Applications of Data Science"

    agent.insert_section(1, "History of Data Science")
    updated = agent.get_outline()
    print(f"📌 After inserting section at index 1:\n{updated}")
    assert updated[1] == "History of Data Science"

    agent.remove_section(1)
    updated = agent.get_outline()
    print(f"❌ After removing section at index 1:\n{updated}")
    assert not any("History" in s for s in updated)

    agent.clear_outline()
    print(f"🧹 After clearing outline:\n{agent.get_outline()}")
    assert agent.get_outline() == []

    print("✅ Legacy outline test passed.\n")
