def get_identity_source(store, request: dict) -> dict:
    return store.get_identity_source(
        PolicyStoreId=request["PolicyStoreId"],
        IdentitySourceId=request["IdentitySourceId"],
    )
