"""Handler for UpdateIPSet — AWS WAFv2."""
def handler(store, request):
    return store.update_ip_set(
        id=request.get("Id"),
        name=request["Name"],
        scope=request["Scope"],
        lock_token=request["LockToken"],
        addresses=request["Addresses"],
        description=request.get("Description", ""))
