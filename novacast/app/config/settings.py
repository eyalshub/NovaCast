# app/config/settings.py
from pydantic_settings import BaseSettings
from pydantic import Field, ConfigDict  # ✅ הוסף את זה
from typing import Optional

class Settings(BaseSettings):
    model_config = ConfigDict(  # ✅ החלפה ל־Pydantic v2
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    # Application settings
    app_name: str = "NovaCast"
    app_version: str = "1.0.0"
    
    # Database settings
    db_url: Optional[str] = None
    db_name: Optional[str] = None
    db_user: Optional[str] = None
    db_password: Optional[str] = None
    
    # API settings
    api_key: Optional[str] = None
    jwt_secret: Optional[str] = None
    oauth2_client_id: Optional[str] = None
    oauth2_client_secret: Optional[str] = None
    
    # Telemetry settings
    telemetry_enabled: bool = True
    prometheus_url: str = "http://localhost:9090"
    
    # LLM settings (Ollama etc.)
    ollama_host: str = Field(default="http://localhost:11434")
    ollama_model: str = Field(default="llama3.2:latest")
    ollama_timeout: int = Field(default=120)
    llm_provider: str = Field(default="ollama")

    # Other settings
    log_level: str = "INFO"

settings = Settings()
