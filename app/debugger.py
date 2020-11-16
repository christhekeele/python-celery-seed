import debugpy

import app.config


def start():
    if app.config.DEBUGGING_ENABLED:
        # 5678 is the default attach port in the VS Code debug configurations.
        # Unless a host and port are specified, host defaults to 127.0.0.1
        debugpy.listen(5678)
        print("Waiting for debugger to attach...")
        debugpy.wait_for_client()
        debugpy.breakpoint()
