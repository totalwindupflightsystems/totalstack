def handler(store, request: dict) -> dict:
    return store.describe_group(request["identityStoreId"], request["groupId"])
