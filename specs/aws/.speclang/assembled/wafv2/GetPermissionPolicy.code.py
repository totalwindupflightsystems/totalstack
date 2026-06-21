"""Handler for GetPermissionPolicy — AWS WAFv2."""
def handler(store, request):
    return store.get_permission_policy(request["ResourceArn"])
