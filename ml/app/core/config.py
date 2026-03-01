"""
ML Service Configuration
"""

from typing import List
from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    """ML service settings"""

    # Application
    APP_NAME: str = "Clinical AI ML Service"
    VERSION: str = "1.0.0"
    DEBUG: bool = True

    # Model Configuration
    MODEL_CACHE_DIR: str = "/app/models"
    DEVICE: str = "cpu"  # "cpu", "cuda", or "mps"

    # OpenAI
    OPENAI_API_KEY: str = ""
    OPENAI_MODEL: str = "gpt-4"
    OPENAI_TEMPERATURE: float = 0.7
    OPENAI_MAX_TOKENS: int = 2000

    # Clinical Note Generation
    NOTE_GENERATION_MODEL: str = "meta-llama/Llama-3.2-3B-Instruct"
    NOTE_MAX_LENGTH: int = 2048
    NOTE_TEMPERATURE: float = 0.7

    # Code Suggestion
    CODE_SUGGESTION_MODEL: str = "bert-base-uncased"
    CODE_MAX_SUGGESTIONS: int = 10
    CODE_MIN_CONFIDENCE: float = 0.6

    # Summarization
    SUMMARIZATION_MODEL: str = "facebook/bart-large-cnn"
    SUMMARY_MAX_LENGTH: int = 300
    SUMMARY_MIN_LENGTH: int = 100

    # Feature Flags
    ENABLE_LLM_GENERATION: bool = True
    ENABLE_CODE_SUGGESTION: bool = True
    ENABLE_SUMMARIZATION: bool = True

    # Caching
    ENABLE_CACHE: bool = True
    CACHE_TTL: int = 3600  # 1 hour

    # Monitoring
    PROMETHEUS_ENABLED: bool = False

    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings"""
    return Settings()


settings = get_settings()
