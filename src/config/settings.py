from pydantic import BaseSettings
from dotenv import load_dotenv


load_dotenv()

class Settings(BaseSettings):
    db: str 
    user: str
    password: str
    host: str
    port: str

    class Config:
        env_file = ".env"
        env_prefix = "postgres_"

    def url(self):
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}"


settings = Settings()
