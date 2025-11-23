# tests/media/test_video_builder.py

import os
import pytest
from app.media.video_builder import  build_media_clip_with_context

SAMPLE_AUDIO = "output/audio_coqui.wav"


@pytest.mark.parametrize("func", [ build_media_clip_with_context])
def test_video_generation(func):
    print(f"\n🧪 Testing function: {func.__name__}")

    # Ensure sample audio exists
    assert os.path.exists(SAMPLE_AUDIO), f"❌ Sample audio file not found: {SAMPLE_AUDIO}"

    if func.__name__ == "build_media_clip":
        output_path = func(SAMPLE_AUDIO)
    else:
        output_path = func(SAMPLE_AUDIO, "This is test context for the video")

    assert output_path is not None, "❌ Function returned None"
    assert os.path.exists(output_path), f"❌ Expected video at: {output_path}"
    assert output_path.endswith(".mp4"), "❌ Output is not an mp4 file"
    assert os.path.getsize(output_path) > 10_000, f"❌ Video file too small: {output_path}"

    print(f"✅ Success: {output_path}")


def test_video_from_script_context():
    print("\n🎬 Starting test: video generation from full script context")

    full_script = (
        "Welcome to NovaCast!\n"
        "Today, we'll talk about the French Revolution and its impact on modern Europe.\n"
        "We'll start with the historical background, move on to the economic and social causes, "
        "and finally explore the educational implications of that turbulent period.\n"
        "Let's get started."
    )

    print("📜 Using the following script as video context:")
    print(full_script)

    assert os.path.exists(SAMPLE_AUDIO), f"❌ Sample audio file not found: {SAMPLE_AUDIO}"
    print("🎧 Using sample audio:", SAMPLE_AUDIO)

    output_path = build_media_clip_with_context(SAMPLE_AUDIO, full_script)

    print("📁 Verifying output file...")
    assert output_path is not None, "❌ Function returned None"
    assert os.path.exists(output_path), f"❌ Expected video at: {output_path}"
    assert output_path.endswith(".mp4"), "❌ Output is not an mp4 file"
    assert os.path.getsize(output_path) > 10_000, f"❌ Video file too small: {output_path}"

    print("✅ Test passed! Video successfully generated.")
    print(f"📽️ Final video saved at: {output_path}")
