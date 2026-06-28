def put_schema(store, request: dict) -> dict:
    return store.put_schema(
        PolicyStoreId=request["PolicyStoreId"],
        Definition=request["Definition"],
    )
