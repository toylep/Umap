from pydantic_settings import BaseSettings
from pydantic import Field
from typing import ClassVar


class DBSettings(BaseSettings):
    db_name: str = Field(..., env="DB_NAME")
    db_host: str = Field(..., env="DB_HOST")
    db_password: str = Field(..., env="DB_PASSWORD")
    db_user: str = Field(..., env="DB_USER")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "allow"


class Settings(BaseSettings):
    db: ClassVar = DBSettings()
