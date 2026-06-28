def is_authorized(store, request: dict) -> dict:
    return store.is_authorized(
        PolicyStoreId=request["PolicyStoreId"],
        Principal=request.get("Principal"),
        Action=request.get("Action"),
        Resource=request.get("Resource"),
        Context=request.get("Context"),
    )
