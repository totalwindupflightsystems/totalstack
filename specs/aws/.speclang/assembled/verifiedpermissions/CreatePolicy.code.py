def create_policy(store, request: dict) -> dict:
    return store.create_policy(
        PolicyStoreId=request["PolicyStoreId"],
        Definition=request["Definition"],
        Tags=request.get("Tags"),
    )
