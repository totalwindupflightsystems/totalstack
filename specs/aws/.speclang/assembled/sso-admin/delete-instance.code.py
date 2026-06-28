def handler(store, request: dict) -> dict:
    return store.delete_instance(request["instanceArn"])
