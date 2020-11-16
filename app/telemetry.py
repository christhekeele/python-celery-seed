import newrelic.agent

import app.config

EVENT_NAMESPACE = app.config.NEW_RELIC_EVENT_NAMESPACE


def report(event, data):
    newrelic.agent.record_custom_event(EVENT_NAMESPACE, dict(**data, event=event))
