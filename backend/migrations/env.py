import os
import sys
from logging.config import fileConfig
from pathlib import Path

from alembic import context
from sqlalchemy import engine_from_config, pool

BACKEND_DIR = Path(__file__).resolve().parent.parent
PROJECT_ROOT = BACKEND_DIR.parent
SRC_DIR = BACKEND_DIR / "src"

for path in (str(BACKEND_DIR), str(SRC_DIR)):
    if path not in sys.path:
        sys.path.insert(0, path)


def _load_env(env_path: Path) -> None:
    if not env_path.is_file():
        return
    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


# Top-level dr_portal/.env takes priority over backend/.env if both exist
_load_env(PROJECT_ROOT / ".env")
_load_env(BACKEND_DIR / ".env")

# Update these imports to match your actual Base and model paths inside backend/src/
from src.user.model.user_model import Base  # noqa: E402

config = context.config

db_url = os.getenv("DATABASE_URL")
if not db_url and os.getenv("POSTGRES_USER"):
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD", "")
    host = os.getenv("POSTGRES_HOST", "localhost")
    port = os.getenv("POSTGRES_PORT", "5432")
    db = os.getenv("POSTGRES_DB", "")
    db_url = f"postgresql+psycopg://{user}:{password}@{host}:{port}/{db}"

if db_url:
    config.set_main_option("sqlalchemy.url", db_url.replace("%", "%%"))

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata