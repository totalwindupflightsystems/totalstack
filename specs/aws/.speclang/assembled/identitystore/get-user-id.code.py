def handler(store, request: dict) -> dict:
    return store.get_user_id(request["identityStoreId"], request["alternateIdentifier"])
