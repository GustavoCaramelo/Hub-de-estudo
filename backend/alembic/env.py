from logging import config
from sqlalchemy.engine.url import URL
import os

config.set_main_option("sqlalchemy.url", os.getenv("DATABASE_URL"))