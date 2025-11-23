# Outline Agent Implementation
"""
OutlineAgent (NovaCast)

This agent generates a structured outline for a given topic, typically for use in content creation,
scripts, or educational material. It is part of the NOVACAST pipeline and comes after idea generation.

Responsibilities:
- Generate high-quality outlines using LLMs (LangChain + Ollama)
- Validate and fallback to deterministic structure when needed
- Maintain backwards compatibility with legacy outline methods
"""
from __future__ import annotations

import json
from typing import Any, Dict, List

from pydantic import ValidationError
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from langchain_ollama import OllamaLLM

from app.utils.prompt_loader import load_prompt
from app.config.settings import settings
from app.agents.types import (
    OutlineAgentInput,
    OutlineAgentResult,
    OutlineSection,
)
import logging
logger = logging.getLogger(__name__)

# ---- Helpers -----------------------------------------------------------------

def _safe_json_loads(s: str) -> Dict[str, Any]:
    s = s.strip()
    if s.startswith("```"):
        s = s.strip("`")
        start = s.find("{")
        if start != -1:
            s = s[start:]
    if s.endswith("```"):
        s = s[:-3]
    return json.loads(s)


# ---- Agent -------------------------------------------------------------------

class OutlineAgent:
    def __init__(self, prompt_path: str = "prompts/outline_agent.yaml") -> None:
        self.prompt_cfg = load_prompt(prompt_path)

        self.template = PromptTemplate(
            input_variables=[
                "topic",
                "idea",
                "tone",
                "audience",
                "goal",
                "platform",
                "style",
                "max_sections",
                "language",
            ],
            template=self.prompt_cfg["user_template"],
        )

        self.llm = OllamaLLM(
            model=settings.ollama_model,
            system=self.prompt_cfg.get("system", ""),
        )

        self.chain: RunnableSequence = self.template | self.llm | StrOutputParser()
        self._outline_cache: List[str] = []

    def run(self, data: OutlineAgentInput) -> OutlineAgentResult:
        try:
            logger.debug(f"📤 Sending outline input to LLM: {data.model_dump()}")
            raw = self.chain.invoke(data.model_dump())
            logger.debug(f"📥 Raw LLM response: {raw}")

            payload = _safe_json_loads(raw)
            result = OutlineAgentResult(**payload)

            logger.info("✅ Successfully parsed OutlineAgentResult from LLM")
            return result

        except (json.JSONDecodeError, ValidationError) as e:
            logger.warning(f"⚠️ Failed to parse LLM output. Using fallback. Reason: {e}")
            return self.basic_outline(topic=data.topic, language=data.language)

        except Exception as e:
            logger.exception("❌ Unexpected error in OutlineAgent.run()")
            raise e

    def basic_outline(self, topic: str, language: str = "en") -> OutlineAgentResult:
        title = {"en": f"Outline: {topic}", "he": f"סקיצה: {topic}"}.get(language, f"Outline: {topic}")

        sections = [
            OutlineSection(
                heading={"en": "Introduction", "he": "פתיחה"}.get(language, "Introduction"),
                bullets=[
                    {"en": "Why this matters", "he": "למה זה חשוב"}.get(language, "Why this matters"),
                    {"en": "What we will cover", "he": "מה נכסה"}.get(language, "What we will cover"),
                ],
            ),
            OutlineSection(
                heading={"en": "Main Points", "he": "עיקר"}.get(language, "Main Points"),
                bullets=[
                    {"en": "Key concept 1", "he": "עיקרון 1"}.get(language, "Key concept 1"),
                    {"en": "Key concept 2", "he": "עיקרון 2"}.get(language, "Key concept 2"),
                    {"en": "Key concept 3", "he": "עיקרון 3"}.get(language, "Key concept 3"),
                ],
            ),
            OutlineSection(
                heading={"en": "Conclusion", "he": "סיכום"}.get(language, "Conclusion"),
                bullets=[
                    {"en": "Wrap-up & next steps", "he": "סגירה והצעדים הבאים"}.get(language, "Wrap-up & next steps")
                ],
            ),
        ]

        cta = {"en": "Subscribe for more and share your thoughts.", "he": "עקבו לעוד ושתפו מחשבות."}.get(language)

        return OutlineAgentResult(
            title=title,
            language=language,
            audience="general",
            platform="youtube_short",
            sections=sections,
            cta=cta,
        )

    def create_outline(self, topic: str) -> List[str]:
        self._outline_cache = [
            f"Introduction to {topic}",
            f"Main points about {topic}",
            f"Conclusion on {topic}"
        ]
        return list(self._outline_cache)

    def generate_outline_with_llm(self, topic: str, style: str = "educational") -> List[str]:
        return self.create_outline(topic)

    def add_section(self, section_title: str) -> None:
        self._outline_cache.append(section_title)

    def insert_section(self, index: int, section_title: str) -> None:
        if 0 <= index <= len(self._outline_cache):
            self._outline_cache.insert(index, section_title)

    def remove_section(self, index: int) -> None:
        if 0 <= index < len(self._outline_cache):
            self._outline_cache.pop(index)

    def get_outline(self) -> List[str]:
        return list(self._outline_cache)

    def clear_outline(self) -> None:
        self._outline_cache.clear()

    def to_json(self, result: OutlineAgentResult | None = None) -> Dict[str, Any]:
        if result is not None:
            return result.model_dump()
        return {"outline": list(self._outline_cache)}
