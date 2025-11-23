import pytest
from app.prompt_agent.registry import PromptRegistry

@pytest.fixture
def prompt_registry():
    return PromptRegistry()

def test_register_prompt(prompt_registry):
    prompt = {"id": "test_prompt", "content": "This is a test prompt."}
    prompt_registry.register(prompt)
    assert prompt_registry.get("test_prompt") == prompt

def test_unregister_prompt(prompt_registry):
    prompt = {"id": "test_prompt", "content": "This is a test prompt."}
    prompt_registry.register(prompt)
    prompt_registry.unregister("test_prompt")
    assert prompt_registry.get("test_prompt") is None

def test_get_non_existent_prompt(prompt_registry):
    assert prompt_registry.get("non_existent_prompt") is None

def test_register_duplicate_prompt(prompt_registry):
    prompt = {"id": "test_prompt", "content": "This is a test prompt."}
    prompt_registry.register(prompt)
    with pytest.raises(ValueError):
        prompt_registry.register(prompt)