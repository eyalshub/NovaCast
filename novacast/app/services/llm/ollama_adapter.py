# app/services/llm/ollama_adapter.py
from __future__ import annotations
import json
from typing import Any, Dict, List, Optional
import requests

from app.services.llm.base import BaseLLMService, LLMConnectionError, LLMResponseError
from app.config.settings import settings
from app.utils.retry import retry_on_exception as retry


class OllamaAdapter(BaseLLMService):
    """
    Adapter for local Ollama models via HTTP API (default: http://localhost:11434).
    Implements: generate_text(), chat(), list_models(), health()
    """

    def __init__(self, model_name: Optional[str] = None):
        self.model_name = model_name or settings.ollama_model
        self.host = settings.ollama_host.rstrip("/")
        self.timeout = settings.ollama_timeout
        self._params = {}

    def set_parameters(self, **kwargs):
        """Optional: set global generation parameters (e.g., temperature)."""
        self._params.update(kwargs)

    @retry(tries=3, exceptions=(requests.Timeout, requests.ConnectionError))
    def generate_text(self, prompt: str, **kwargs) -> str:
        """Single prompt → response via /api/generate."""
        url = f"{self.host}/api/generate"
        payload: Dict[str, Any] = {
            "model": self.model_name,
            "prompt": prompt,
            "stream": False,
        }

        # Combine default params + kwargs
        payload.update({k: v for k, v in {**self._params, **kwargs}.items() if v is not None})

        try:
            resp = requests.post(url, json=payload, timeout=self.timeout)
            resp.raise_for_status()
            data = resp.json()
        except requests.Timeout as e:
            raise LLMConnectionError(f"Ollama timeout ({self.timeout}s)") from e
        except requests.ConnectionError as e:
            raise LLMConnectionError("Cannot reach Ollama server") from e
        except requests.HTTPError as e:
            raise LLMResponseError(f"Ollama HTTP error: {e.response.status_code}") from e

        if not isinstance(data, dict) or "response" not in data:
            raise LLMResponseError("Invalid response format from Ollama")

        return data["response"].strip()

    @retry(tries=3, exceptions=(requests.Timeout, requests.ConnectionError))
    def chat(self, messages: List[Dict[str, str]], **kwargs) -> str:
        """Chat-style multi-turn interaction via /api/chat."""
        url = f"{self.host}/api/chat"
        payload: Dict[str, Any] = {
            "model": self.model_name,
            "messages": messages,
            "stream": False,
        }
        payload.update({k: v for k, v in {**self._params, **kwargs}.items() if v is not None})

        try:
            resp = requests.post(url, json=payload, timeout=self.timeout)
            resp.raise_for_status()
            data = resp.json()
        except requests.Timeout as e:
            raise LLMConnectionError("Ollama chat timeout") from e
        except requests.ConnectionError as e:
            raise LLMConnectionError("Cannot reach Ollama server") from e
        except requests.HTTPError as e:
            raise LLMResponseError(f"Ollama HTTP error: {e.response.status_code}") from e

        try:
            return data["message"]["content"].strip()
        except (KeyError, TypeError):
            raise LLMResponseError("Invalid chat response format")

    @retry(tries=3, exceptions=(requests.Timeout, requests.ConnectionError))
    def list_models(self) -> List[Dict[str, Any]]:
        """Returns the available models from /api/tags."""
        url = f"{self.host}/api/tags"
        try:
            resp = requests.get(url, timeout=self.timeout)
            resp.raise_for_status()
            data = resp.json()
        except requests.RequestException as e:
            raise LLMConnectionError("Failed to reach Ollama") from e

        models = data.get("models", [])
        if not isinstance(models, list):
            raise LLMResponseError("Malformed model list")

        return models

    def health(self) -> bool:
        """Returns True if models list is reachable."""
        try:
            _ = self.list_models()
            return True
        except LLMError:
            return False

    def get_model_info(self) -> dict:
        return {
            "provider": "ollama",
            "host": self.host,
            "model_name": self.model_name,
            "timeout": self.timeout,
            "params": self._params or {},
        }
