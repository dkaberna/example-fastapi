from pydantic_settings import BaseSettings, SettingsConfigDict
import dotenv
#from pydantic import BaseSettings

# Default values below are a hack!  Otherwise it errors out!
# Using an older version of FastAPI for purposes of the YouTube course
class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    model_config = SettingsConfigDict(env_file=".env")
    #class Config:
    #    env_file = "app/.env"

settings = Settings()