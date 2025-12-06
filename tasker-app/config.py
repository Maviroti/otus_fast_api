from os import getenv

from sqlalchemy import URL
from pathlib import Path

from pydantic import BaseModel, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent


class DbConfig(BaseModel):
    driver: str = "postgresql+psycopg"
    echo: bool = False

    host: str
    port: int = 5432
    database: str

    username: str
    password: SecretStr

    max_overflow: int = 0
    pool_size: int = 50

    @property
    def url(self) -> URL:
        return URL.create(
            self.driver,
            host=self.host,
            port=self.port,
            database=self.database,
            username=self.username,
            password=self.password.get_secret_value(),
        )


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="TASKER_APP__",
        env_nested_delimiter="__",
        env_file=(
            BASE_DIR / ".env.default",
            BASE_DIR / ".env",
        ),
    )
    db: DbConfig


settings = Settings()  # type: ignore

print(settings)
