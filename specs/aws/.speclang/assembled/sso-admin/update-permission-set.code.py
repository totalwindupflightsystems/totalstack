def handler(store, request: dict) -> dict:
    return store.update_permission_set(request["instanceArn"], request["permissionSetArn"], description=request.get("description"), relayState=request.get("relayState"), sessionDuration=request.get("sessionDuration"))
