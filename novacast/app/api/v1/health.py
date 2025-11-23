from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
async def health_check():
    return {"status": "healthy"}

@router.get("/readiness")
async def readiness_check():
    return {"status": "ready"}

@router.get("/liveness")
async def liveness_check():
    return {"status": "alive"}