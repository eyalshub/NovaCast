# novacast/scripts/run_local_pipeline.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.core.orchestrator import Orchestrator

def run_local_pipeline():
    prompt = "How AI is changing education"
    orchestrator = Orchestrator()

    try:
        result = orchestrator.run_pipeline(prompt)

        print("\n🧠 Idea:")
        print(result.get("idea", ""))

        print("\n🧩 Outline:")
        for section in result.get("outline", []):
            print("-", section)

        print("\n🎬 Script:")
        script = result.get("script", "")
        print((script[:300] + "...") if isinstance(script, str) else repr(script))

        audio_path = result.get("audio_path")
        video_path = result.get("video_path")

        print("\n🎤 Audio file:", audio_path if audio_path else "(missing)")
        print("🎞️ Video file:", video_path if video_path else "(missing)")

    except Exception as e:
        print("❌ Pipeline failed:", e)

    finally:
        print("\n📜 Task History:")
        orchestrator.print_tasks()

if __name__ == "__main__":
    run_local_pipeline()
