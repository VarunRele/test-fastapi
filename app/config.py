from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    DB_USER: str
    DB_PASSWORD: str
    DB_IP: str
    DB_PORT: str
    DB_NAME: str
    model_config = SettingsConfigDict(env_file='.env')


setting = Settings()