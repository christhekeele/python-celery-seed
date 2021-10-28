"""Runtime configuration loads when this file is imported."""
import os

from pathlib import Path

# App meta
APP_NAME = os.environ.get("APP_NAME", "myapp").lower()
APP_MODE = os.environ.get("APP_MODE", "dev").lower()

# For config file loading
APP_ROOT_PATH = Path(os.path.dirname(os.path.realpath(__file__)))

# For config file loading
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO").upper()

####
# Databases
##

# Postgres database for this app
POSTGRESQL_URL = os.environ["POSTGRESQL_URL"]

# Redis installation for this app
REDIS_URL = os.environ["REDIS_URL"]

####
# API
##
API_HOST = os.environ["API_HOST"]
API_PORT = int(os.environ["API_PORT"])

# UVICORN
# One of: trace, debug, info, warning, error, critical
UVICORN_LOG_LEVEL = os.environ.get("UVICORN_LOG_LEVEL=error")

####
# CACHE
##

CACHE_REDIS_DATABASE = os.environ["CACHE_REDIS_DATABASE"]

####
# TASKS
##

# Brokers for this app's workers
RABBITMQ_URL = os.environ["RABBITMQ_URL"]

# This lets us externally drive whether tasks execute within a worker,
#  or immediately for local testing.
CELERY_TASK_ALWAYS_EAGER = os.environ.get("CELERY_TASK_ALWAYS_EAGER", "false") == "true"
# Redis database to use as task result store
CELERY_RESULT_BACKEND_DATABASE = os.environ.get("CELERY_RESULT_BACKEND_DATABASE", "0")
# Where we store results. This composes the redis url with a desired redis database number
CELERY_RESULT_BACKEND_URL = os.path.join(REDIS_URL, CELERY_RESULT_BACKEND_DATABASE)

CELERY_BEAT_CHECK_FREQUENCY = int(os.environ["CELERY_BEAT_CHECK_FREQUENCY"])

# Task schedules
TASK_SCHEDULE_SYSTEM_HEARTBEAT = os.environ["TASK_SCHEDULE_SYSTEM_HEARTBEAT"]


####
# TELEMETRY
##

TELEMETRY_ENABLED = os.environ.get("TELEMETRY_ENABLED", "true").lower() == "true"
