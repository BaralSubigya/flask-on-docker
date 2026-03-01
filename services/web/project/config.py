import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Prefer DATABASE_URL if provided, otherwise build from Postgres env vars
    POSTGRES_USER = os.getenv("POSTGRES_USER", "hello_flask")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "hello_flask")
    POSTGRES_DB = os.getenv("POSTGRES_DB", "hello_flask_dev")
    POSTGRES_HOST = os.getenv("POSTGRES_HOST", "db")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    )
