def handler(store, request: dict) -> dict:
    return store.put_account_configuration(
        ExpiryEvents=request.get("ExpiryEvents"),
        IdempotencyToken=request.get("IdempotencyToken"),
        OptInRegions=request.get("OptInRegions"),
    )
