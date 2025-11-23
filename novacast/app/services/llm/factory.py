# app/services/llm/factory.py
from typing import Optional
from app.services.llm.base import BaseLLMService
from app.config.settings import settings

from app.services.llm.ollama_adapter import OllamaAdapter

# Optional: for future use
# from app.services.llm.openai_adapter import OpenAIAdapter
# from app.services.llm.anthropic_adapter import AnthropicAdapter


def create_language_model(
    model_type: Optional[str] = None,
    model_name: Optional[str] = None,
) -> BaseLLMService:
    """
    Returns an initialized language model adapter.

    Args:
        model_type: "ollama", "openai", "anthropic" (default: settings.LLM_PROVIDER)
        model_name: optional override of model name (e.g., "llama3.2:latest")

    Returns:
        An instance of BaseLLMService-compatible adapter
    """
    model_type = (model_type or settings.LLM_PROVIDER).lower()

    if model_type == "ollama":
        return OllamaAdapter(model_name=model_name)

    elif model_type == "openai":
        # return OpenAIAdapter(model_name=model_name)
        raise NotImplementedError("OpenAIAdapter not implemented yet")

    elif model_type == "anthropic":
        # return AnthropicAdapter(model_name=model_name)
        raise NotImplementedError("AnthropicAdapter not implemented yet")

    else:
        raise ValueError(f"Unknown model type: {model_type}")


# factory.py
def get_llm() -> BaseLLMService:
    return create_language_model(settings.llm_provider, settings.ollama_model)
