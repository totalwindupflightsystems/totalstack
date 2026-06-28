def handler(store, request: dict) -> dict:
    return store.create_listener(
        AcceleratorArn=request["AcceleratorArn"],
        PortRanges=request["PortRanges"],
        Protocol=request["Protocol"],
        IdempotencyToken=request.get("IdempotencyToken"),
        ClientAffinity=request.get("ClientAffinity"),
    )
