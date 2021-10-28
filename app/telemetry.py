from config import TELEMETRY_ENABLED


def notice_event(event_type, **event):
    event["type"] = event_type

    if TELEMETRY_ENABLED:
        pass  # Not using any telemetry services in app yet
