def describe_tapes(store, request: dict) -> dict:
    return store.describe_tapes(
        TapeARNs=request["TapeARNs"],
        GatewayARN=request.get("GatewayARN"),
        Marker=request.get("Marker"),
        Limit=request.get("Limit"),
    )
