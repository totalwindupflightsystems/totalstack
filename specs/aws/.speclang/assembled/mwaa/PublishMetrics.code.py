def publish_metrics(store, request: dict) -> dict:
    return store.publish_metrics(request["EnvironmentName"], request["MetricData"])
