def handler(store, request: dict) -> dict:
    return store.update_instance(request["instanceArn"], name=request.get("name"))
