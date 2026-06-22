def handler(store, request: dict) -> dict:
    return store.delete_user(request["UserName"])

