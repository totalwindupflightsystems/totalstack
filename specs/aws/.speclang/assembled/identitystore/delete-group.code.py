def handler(store, request: dict) -> dict:
    return store.delete_group(request["identityStoreId"], request["groupId"])
