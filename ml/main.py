"""
ML Service - AI inference for clinical documentation
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import structlog
from app.core.config import settings
from app.api.routes import inference, health

# Configure structured logging
structlog.configure(
    processors=[
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.JSONRenderer()
    ],
    logger_factory=structlog.stdlib.LoggerFactory(),
)

logger = structlog.get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """ML service lifespan events"""
    logger.info("Starting ML Service for Clinical AI Assistant")
    # Load models on startup
    from app.models.model_loader import ModelLoader
    ModelLoader.load_all_models()
    logger.info("All models loaded successfully")
    yield
    logger.info("Shutting down ML Service")


# Create FastAPI application
app = FastAPI(
    title="Clinical AI ML Service",
    description="AI inference service for clinical documentation and medical code suggestions",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure properly for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(health.router, prefix="/api/v1", tags=["health"])
app.include_router(inference.router, prefix="/api/v1", tags=["inference"])


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "service": "Clinical AI ML Service",
        "version": "1.0.0",
        "status": "operational"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8001,
        reload=True
    )
