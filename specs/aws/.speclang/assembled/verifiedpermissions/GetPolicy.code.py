def get_policy(store, request: dict) -> dict:
    return store.get_policy(
        PolicyStoreId=request["PolicyStoreId"],
        PolicyId=request["PolicyId"],
    )
