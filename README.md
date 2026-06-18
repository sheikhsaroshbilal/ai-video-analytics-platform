# AI Video Analytics Platform

Real-time CCTV intelligence platform built with FastAPI and Python.
Deployed on-premise at Dubai branch — processes live video feeds for business intelligence.

## Architecture
```
CCTV Cameras → Video Ingestion → AI Inference Engine → FastAPI REST API → Dashboard
```

## API Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/stream/status` | GET | Live stream health and connection status |
| `/api/v1/detect/motion` | POST | Motion detection on video frame |
| `/api/v1/analytics/summary` | GET | Aggregated analytics for time period |
| `/api/v1/alerts` | GET | Active alerts and threshold breaches |

## Tech Stack
- **API**: FastAPI (Python 3.11)
- **AI/ML**: OpenCV, NumPy for computer vision
- **Infrastructure**: On-premise server, systemd service
- **Monitoring**: Health endpoints, structured JSON logging

## Running Locally
```bash
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8001 --reload
```