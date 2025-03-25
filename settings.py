from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(extra="allow")

    APP_NAME: str = "Levenstein count"


config = Config()
