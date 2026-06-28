def handler(store, request: dict) -> dict:
    return store.update_user(request["identityStoreId"], request["userId"], request["operations"])
