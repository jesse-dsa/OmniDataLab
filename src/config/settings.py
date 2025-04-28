import os
from dotenv import load_dotenv

# Carregar .env
load_dotenv()


class Settings:
    POSTGRES_DB = os.getenv("POSTGRES_DB")
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_HOST = os.getenv("POSTGRES_HOST")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT")
    POSTGRES_MINCONN = int(os.getenv("POSTGRES_MINCONN", 1))
    POSTGRES_MAXCONN = int(os.getenv("POSTGRES_MAXCONN", 10))


settings = Settings()
