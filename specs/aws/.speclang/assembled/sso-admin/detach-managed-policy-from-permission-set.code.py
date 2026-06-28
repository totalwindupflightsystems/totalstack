def handler(store, request: dict) -> dict:
    return store.detach_managed_policy_from_permission_set(request["instanceArn"], request["permissionSetArn"], request["managedPolicyArn"])
