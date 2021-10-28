import sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

from config import POSTGRESQL_URL, APP_NAME, APP_MODE

database_uri = f"{POSTGRESQL_URL}{APP_NAME}-{APP_MODE}"

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
alembic = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(alembic.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = None

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.

db_confirmation = input("Connecting to {uri}... continue [Y/n]? ".format(uri=database_uri)) or "Y"

if db_confirmation not in ("Y", "y"):
    print("Goodbye!")
    sys.exit()

alembic.set_main_option("sqlalchemy.url", database_uri)

connectable = engine_from_config(
    alembic.get_section(alembic.config_ini_section), prefix="sqlalchemy.", poolclass=pool.NullPool,
)

with connectable.connect() as connection:
    context.configure(connection=connection, target_metadata=target_metadata)

    try:
        with context.begin_transaction():
            context.execute("SET session statement_timeout TO {};".format(5000))  # in ms
            context.run_migrations()
    finally:
        connection.close()
