def list_file_shares(store, request: dict) -> dict:
    return store.list_file_shares(
        GatewayARN=request.get("GatewayARN"),
        Marker=request.get("Marker"),
        Limit=request.get("Limit"),
    )
