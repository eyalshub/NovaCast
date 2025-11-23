# novacast/app/media/halp_video.py --- IGNORE ---
import os
import numpy as np
from typing import Tuple
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import ImageClip, ColorClip, CompositeVideoClip, AudioFileClip


def create_text_overlay_clip(
    text: str,
    size: Tuple[int, int] = (1280, 720),
    duration: float = 5.0,
    font_path: str = None,
    font_size: int = 48,
    text_color: Tuple[int, int, int] = (255, 255, 255),
    bg_color: Tuple[int, int, int, int] = (0, 0, 0, 160),
    margin: int = 40,
) -> ImageClip:
    """
    Create a text overlay clip using Pillow (no ImageMagick needed).
    Supports multiline wrapping and semi-transparent background.
    """
    img = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype(font_path or "arial.ttf", font_size)
    except Exception:
        font = ImageFont.load_default()

    # Word wrapping
    words = text.split()
    lines = []
    line = ""
    for word in words:
        test_line = f"{line} {word}".strip()
        if draw.textlength(test_line, font=font) < size[0] - 2 * margin:
            line = test_line
        else:
            lines.append(line)
            line = word
    lines.append(line)

    line_height = font.getbbox("Ay")[3] + 10
    text_height = line_height * len(lines)
    y = size[1] - text_height - margin

    # Background rectangle
    rect_top = y - 10
    rect_bottom = y + text_height + 10
    draw.rectangle([(0, rect_top), (size[0], rect_bottom)], fill=bg_color)

    for line in lines:
        line_width = draw.textlength(line, font=font)
        x = (size[0] - line_width) // 2
        draw.text((x, y), line, font=font, fill=text_color)
        y += line_height

    frame = np.array(img)
    return ImageClip(frame, ismask=False).set_duration(duration)


def create_background_clip(
    image_path: str = None,
    fallback_color: Tuple[int, int, int] = (20, 30, 70),
    size: Tuple[int, int] = (1280, 720),
    duration: float = 5.0,
) -> ImageClip:
    """
    Create a video background clip from an image or solid color fallback.
    """
    try:
        if image_path and os.path.exists(image_path):
            return ImageClip(image_path).resize(height=size[1]).set_duration(duration).set_position("center")
        else:
            raise FileNotFoundError("No valid image path provided.")
    except Exception as e:
        print(f"[⚠️] Fallback to solid background due to error: {e}")
        return ColorClip(size=size, color=fallback_color).set_duration(duration)


def compose_video_with_audio(
    visual_clips: list,
    audio_path: str,
    output_path: str,
    fps: int = 24,
    codec: str = "libx264",
    audio_codec: str = "aac",
) -> str | None:
    """
    Composes visual clips with audio into a final video file.
    Handles fallback strategies.
    """
    try:
        print("🎧 Loading audio...")
        audio = AudioFileClip(audio_path)
        duration = audio.duration

        # Set uniform duration
        for clip in visual_clips:
            clip.set_duration(duration)

        final_clip = CompositeVideoClip(visual_clips).set_duration(duration).set_audio(audio)

        print("[🎬] Writing final video...")
        final_clip.write_videofile(
            output_path,
            fps=fps,
            codec=codec,
            audio=True,
            audio_codec=audio_codec,
            threads=2,
            logger=None,
        )

        print(f"[✅] Video saved at: {output_path}")
        audio.close()
        final_clip.close()
        return output_path

    except Exception as e:
        print(f"[❌] Failed to compose video: {e}")
        return None
