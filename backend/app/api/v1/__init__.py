"""
API v1 Router
"""

from fastapi import APIRouter
from app.api.v1.endpoints import health, auth, patients, documents, codes

api_router = APIRouter()

# Include all route modules
api_router.include_router(health.router, tags=["health"])
api_router.include_router(auth.router, prefix="/auth", tags=["authentication"])
api_router.include_router(patients.router, prefix="/patients", tags=["patients"])
api_router.include_router(documents.router, prefix="/documents", tags=["documents"])
api_router.include_router(codes.router, prefix="/codes", tags=["medical-codes"])
