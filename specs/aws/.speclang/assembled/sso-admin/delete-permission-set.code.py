def handler(store, request: dict) -> dict:
    return store.delete_permission_set(request["instanceArn"], request["permissionSetArn"])
