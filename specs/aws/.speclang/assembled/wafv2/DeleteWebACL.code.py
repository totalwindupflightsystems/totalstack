"""Handler for DeleteWebACL — AWS WAFv2."""
def handler(store, request):
    return store.delete_web_acl(
        id=request.get("Id"),
        name=request["Name"],
        scope=request["Scope"],
        lock_token=request["LockToken"])
