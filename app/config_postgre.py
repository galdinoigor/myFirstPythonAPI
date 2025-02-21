from pydantic_settings import BaseSettings
from urllib.parse import quote_plus

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:quote_plus(ibarbosa@@)@127.0.0.1:5432/database_1"
    DEBUG: bool = True

settings = Settings()