def create_tapes(store, request: dict) -> dict:
    return store.create_tapes(
        GatewayARN=request["GatewayARN"],
        TapeSizeInBytes=request["TapeSizeInBytes"],
        ClientToken=request["ClientToken"],
        NumTapesToCreate=request["NumTapesToCreate"],
        TapeBarcodePrefix=request.get("TapeBarcodePrefix"),
        PoolId=request.get("PoolId"),
        Tags=request.get("Tags"),
    )
