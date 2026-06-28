def handler(store, request: dict) -> dict:
    return store.delete_listener(request["ListenerArn"])
