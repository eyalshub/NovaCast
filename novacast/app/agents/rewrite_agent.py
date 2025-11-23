# Rewrite Agent Implementation
"""
RewriteAgent

This agent is responsible for rephrasing or rewriting input text into a different style, tone, or format.
It is used to enhance or adjust generated content for specific audiences, platforms, or purposes.

Use cases:
- Adjusting tone (formal, casual, humorous, inspirational, etc.)
- Platform-specific rewrites (YouTube, TikTok, blog, academic)
- Language simplification or enhancement
"""

from typing import Optional

class RewriteAgent:
    def __init__(self, style: Optional[str] = "default"):
        self.style = style

    def rewrite(self, text: str, style: Optional[str] = None) -> str:
        """
        Rewrites the given text using the provided style or the agent's default style.
        TODO: Replace with call to LLM (LangChain or Ollama)

        :param text: The original text to be rewritten.
        :param style: (Optional) The style in which to rewrite the text.
        :return: The rewritten text.
        """
        final_style = style if style else self.style
        # Placeholder logic
        rewritten_text = f"[{final_style.upper()} STYLE] {text}"
        return rewritten_text

    def set_style(self, style: str) -> None:
        """
        Sets the default style for rewriting.

        :param style: The style to be set.
        """
        self.style = style

    def get_style(self) -> str:
        """
        Returns the current default rewriting style.
        """
        return self.style

    def rewrite_batch(self, texts: list[str], style: Optional[str] = None) -> list[str]:
        """
        Rewrites a batch of texts using a given or default style.

        :param texts: A list of strings to rewrite.
        :param style: (Optional) Style to apply.
        :return: List of rewritten texts.
        """
        return [self.rewrite(text, style) for text in texts]

    def to_json(self, original: str, rewritten: str) -> dict:
        """
        Returns a JSON structure containing the original and rewritten text.
        """
        return {
            "style": self.style,
            "original": original,
            "rewritten": rewritten
        }
