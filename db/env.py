import sys
import os
from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool


# Add inner ali_backend folder to sys.path so we can import ali_backend package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'ali_backend')))

from ali_backend.conf.db import DatabaseSettings
from db.base import Base

settings = DatabaseSettings()

# Alembic Config object, which provides access to values in .ini file
config = context.config

# Setup Python logging config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Metadata for 'autogenerate' support
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    context.configure(
        url=settings.database_url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    connectable = engine_from_config(
        {'db.url': settings.database_url, 'db.echo': 'True'},
        prefix="db.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
