# app/media/tts_engine.py
"""
TTS Engine Adapter System

This module provides an extensible abstraction layer for Text-to-Speech (TTS) synthesis.
It supports multiple TTS backends (Coqui, ElevenLabs, Piper) through a unified interface.

Core Components:
- TTSAdapter: Abstract base class for all TTS providers
- CoquiTTSAdapter / ElevenLabsTTSAdapter / PiperTTSAdapter: Concrete implementations
- TTSEngine: High-level interface for selecting and using a specific TTS engine

Usage:
    tts_engine = TTSEngine()
    audio_path = tts_engine.synthesize("coqui", "Hello world!")
    # → returns path to synthesized audio file

This layer enables easy integration of real-time or offline TTS generation,
and supports seamless switching between engines for testing, fallback, or A/B experimentation.
"""


from typing import List, Dict, Any
import os
from TTS.api import TTS
class TTSAdapter:
    def __init__(self, engine: str):
        self.engine = engine

    def synthesize(self, text: str) -> str:
        raise NotImplementedError("This method should be overridden by subclasses.")

class CoquiTTSAdapter(TTSAdapter):
    def synthesize(self, text: str) -> str:
        output_path = "output/audio_coqui.wav"
        os.makedirs("output", exist_ok=True)

        # Load Coqui model (once per adapter)
        tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)

        # Synthesize and save
        tts.tts_to_file(text=text, file_path=output_path)

        return output_path

class ElevenLabsTTSAdapter(TTSAdapter):
    def synthesize(self, text: str) -> str:
        # Implementation for ElevenLabs TTS
        return f"ElevenLabs TTS synthesized audio for: {text}"

class PiperTTSAdapter(TTSAdapter):
    def synthesize(self, text: str) -> str:
        # Implementation for Piper TTS
        return f"Piper TTS synthesized audio for: {text}"

class TTSEngine:
    def __init__(self):
        self.adapters: Dict[str, TTSAdapter] = {
            "coqui": CoquiTTSAdapter("coqui"),
            "elevenlabs": ElevenLabsTTSAdapter("elevenlabs"),
            "piper": PiperTTSAdapter("piper"),
        }

    def synthesize(self, engine: str, text: str) -> str:
        if engine not in self.adapters:
            raise ValueError(f"Unsupported TTS engine: {engine}")
        return self.adapters[engine].synthesize(text)

# Example usage
if __name__ == "__main__":
    tts_engine = TTSEngine()
    print(tts_engine.synthesize("coqui", "Hello, world!"))
    print(tts_engine.synthesize("elevenlabs", "Hello, world!"))
    print(tts_engine.synthesize("piper", "Hello, world!"))