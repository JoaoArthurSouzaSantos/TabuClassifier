from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context
from models.user_model import db  # Importe o SQLAlchemy e o modelo de sua aplicação
from models.user_model import User  # Importando o modelo User

# Esta linha garante que a metadata do SQLAlchemy será usada
target_metadata = db.metadata

# Arquivo de configuração de log
config = context.config
fileConfig(config.config_file_name)

def run_migrations_offline():
    """Executa migrações no modo offline sem conexão com o banco de dados."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Executa migrações no modo online com uma conexão ativa com o banco de dados."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
