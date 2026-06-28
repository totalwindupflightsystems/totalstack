def handler(store, request: dict) -> dict:
    return store.put_inline_policy_to_permission_set(request["instanceArn"], request["permissionSetArn"], request["inlinePolicy"])
