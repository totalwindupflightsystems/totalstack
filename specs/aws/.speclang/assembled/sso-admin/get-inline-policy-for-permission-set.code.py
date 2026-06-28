def handler(store, request: dict) -> dict:
    return store.get_inline_policy_for_permission_set(request["instanceArn"], request["permissionSetArn"])
