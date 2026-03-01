"""
Health check endpoints
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db

router = APIRouter()


@router.get("/health")
async def health_check():
    """Basic health check"""
    return {
        "status": "healthy",
        "service": "Healthcare Clinical AI Assistant"
    }


@router.get("/health/db")
async def database_health(db: Session = Depends(get_db)):
    """Database health check"""
    try:
        # Execute a simple query
        db.execute("SELECT 1")
        return {
            "status": "healthy",
            "database": "connected"
        }
    except Exception as e:
        return {
            "status": "unhealthy",
            "database": "disconnected",
            "error": str(e)
        }


@router.get("/health/ready")
async def readiness_check():
    """Readiness check for Kubernetes"""
    return {
        "status": "ready"
    }


@router.get("/health/live")
async def liveness_check():
    """Liveness check for Kubernetes"""
    return {
        "status": "alive"
    }
