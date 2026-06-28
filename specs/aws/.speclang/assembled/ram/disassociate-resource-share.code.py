def handler(store, request: dict) -> dict:
    return store.disassociate_resource_share(
        request["resourceShareArn"],
        resourceArns=request.get("resourceArns"),
        principals=request.get("principals"),
        clientToken=request.get("clientToken"),
        sources=request.get("sources"),
    )
