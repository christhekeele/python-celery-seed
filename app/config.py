"""Runtime configuration loads here."""
import os

from pathlib import Path

# For config file loading
APP_ROOT_PATH = Path(os.path.dirname(os.path.realpath(__file__)))

DEBUGGING_ENABLED = "true" == os.environ.get("DEBUGGING_ENABLED", "false").strip()

# Log resolution
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO").strip().upper()
# Log output
LOG_RENDERER = os.environ.get("LOG_RENDERER", "PRETTY").strip().upper()

# Primary database for this app
DATABASE_URL = os.environ["DATABASE_URL"]
# Migration timeout in milliseconds
DATABASE_MIGRATION_TIMEOUT = int(os.environ.get("DATABASE_MIGRATION_TIMEOUT", "5000"))

# New Relic Insights event namespace
NEW_RELIC_EVENT_NAMESPACE = os.environ["NEW_RELIC_EVENT_NAMESPACE"]

####
# Tasks
##

# Brokers for this app's workers
CELERY_BROKER = os.environ["CELERY_BROKER"]

CELERY_TASK_ALWAYS_EAGER = os.environ.get("CELERY_TASK_ALWAYS_EAGER", "false")

# Periodicity of units sync
NEW_YEAR_CRON = os.environ["NEW_YEAR_CRON"]
