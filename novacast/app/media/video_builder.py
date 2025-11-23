import os
import uuid
import requests
import subprocess
from typing import List
from dotenv import load_dotenv
from app.media.halp_video import (
    create_background_clip,
    create_text_overlay_clip,
    compose_video_with_audio,
)
from moviepy.editor import ImageClip, ColorClip, TextClip, AudioFileClip, CompositeVideoClip, VideoFileClip
from moviepy.video.fx.resize import resize  

load_dotenv()
PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")
PEXELS_API_URL = "https://api.pexels.com/v1/search"
HEADERS = {"Authorization": PEXELS_API_KEY}


class VideoBuilder:
    def __init__(self, template: str = None):
        self.template = template
        os.makedirs("output", exist_ok=True)
        self.video_index = self._get_latest_index()

    def _get_latest_index(self) -> int:
        existing = [f for f in os.listdir("output") if f.startswith("final_video_") and f.endswith(".mp4")]
        indexes = [int(f.split("_")[-1].replace(".mp4", "")) for f in existing if f.split("_")[-1].replace(".mp4", "").isdigit()]
        return max(indexes, default=0)

    def _get_next_output_path(self) -> str:
        self.video_index += 1
        return f"output/final_video_{self.video_index}.mp4"

    def build_video(self, audio_file: str) -> str:
        print("[🎬] Building video from template...")
        output_path = self._get_next_output_path()
        command = [
            'ffmpeg', '-i', audio_file, '-i', self.template,
            '-c:v', 'copy', '-c:a', 'aac', '-strict', 'experimental',
            output_path
        ]
        subprocess.run(command, check=True)
        print(f"[✅] Video created at: {output_path}")
        return output_path

    def add_audio_to_video(self, video_file: str, audio_file: str) -> str:
        print("[🎧] Adding audio to video...")
        output_path = self._get_next_output_path()
        command = [
            'ffmpeg', '-i', video_file, '-i', audio_file,
            '-c:v', 'copy', '-c:a', 'aac', '-strict', 'experimental',
            '-shortest', output_path
        ]
        subprocess.run(command, check=True)
        return output_path

    def create_video_from_images(self, image_files: List[str], fps: int = 30) -> str:
        print("[🖼️] Creating video from images...")
        output_path = self._get_next_output_path()
        images = '|'.join(image_files)
        command = f'ffmpeg -r {fps} -i "concat:{images}" -c:v libx264 -vf "fps={fps},format=yuv420p" {output_path}'
        subprocess.run(command, shell=True, check=True)
        return output_path


def search_pexels_image(query: str) -> bytes | None:
    try:
        print(f"[🔍] Searching Pexels for: {query}")
        params = {"query": query, "per_page": 1}
        response = requests.get(PEXELS_API_URL, headers=HEADERS, params=params)
        response.raise_for_status()
        data = response.json()
        if data["photos"]:
            url = data["photos"][0]["src"]["large"]
            print(f"[📸] Found image: {url}")
            return requests.get(url).content
    except Exception as e:
        print(f"[❌] Pexels image search failed: {e}")
    return None


def build_media_clip_with_context(audio_path: str, context_text: str) -> str | None:
    builder = VideoBuilder()
    output_path = builder._get_next_output_path()

    temp_image_path = None
    clips = []

    try:
        print("🎧 Loading audio...")
        audio = AudioFileClip(audio_path)
        duration = max(0.1, float(audio.duration or 0.1))

        print("🖼️ Searching for Pexels image...")
        img_data = None
        try:
            img_data = search_pexels_image(context_text[:60])
        except Exception as e:
            print(f"[⚠️] Pexels search error: {e}")

        # 🔹 שמירת התמונה הזמנית (אם נמצאה)
        if img_data:
            temp_image_path = f"temp_img_{uuid.uuid4().hex}.jpg"
            with open(temp_image_path, "wb") as f:
                f.write(img_data)
            print(f"[📸] Using Pexels image: {temp_image_path}")
        else:
            print("🎨 Using solid background")

        # 🔹 יצירת רקע
        background = create_background_clip(
            image_path=temp_image_path,
            duration=duration,
        )
        clips.append(background)

        # 🔹 יצירת שכבת טקסט (Pillow overlay)
        print("📝 Creating text overlay...")
        try:
            text_clip = create_text_overlay_clip(
                text=context_text,
                duration=duration,
            ).set_position("center")
            clips.append(text_clip)
        except Exception as e:
            print(f"[⚠️] Failed to create Pillow overlay: {e}")

        # 🔹 קומפוזיציה + יצירה
        return compose_video_with_audio(
            visual_clips=clips,
            audio_path=audio_path,
            output_path=output_path,
        )

    except Exception as e:
        print(f"[❌] Fatal error in build_media_clip_with_context: {e}")
        return None

    finally:
        try:
            if audio:
                audio.close()
        except:
            pass
        if temp_image_path and os.path.exists(temp_image_path):
            try:
                os.remove(temp_image_path)
            except:
                pass