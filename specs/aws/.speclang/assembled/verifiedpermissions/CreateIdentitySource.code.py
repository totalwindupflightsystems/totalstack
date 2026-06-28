def create_identity_source(store, request: dict) -> dict:
    return store.create_identity_source(
        PolicyStoreId=request["PolicyStoreId"],
        Configuration=request["Configuration"],
        PrincipalEntityType=request.get("PrincipalEntityType"),
        Tags=request.get("Tags"),
    )
