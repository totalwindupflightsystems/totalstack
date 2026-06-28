def delete_gateway(store, request: dict) -> dict:
    return store.delete_gateway(GatewayARN=request["GatewayARN"])
