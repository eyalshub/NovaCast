import os
import pytest
from app.media.tts_engine import TTSEngine

@pytest.fixture
def tts():
    return TTSEngine()

def test_coqui_tts_creates_file(tts):
    text = "Hello from Coqui!"
    output_path = tts.synthesize("coqui", text)
    assert output_path.endswith(".wav")
    assert os.path.exists(output_path)
    assert os.path.getsize(output_path) > 0

def test_elevenlabs_tts_output(tts):
    text = "Hello from ElevenLabs!"
    output = tts.synthesize("elevenlabs", text)
    assert isinstance(output, str)
    assert "ElevenLabs TTS synthesized" in output

def test_piper_tts_output(tts):
    text = "Hello from Piper!"
    output = tts.synthesize("piper", text)
    assert isinstance(output, str)
    assert "Piper TTS synthesized" in output

def test_invalid_engine(tts):
    with pytest.raises(ValueError) as exc:
        tts.synthesize("unknown", "Hello?")
    assert "Unsupported TTS engine" in str(exc.value)
