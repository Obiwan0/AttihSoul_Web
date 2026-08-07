import os
from pathlib import Path

import psycopg
from dotenv import load_dotenv

# Load environment variables from .env (project root)
BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_PATH = BASE_DIR / ".env"
load_dotenv(ENV_PATH)


def get_connection():
    """Return a psycopg connection to Supabase PostgreSQL."""
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        raise RuntimeError(
            "DATABASE_URL is not set. Add it to the .env file at the project root."
        )
    return psycopg.connect(database_url)