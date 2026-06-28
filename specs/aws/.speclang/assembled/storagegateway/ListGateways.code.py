def list_gateways(store, request: dict) -> dict:
    return store.list_gateways(
        Marker=request.get("Marker"),
        Limit=request.get("Limit"),
    )
