def handler(store, request: dict) -> dict:
    return store.update_listener(
        ListenerArn=request["ListenerArn"],
        PortRanges=request.get("PortRanges"),
        Protocol=request.get("Protocol"),
        ClientAffinity=request.get("ClientAffinity"),
    )
