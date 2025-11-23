from typing import Dict, Any

class PromptRegistry:
    def __init__(self):
        self.prompts: Dict[str, Any] = {}

    def register_prompt(self, name: str, prompt: Any) -> None:
        if name in self.prompts:
            raise ValueError(f"Prompt '{name}' is already registered.")
        self.prompts[name] = prompt

    def get_prompt(self, name: str) -> Any:
        if name not in self.prompts:
            raise KeyError(f"Prompt '{name}' not found.")
        return self.prompts[name]

    def list_prompts(self) -> Dict[str, Any]:
        return self.prompts.copy()