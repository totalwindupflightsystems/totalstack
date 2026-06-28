def handler(store, request: dict) -> dict:
    return store.update_group(request["identityStoreId"], request["groupId"], request["operations"])
