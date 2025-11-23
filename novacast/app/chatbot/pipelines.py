# This file defines the pipelines for processing chatbot interactions.

from typing import Any, Dict, List

class ChatbotPipeline:
    def __init__(self):
        self.steps = []

    def add_step(self, step: 'PipelineStep'):
        self.steps.append(step)

    def run(self, input_data: Any) -> Any:
        data = input_data
        for step in self.steps:
            data = step.execute(data)
        return data

class PipelineStep:
    def execute(self, input_data: Any) -> Any:
        raise NotImplementedError("Each step must implement the execute method.")

class ExampleStep(PipelineStep):
    def execute(self, input_data: Any) -> Any:
        # Example processing logic
        return input_data  # Modify this to implement actual logic

# Example usage
if __name__ == "__main__":
    pipeline = ChatbotPipeline()
    pipeline.add_step(ExampleStep())
    result = pipeline.run("Initial input data")
    print(result)  # Output the result of the pipeline processing