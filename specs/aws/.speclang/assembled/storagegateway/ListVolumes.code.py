def list_volumes(store, request: dict) -> dict:
    return store.list_volumes(
        GatewayARN=request.get("GatewayARN"),
        Marker=request.get("Marker"),
        Limit=request.get("Limit"),
    )
