from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    """Настройки приложения, загружаемые из .env"""
    rabbitmq_url: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
