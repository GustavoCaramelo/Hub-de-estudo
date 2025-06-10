import sys
import os
from pathlib import Path

# Garante que o Python encontre o módulo app
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from alembic import context
from sqlalchemy import engine_from_config, pool
from logging.config import fileConfig
from alembic.config import Config
from dotenv import load_dotenv

load_dotenv()

config = context.config

db_url = os.getenv("DATABASE_URL")
if not db_url:
    raise ValueError("A variável de ambiente DATABASE_URL não está definida.")

config.set_main_option("sqlalchemy.url", db_url)

fileConfig(config.config_file_name)

from app.database import Base
from app import models

target_metadata = Base.metadata
