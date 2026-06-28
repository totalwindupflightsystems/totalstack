def handler(store, request: dict) -> dict:
    return store.describe_instance(request["instanceArn"])
