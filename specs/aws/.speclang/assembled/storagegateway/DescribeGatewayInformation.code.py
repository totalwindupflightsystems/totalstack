def describe_gateway_information(store, request: dict) -> dict:
    return store.describe_gateway_information(GatewayARN=request["GatewayARN"])
