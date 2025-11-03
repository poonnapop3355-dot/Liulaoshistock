from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Bookstore Admin"
    API_V1_STR: str = "/api/v1"
    JWT_SECRET: str = "change_me"
    JWT_EXPIRES_IN: int = 3600

    class Config:
        case_sensitive = True

settings = Settings()
