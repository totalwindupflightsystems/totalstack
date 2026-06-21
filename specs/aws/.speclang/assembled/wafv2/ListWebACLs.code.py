"""Handler for ListWebACLs — AWS WAFv2."""
def handler(store, request):
    return store.list_web_acls(
        scope=request["Scope"],
        next_marker=request.get("NextMarker"),
        limit=request.get("Limit"))
