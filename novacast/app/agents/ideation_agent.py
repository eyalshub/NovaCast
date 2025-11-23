# app/agents/ideation_agent.py

"""
IdeationAgent

This agent is responsible for generating creative content ideas based on a given topic or prompt.
It serves as the first step in the NOVACAST pipeline, helping spark structured or open-ended directions
for scripts, videos, or outlines using AI or rule-based logic.
"""

import logging
from typing import Optional
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_ollama import OllamaLLM

from app.agents.types import IdeationAgentInput
from app.config.settings import settings
from app.utils.prompt_loader import load_prompt
from app.agents.types import IdeationAgentInput, IdeationAgentOutput

logger = logging.getLogger(__name__)


class IdeationAgent:
    def __init__(self, prompt_path: str = "prompts/ideation_agent.yaml"):
        try:
            self.prompt_config = load_prompt(prompt_path)
            self.template = PromptTemplate(
                input_variables=[
                    "topic", "tone", "audience", "goal", "platform",
                    "style", "max_words", "language"
                ],
                template=self.prompt_config["user_template"]
            )
            llm = OllamaLLM(model=settings.ollama_model)
            self.chain: RunnableSequence = self.template | llm
            logger.info("✅ IdeationAgent initialized successfully.")
        except Exception as e:
            logger.exception("❌ Failed to initialize IdeationAgent")
            raise e

    def run(self, input_data: IdeationAgentInput) -> IdeationAgentOutput:
        """Generate a creative idea based on the input parameters."""
        try:
            logger.debug(f"📤 Sending input to IdeationAgent: {input_data.model_dump()}")
            response = self.chain.invoke(input_data.model_dump())
            idea = response.strip().strip('"').strip("'")
            logger.debug(f"📥 Received idea: {idea}")
            return {"idea": idea}
        except Exception as e:
            logger.exception("❌ Error during IdeationAgent.run()")
            raise 
