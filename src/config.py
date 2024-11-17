import os 
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
from starlette.config import Config

# 환경 변수 로드 및 오버라이드
load_dotenv(".env", override=True)

# Config 객체 생성 (데이터 우선 순위: 1. 환경 변수, 2. .env 파일, 3. 기본값)
config = Config()

class AppSettings(BaseSettings):
    APP_NAME: str = config("APP_NAME", default="FastAPI app")
    APP_DESCRIPTION: str | None = config("APP_DESCRIPTION", default=None)
    APP_VERSION: str | None = config("APP_VERSION", default=None)
    LICENSE_NAME: str | None = config("LICENSE", default=None)
    CONTACT_NAME: str | None = config("CONTACT_NAME", default=None)
    CONTACT_EMAIL: str | None = config("CONTACT_EMAIL", default=None)

class PostgresDBSettings(BaseSettings):
    POSTGRES_USER: str = config("POSTGRES_USER", default="postgres")
    POSTGRES_PASSWORD: str = config("POSTGRES_PASSWORD", default="postgres")
    POSTGRES_SERVER: str = config("POSTGRES_SERVER", default="localhost")
    POSTGRES_PORT: int = config("POSTGRES_PORT", default=5432)
    POSTGRES_DB: str = config("POSTGRES_DB", default="postgres")
    POSTGRES_SYNC_PREFIX: str = config("POSTGRES_SYNC_PREFIX", default="postgresql://")
    POSTGRES_ASYNC_PREFIX: str = config("POSTGRES_ASYNC_PREFIX", default="postgresql+asyncpg://")
    POSTGRES_URI: str = f"{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    POSTGRES_URL: str | None = config("POSTGRES_URL", default=None)

class MongoDBSettings(BaseSettings):
    MONGO_URL: str = config("MONGO_URL", default=None)
    MONGO_USER_NAME: str = config("MONGO_USER_NAME", default=None)
    MONGO_USER_PASSWORD: str = config("MONGO_USER_PASSWORD", default=None)
    MONGO_DB_NAME: str = config("MONGO_DB_NAME", default=None)

    def get_mongo_url(self) -> str:
        """
        MongoDB connection string을 생성합니다.
        """
        return f"mongodb://{self.MONGO_USER_NAME}:{self.MONGO_USER_PASSWORD}@{self.MONGO_URL}/"
    
class Settings(
    AppSettings,
    PostgresDBSettings,
    MongoDBSettings
):
    pass

settings = Settings()
