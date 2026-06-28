def delete_policy_store(store, request: dict) -> dict:
    return store.delete_policy_store(PolicyStoreId=request["PolicyStoreId"])
