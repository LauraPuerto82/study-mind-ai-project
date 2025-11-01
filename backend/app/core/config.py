from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    # App metadata
    PROJECT_NAME: str = "StudyMind AI"  # ← Valores por defecto
    VERSION: str = "0.1.0"
    API_PREFIX: str = "/api/v1"

    # Database - ESTAS se leen del .env (no tienen valor por defecto)
    POSTGRES_USER: str  # ← Debe estar en .env
    POSTGRES_PASSWORD: str  # ← Debe estar en .env
    POSTGRES_DB: str  # ← Debe estar en .env
    POSTGRES_HOST: str = "localhost"  # ← Tiene default
    POSTGRES_PORT: int = 5432  # ← Tiene default

    @property
    def DATABASE_URL(self) -> str:
        # ↑ Esta función construye la URL de conexión automáticamente
        # Ejemplo resultado: "postgresql://studymind:password123@localhost:5432/studymind_db"
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    # Security
    SECRET_KEY: str  # ← Clave para firmar los JWT tokens
    ALGORITHM: str = "HS256"  # ← Algoritmo de encriptación
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30  # ← Tokens duran 30 min

    model_config = SettingsConfigDict(
        env_file=str(BASE_DIR / ".env"), case_sensitive=True
    )


settings = Settings()  # type: ignore
