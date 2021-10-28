import celery

from config import (
    CELERY_BEAT_CHECK_FREQUENCY,
    CELERY_RESULT_BACKEND_URL,
    CELERY_TASK_ALWAYS_EAGER,
    RABBITMQ_URL,
    TASK_SCHEDULE_SYSTEM_HEARTBEAT,
)
import crontab

import background.hooks

# Use hooks module just for side effects
assert background.hooks
del background.hooks


####
# PRIORITIES
##

NO_PRIORITY = 1
LOW_PRIORITY = 2
NORMAL_PRIORITY = 3
HIGH_PRIORITY = 4
MAX_PRIORITY = 5
PRIORITIES = [
    NO_PRIORITY,
    LOW_PRIORITY,
    NORMAL_PRIORITY,
    HIGH_PRIORITY,
    MAX_PRIORITY,
]


####
# TASK REGISTRY
##


registry = celery.Celery("app", broker=RABBITMQ_URL, include=["background.tasks.system",])

####
# General
##

# Use UTC
registry.conf.timezone = "UTC"
registry.conf.enable_utc = True
# Consult config for sync/async settings
registry.conf.task_always_eager = CELERY_TASK_ALWAYS_EAGER

# Serialization

# Always serialize data into tasks as json
registry.conf.task_serializer = "json"
registry.conf.result_serializer = "json"
# Reject non-json content
registry.conf.accept_content = ["json"]

####
# Results
##
registry.conf.result_backend = CELERY_RESULT_BACKEND_URL

####
# Queues
##

# Create missing queues by default
registry.conf.task_create_missing_queues = True
# Use 'default' as default queue name instead of 'celery'
# registry.conf.task_default_queue = 'celery'
registry.conf.task_default_queue = "default"

####
# Schedules
##

registry.conf.beat_schedule = {
    "heartbeat": {"task": "background.tasks.system.heart", "schedule": crontab.parse(TASK_SCHEDULE_SYSTEM_HEARTBEAT),}
}
registry.conf.beat_max_loop_interval = CELERY_BEAT_CHECK_FREQUENCY

####
# Priorities
##

# Keep within RabbitMQ's max priority size
# registry.conf.task_queue_max_priority = 10
# We want fewer priorities, for simplicity and performance
registry.conf.task_queue_max_priority = MAX_PRIORITY
# Default tasks to normal priority
registry.conf.task_default_priority = NORMAL_PRIORITY


####
# Entrypoint
##

if __name__ == "__main__":
    import sys

    registry.start(sys.argv)
