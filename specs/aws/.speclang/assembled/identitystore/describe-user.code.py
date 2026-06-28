def handler(store, request: dict) -> dict:
    return store.describe_user(request["identityStoreId"], request["userId"])
