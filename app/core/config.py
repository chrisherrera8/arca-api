from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://arca:arca@localhost:5432/arca"
    SECRET_KEY: str = "your-secret-key-here"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    CORS_ORIGINS: list[str] = ["http://localhost:5173"]

    STORAGE_BACKEND: str = "local"
    STORAGE_LOCAL_PATH: str = "./uploads"

    model_config = {"env_file": ".env", "extra": "ignore"}


settings = Settings()
