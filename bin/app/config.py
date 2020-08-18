"""Runtime configuration loads here."""
import os

from pathlib import Path

# For config file loading
APP_ROOT_PATH = Path(os.path.dirname(os.path.realpath(__file__)))

# For config file loading
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")

# Primary database for this app
DATABASE_URL = os.environ["DATABASE_URL"]

####
# Tasks
##

# Brokers for this app's workers
CELERY_BROKER = os.environ["CELERY_BROKER"]

CELERY_TASK_ALWAYS_EAGER = os.environ.get("CELERY_TASK_ALWAYS_EAGER", "false")

# Periodicity of units sync
SOME_TASK_CRON = os.environ["SOME_TASK_CRON"]
