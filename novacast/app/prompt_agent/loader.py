from typing import Any, Dict
import json
import os

class PromptLoader:
    def __init__(self, config_path: str):
        self.config_path = config_path
        self.prompts = self.load_prompts()

    def load_prompts(self) -> Dict[str, Any]:
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Configuration file not found: {self.config_path}")

        with open(self.config_path, 'r') as file:
            return json.load(file)

    def get_prompt(self, prompt_name: str) -> Any:
        return self.prompts.get(prompt_name, None)