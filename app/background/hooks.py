from celery import signals as hooks
import logs


@hooks.setup_logging.connect
def setup_logging(**kwargs):
    return logs.logger
