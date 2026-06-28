def handler(store, request: dict) -> dict:
    return store.describe_listener(request["ListenerArn"])
