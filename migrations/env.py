from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context
import sys, os

import os
import importlib
import inspect

sys.path.append('/home/www/work/train/art')

from config.database import metadata, Base
from config.settings import apps_folder
from config.env_variables import DATABASE_URL

config = context.config
section = config.config_ini_section
sslmode = True
config.set_main_option('sqlalchemy.url', f'{DATABASE_URL}?async_fallback=True&ssl=require')


def import_app_models():
    models = {}
    
    # Перебираем все папки в директории 'apps'
    for app_name in os.listdir(apps_folder):
        app_path = os.path.join(apps_folder, app_name)
        
        # Проверяем, является ли это папкой и есть ли в ней файл 'models.py'
        if os.path.isdir(app_path) and os.path.exists(os.path.join(app_path, "models.py")):
            module_name = f"{apps_folder}.{app_name}.models"
            module = importlib.import_module(module_name)
            
            # Импортируем и фильтруем модели
            for name, obj in inspect.getmembers(module):
                if inspect.isclass(obj) and issubclass(obj, Base):
                    models[name] = obj
    
    return models

app_models = import_app_models()

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = metadata

def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

def autogenerate_cmd():
    import subprocess
    subprocess.run(["python3", "autogenerate.py"])


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
