"""Handler for DeletePermissionPolicy — AWS WAFv2."""
def handler(store, request):
    return store.delete_permission_policy(request["ResourceArn"])
