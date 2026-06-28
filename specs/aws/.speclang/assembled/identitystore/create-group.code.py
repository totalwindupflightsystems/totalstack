def handler(store, request: dict) -> dict:
    return store.create_group(request["identityStoreId"], displayName=request.get("displayName"), description=request.get("description"), DisplayName=request.get("DisplayName"), Description=request.get("Description"))
