def delete_policy(store, request: dict) -> dict:
    return store.delete_policy(
        PolicyStoreId=request["PolicyStoreId"],
        PolicyId=request["PolicyId"],
    )
