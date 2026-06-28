def handler(store, request: dict) -> dict:
    return store.describe_application(request["applicationArn"])
