def delete_tape(store, request: dict) -> dict:
    return store.delete_tape(
        GatewayARN=request["GatewayARN"],
        TapeARN=request["TapeARN"],
    )
