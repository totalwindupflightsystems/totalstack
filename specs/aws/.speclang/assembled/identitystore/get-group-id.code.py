def handler(store, request: dict) -> dict:
    return store.get_group_id(request["identityStoreId"], request["alternateIdentifier"])
