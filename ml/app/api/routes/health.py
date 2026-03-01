"""
Health check endpoints for ML service
"""

from fastapi import APIRouter
from app.models.model_loader import ModelLoader

router = APIRouter()


@router.get("/health")
async def health_check():
    """Basic health check"""
    models_loaded = ModelLoader.get_loaded_models()
    return {
        "status": "healthy",
        "service": "Clinical AI ML Service",
        "models": models_loaded
    }


@router.get("/health/models")
async def model_health():
    """Check model loading status"""
    models_loaded = ModelLoader.get_loaded_models()
    total_models = len(models_loaded)

    return {
        "status": "healthy" if total_models > 0 else "degraded",
        "models_loaded": total_models,
        "models": models_loaded
    }


@router.get("/ready")
async def readiness_check():
    """Readiness check for Kubernetes"""
    models_loaded = ModelLoader.get_loaded_models()
    is_ready = len(models_loaded) > 0

    return {
        "status": "ready" if is_ready else "not_ready"
    }
