def handler(store, request: dict) -> dict:
    return store.delete_application(request["applicationArn"])
