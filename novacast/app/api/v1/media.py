from fastapi import APIRouter, HTTPException
from app.media.tts_engine import TSEngine
from app.media.video_builder import VideoBuilder
from app.media.publisher import Publisher

router = APIRouter()

@router.post("/process_media/")
async def process_media(script: str):
    try:
        # Step 1: Convert script to speech
        tts_engine = TSEngine()
        audio_file = await tts_engine.convert_script_to_audio(script)

        # Step 2: Create video from audio
        video_builder = VideoBuilder()
        video_file = await video_builder.create_video_from_audio(audio_file)

        # Step 3: Publish video
        publisher = Publisher()
        publish_response = await publisher.publish_video(video_file)

        return {"message": "Media processed successfully", "publish_response": publish_response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))