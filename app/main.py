from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import stream, detection, analytics, alerts
from app.core.config import settings
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI(
    title="AI Video Analytics Platform",
    description="Real-time CCTV intelligence and monitoring API",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(stream.router,    prefix="/api/v1/stream",    tags=["stream"])
app.include_router(detection.router, prefix="/api/v1/detect",    tags=["detection"])
app.include_router(analytics.router, prefix="/api/v1/analytics", tags=["analytics"])
app.include_router(alerts.router,    prefix="/api/v1/alerts",    tags=["alerts"])

@app.get("/health")
def health():
    return {"status": "healthy", "version": "1.0.0"}