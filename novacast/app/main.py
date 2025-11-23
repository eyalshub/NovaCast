from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.connection import init_db
from app.telemetry.metrics import init_metrics
from app.telemetry.tracing import init_tracing
from app.worker.queue import init_worker

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    await init_db()
    init_metrics()
    init_tracing()
    init_worker()

@app.on_event("shutdown")
async def shutdown_event():
    # Add any shutdown logic here if necessary
    pass

# Include routers for API endpoints
# from app.api.v1 import router as api_router
# app.include_router(api_router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)