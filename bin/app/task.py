import celery
from celery.schedules import crontab

import app.config


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


def schedule(spec):
    """Parses cron-style strings into celery crontab schedules.

    Fails without a year field specified, but silently discards the value
    since celery cannot leverage it.

    For more crontab documentation, see:

    - AWS cron string syntax:
        https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html
    - Celery cron field syntax:
        https://docs.celeryproject.org/en/stable/reference/celery.schedules.html#celery.schedules.crontab
    """
    (minute, hour, day_of_month, month_of_year, day_of_week, _year) = spec.split(" ", 6)
    return crontab(
        minute=minute, hour=hour, day_of_week=day_of_week, day_of_month=day_of_month, month_of_year=month_of_year
    )


####
# TASK REGISTRY
##

registry = celery.Celery(
    "discrepancy-monitoring", broker=app.config.CELERY_BROKER, include=["app.tasks.units", "app.tasks.sync"]
)

####
# General
##

registry.conf.task_always_eager = app.config.CELERY_TASK_ALWAYS_EAGER == "true"

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
    # "some-task": {"task": "app.tasks.some.task", "schedule": schedule(app.config.SOME_TASK_CRON)}
}

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
