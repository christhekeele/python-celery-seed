from background.worker import registry


@registry.task()
def heart():
    return "beat"


@registry.task()
def healthcheck():
    return "healthy"
