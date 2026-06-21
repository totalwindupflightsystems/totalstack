"""Handler for DeleteIPSet — AWS WAFv2."""
def handler(store, request):
    return store.delete_ip_set(
        id=request.get("Id"),
        name=request.get("Name"),
        scope=request["Scope"],
        lock_token=request["LockToken"])
