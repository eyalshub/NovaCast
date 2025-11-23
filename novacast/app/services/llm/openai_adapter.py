from typing import Any, Dict
import openai

class OpenAIAdapter:
    def __init__(self, api_key: str):
        openai.api_key = api_key

    def generate_text(self, prompt: str, **kwargs: Any) -> str:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            **kwargs
        )
        return response['choices'][0]['message']['content']

    def generate_image(self, prompt: str, **kwargs: Any) -> str:
        response = openai.Image.create(
            prompt=prompt,
            **kwargs
        )
        return response['data'][0]['url']

    def fine_tune_model(self, training_data: Dict[str, Any]) -> str:
        response = openai.FineTune.create(training_file=training_data)
        return response['id']

    def list_models(self) -> Dict[str, Any]:
        return openai.Model.list()