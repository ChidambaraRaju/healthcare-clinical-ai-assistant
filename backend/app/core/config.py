"""
Application configuration using Pydantic Settings
"""

from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    """Application settings"""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore"
    )

    # Application
    APP_NAME: str = "Healthcare Clinical AI Assistant"
    VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True

    # API
    API_V1_PREFIX: str = "/api/v1"
    PROJECT_NAME: str = "Healthcare Clinical AI Assistant"

    # Security
    JWT_SECRET_KEY: str = "change-me-in-production"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 60
    ENCRYPTION_KEY: str = "change-me-in-production"

    # CORS
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:8000",
        "http://127.0.0.1:3000"
    ]
    ALLOWED_HOSTS: List[str] = ["*"]

    # Database
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/clinical_ai"
    DATABASE_POOL_SIZE: int = 20
    DATABASE_MAX_OVERFLOW: int = 10

    # Redis (for cache and Celery)
    REDIS_URL: str = "redis://localhost:6379/0"

    # ML Service
    ML_SERVICE_URL: str = "http://localhost:8001"
    MODEL_CACHE_DIR: str = "/app/models"

    # Rate Limiting
    RATE_LIMIT_PER_MINUTE: int = 100
    RATE_LIMIT_BURST: int = 200

    # Session
    SESSION_TIMEOUT_MINUTES: int = 30
    MAX_SESSIONS_PER_USER: int = 5

    # MFA
    MFA_ENABLED: bool = False
    MFA_ISSUER: str = "HealthcareAI"

    # Audit Logging
    AUDIT_LOG_ENABLED: bool = True
    AUDIT_LOG_RETENTION_DAYS: int = 2190  # 6 years for HIPAA

    # AWS
    AWS_REGION: str = "us-east-1"
    S3_BUCKET_NAME: str = "clinical-ai-documents"
    CLOUDFRONT_DISTRIBUTION_ID: str = ""
    ECS_CLUSTER_NAME: str = "clinical-ai-cluster"

    # OpenAI (for LLM features)
    OPENAI_API_KEY: str = ""
    OPENAI_MODEL: str = "gpt-4"

    # HIPAA
    DATA_RETENTION_DAYS: int = 2555  # 7 years minimum
    HIPAA_MODE: bool = True

    # Logging
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "json"

    # Monitoring
    PROMETHEUS_ENABLED: bool = False
    SENTRY_DSN: str = ""

    # Feature Flags
    ENABLE_CODE_SUGGESTIONS: bool = True
    ENABLE_DOCUMENT_SUMMARY: bool = True
    ENABLE_VOICE_TRANSCRIPTION: bool = False


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance"""
    return Settings()


settings = get_settings()
