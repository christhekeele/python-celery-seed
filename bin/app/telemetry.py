import newrelic.agent

EVENT_NAMESPACE = "DiscrepancyMonitoring"


def report(event, data):
    newrelic.agent.record_custom_event(EVENT_NAMESPACE, dict(**data, event=event))
