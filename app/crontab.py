from celery.schedules import crontab


def parse(spec):
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
        minute=minute, hour=hour, day_of_week=day_of_week, day_of_month=day_of_month, month_of_year=month_of_year,
    )
