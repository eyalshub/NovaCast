from pydantic import BaseModel
from typing import List, Dict, Any

class ModelConfig(BaseModel):
    name: str
    version: str
    description: str
    parameters: Dict[str, Any]

class ModelsMap:
    def __init__(self, models: List[ModelConfig]):
        self.models = {model.name: model for model in models}

    def get_model(self, name: str) -> ModelConfig:
        return self.models.get(name)

    def list_models(self) -> List[str]:
        return list(self.models.keys())

    def add_model(self, model: ModelConfig):
        self.models[model.name] = model

    def remove_model(self, name: str):
        if name in self.models:
            del self.models[name]