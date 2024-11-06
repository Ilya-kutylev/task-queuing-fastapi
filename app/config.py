"""File with settings and configs for the project"""
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
import os


class Settings(BaseSettings):
    # Basic application settings
    PROJECT_NAME: str = Field(env="PROJECT_NAME")

    # Database settings
    DATABASE_URL: str = Field(env="DATABASE_URL")
    DB_NAME: str = Field(env="DB_NAME")
    DB_USER: str = Field(env="DB_USER")
    DB_PASSWORD: str = Field(env="DB_PASSWORD")
    DB_HOST: str = Field(env="DB_HOST")
    DB_PORT: int = Field(env="DB_PORT")

    # Settings for debugging and development
    DEBUG: bool = Field(False, env="DEBUG")

    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "../.env"),
        env_file_encoding="utf-8",
    )


settings = Settings()
