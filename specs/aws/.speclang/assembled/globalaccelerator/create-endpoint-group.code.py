def handler(store, request: dict) -> dict:
    return store.create_endpoint_group(
        EndpointGroupRegion=request["EndpointGroupRegion"],
        ListenerArn=request["ListenerArn"],
        EndpointConfigurations=request.get("EndpointConfigurations"),
        HealthCheckIntervalSeconds=request.get("HealthCheckIntervalSeconds"),
        HealthCheckPath=request.get("HealthCheckPath"),
        HealthCheckPort=request.get("HealthCheckPort"),
        HealthCheckProtocol=request.get("HealthCheckProtocol"),
        IdempotencyToken=request.get("IdempotencyToken"),
        PortOverrides=request.get("PortOverrides"),
        ThresholdCount=request.get("ThresholdCount"),
        TrafficDialPercentage=request.get("TrafficDialPercentage"),
    )
