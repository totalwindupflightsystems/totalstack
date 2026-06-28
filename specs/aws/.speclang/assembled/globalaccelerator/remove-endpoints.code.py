def handler(store, request: dict) -> dict:
    return store.remove_endpoints(
        EndpointGroupArn=request["EndpointGroupArn"],
        EndpointIdentifiers=request["EndpointIdentifiers"],
    )
