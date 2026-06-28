def handler(store, request: dict) -> dict:
    return store.delete_inline_policy_from_permission_set(request["instanceArn"], request["permissionSetArn"])
