# app/utils/prompt_loader.py

import os
import yaml
from typing import Dict


def load_prompt(path: str) -> Dict:
    """
    Loads a YAML prompt file and returns its content as a dictionary.
    Supports relative paths under the 'prompts/' directory.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Prompt file not found: {path}")

    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)
