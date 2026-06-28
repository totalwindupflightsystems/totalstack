def handler(store, request: dict) -> dict:
    return store.add_endpoints(
        EndpointGroupArn=request["EndpointGroupArn"],
        EndpointConfigurations=request["EndpointConfigurations"],
    )
