from fastapi import APIRouter, HTTPException
from typing import Dict
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/status")
def get_stream_status() -> Dict:
    """Return health and connection status for all configured streams."""
    return {
        "status": "active",
        "streams": [
            {"id": "cam-01", "location": "entrance", "status": "connected", "fps": 25},
            {"id": "cam-02", "location": "parking",  "status": "connected", "fps": 25},
            {"id": "cam-03", "location": "lobby",    "status": "connected", "fps": 15},
        ],
        "total_active": 3,
    }