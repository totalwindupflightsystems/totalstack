def get_policy_store(store, request: dict) -> dict:
    return store.get_policy_store(PolicyStoreId=request["PolicyStoreId"])
