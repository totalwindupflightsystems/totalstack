def get_schema(store, request: dict) -> dict:
    return store.get_schema(PolicyStoreId=request["PolicyStoreId"])
