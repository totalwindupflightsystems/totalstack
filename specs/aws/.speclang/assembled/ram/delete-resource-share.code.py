def handler(store, request: dict) -> dict:
    return store.delete_resource_share(
        request["resourceShareArn"],
        clientToken=request.get("clientToken"),
    )
