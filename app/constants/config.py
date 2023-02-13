import os
from enum import Enum

from pydantic import AnyHttpUrl, BaseSettings


class DeploymenyEnvironment(str, Enum):
    PROD = "production"
    DEV = "development"


class Settings(BaseSettings):
    # Environment Variables
    PROJECT_NAME: str = "Echo Line Bot"
    SERVER_NAME: str = "echo_line_bot"
    SERVER_HOST: AnyHttpUrl
    SERVER_PORT: int
    API_PREFIX: str = ""

    # Line API Configs
    LINE_CHANNEL_ACCESS_TOKEN: str
    LINE_CHANNEL_SECRET: str

    class Config:
        env_file = ".env"

        if os.environ.get("ENVIRONMENT", "") == DeploymenyEnvironment.PROD:
            env_file = ".env.prod"
        elif os.environ.get("ENVIRONMENT", "") == DeploymenyEnvironment.DEV:
            env_file = ".env.dev"

        if not os.path.exists(os.getcwd() + "/" + env_file):
            env_file = ".env"


settings = Settings()
