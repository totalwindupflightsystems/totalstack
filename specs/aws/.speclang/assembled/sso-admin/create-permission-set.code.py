def handler(store, request: dict) -> dict:
    return store.create_permission_set(request["name"], request["instanceArn"], description=request.get("description"), relayState=request.get("relayState"), sessionDuration=request.get("sessionDuration"), tags=request.get("tags"))
