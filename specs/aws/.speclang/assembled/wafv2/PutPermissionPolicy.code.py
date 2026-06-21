"""Handler for PutPermissionPolicy — AWS WAFv2."""
def handler(store, request):
    return store.put_permission_policy(
        resource_arn=request["ResourceArn"],
        policy=request["Policy"])
