def handler(store, request: dict) -> dict:
    return store.update_endpoint_group(
        EndpointGroupArn=request["EndpointGroupArn"],
        EndpointConfigurations=request.get("EndpointConfigurations"),
        HealthCheckIntervalSeconds=request.get("HealthCheckIntervalSeconds"),
        HealthCheckPath=request.get("HealthCheckPath"),
        HealthCheckPort=request.get("HealthCheckPort"),
        HealthCheckProtocol=request.get("HealthCheckProtocol"),
        PortOverrides=request.get("PortOverrides"),
        ThresholdCount=request.get("ThresholdCount"),
        TrafficDialPercentage=request.get("TrafficDialPercentage"),
    )
