def activate_gateway(store, request: dict) -> dict:
    return store.activate_gateway(
        ActivationKey=request["ActivationKey"],
        GatewayName=request.get("GatewayName"),
        GatewayTimezone=request.get("GatewayTimezone"),
        GatewayType=request.get("GatewayType"),
        Tags=request.get("Tags"),
    )
