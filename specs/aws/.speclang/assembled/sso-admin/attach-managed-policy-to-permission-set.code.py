def handler(store, request: dict) -> dict:
    return store.attach_managed_policy_to_permission_set(request["instanceArn"], request["permissionSetArn"], request["managedPolicyArn"])
