from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    app_name: str = "AI Video Analytics Platform"
    server_host: str = "0.0.0.0"
    server_port: int = 8001
    allowed_origins: List[str] = ["*"]
    camera_stream_urls: List[str] = []
    motion_threshold: float = 0.02
    alert_retention_hours: int = 24
    log_level: str = "INFO"

    class Config:
        env_file = ".env"

settings = Settings()