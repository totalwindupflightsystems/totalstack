def delete_identity_source(store, request: dict) -> dict:
    return store.delete_identity_source(
        PolicyStoreId=request["PolicyStoreId"],
        IdentitySourceId=request["IdentitySourceId"],
    )
