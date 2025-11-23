# app/services/llm/base.py
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Dict, Iterable, List


__all__ = [
    "LLMError",
    "LLMConnectionError",
    "LLMResponseError",
    "BaseLLMService",
]


class LLMError(Exception):
    """Base error for LLM adapters."""


class LLMConnectionError(LLMError):
    """Connectivity issues (host down, DNS, timeout, etc.)."""


class LLMResponseError(LLMError):
    """Unexpected HTTP status or malformed provider response."""


class BaseLLMService(ABC):
    """
    Abstract interface every LLM adapter must implement.

    Mandatory:
      - generate_text(prompt, **kwargs) -> str
      - get_model_info() -> dict

    Optional (raise NotImplementedError by default):
      - generate_stream(prompt, **kwargs) -> Iterable[str]
      - chat(messages, **kwargs) -> str
      - list_models() -> List[dict]
      - health() -> bool
      - format_chat(system, user) -> str
    """

    # -------- Required API --------
    @abstractmethod
    def generate_text(self, prompt: str, **kwargs) -> str:
        """Single-turn text generation (completion style)."""

    @abstractmethod
    def get_model_info(self) -> Dict[str, Any]:
        """Return model/provider info (name, host, etc.)."""

    # -------- Optional / Convenience API --------
    def generate(self, prompt: str, **kwargs) -> str:
        """
        Alias for generate_text to keep naming consistent across adapters.
        Useful if some callers expect `generate(...)`.
        """
        return self.generate_text(prompt, **kwargs)

    def generate_stream(self, prompt: str, **kwargs) -> Iterable[str]:
        """
        Streaming variant. Yield text chunks as they arrive.
        Default: not implemented.
        """
        raise NotImplementedError("Streaming is not implemented for this provider.")

    def chat(self, messages: List[Dict[str, str]], **kwargs) -> str:
        """
        Multi-turn chat API.
        messages: [{'role': 'system'|'user'|'assistant', 'content': '...'}]
        Default: not implemented.
        """
        raise NotImplementedError("Chat API is not implemented for this provider.")

    def list_models(self) -> List[Dict[str, Any]]:
        """Return a list of available models on the runtime. Default: empty list."""
        return []

    def health(self) -> bool:
        """
        Provider health-check. Override to perform a real ping.
        Default: True (assumed healthy).
        """
        return True

    # -------- Helpers --------
    def format_chat(self, system: str, user: str) -> str:
        """
        Helper for providers that accept a single 'prompt' string but we still
        want to pass system+user context. Override if your provider uses
        a different instruction format.
        """
        system = (system or "").strip()
        user = (user or "").strip()
        if not system:
            return user
        return f"[SYSTEM]\n{system}\n\n[USER]\n{user}"
