"""Handler for ListIPSets — AWS WAFv2."""
def handler(store, request):
    return store.list_ip_sets(
        scope=request["Scope"],
        next_marker=request.get("NextMarker"),
        limit=request.get("Limit"))
