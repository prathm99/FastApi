import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)



class Settings:
    PROJECT_TITLE: str = "Prathmesh's Blog 🚀"
    PROJECT_VERSION: str = "0.1.0 🫶🏻"

    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", default="localhost")
    POSTGRES_PORT: int = os.getenv("POSTGRES_PORT", default="5432")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    DATABASE_URL: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

settings = Settings()