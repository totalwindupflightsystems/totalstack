def handler(store, request: dict) -> dict:
    return store.create_permission(
        name=request["name"],
        resourceType=request["resourceType"],
        policyTemplate=request["policyTemplate"],
        clientToken=request.get("clientToken"),
        tags=request.get("tags"),
    )
