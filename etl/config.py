import os
from pathlib import Path
from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parent.parent
load_dotenv(ROOT_DIR / ".env")

def get_env_or_fail(key: str) -> str:
    val = os.getenv(key)
    if not val:
        raise ValueError(
            f"Missing required environment variable '{key}'. "
            f"Copy .env.example to .env and configure your credentials."
        )
    return val

# Connection parameters
IMMICH_DB_HOST = get_env_or_fail("IMMICH_DB_HOST")
IMMICH_DB_PORT = os.getenv("IMMICH_DB_PORT", "5432")
IMMICH_DB_NAME = os.getenv("IMMICH_DB_NAME", "immich")
IMMICH_DB_USER = os.getenv("IMMICH_DB_USER", "postgres")
IMMICH_DB_PASSWORD = get_env_or_fail("IMMICH_DB_PASSWORD")

TARGET_DB_HOST = os.getenv("TARGET_DB_HOST", "localhost")
TARGET_DB_PORT = os.getenv("TARGET_DB_PORT", "6543")
TARGET_DB_NAME = os.getenv("TARGET_DB_NAME", "immich_analytics")
TARGET_DB_USER = os.getenv("TARGET_DB_USER", "course_admin")
TARGET_DB_PASSWORD = os.getenv("TARGET_DB_PASSWORD", "secretpassword")

IMMICH_SOURCE_URI = (
    f"postgresql://{IMMICH_DB_USER}:{IMMICH_DB_PASSWORD}@"
    f"{IMMICH_DB_HOST}:{IMMICH_DB_PORT}/{IMMICH_DB_NAME}"
)

TARGET_COURSE_URI = (
    f"postgresql://{TARGET_DB_USER}:{TARGET_DB_PASSWORD}@"
    f"{TARGET_DB_HOST}:{TARGET_DB_PORT}/{TARGET_DB_NAME}"
)