def handler(store, request: dict) -> dict:
    return store.describe_permission_set(request["instanceArn"], request["permissionSetArn"])
