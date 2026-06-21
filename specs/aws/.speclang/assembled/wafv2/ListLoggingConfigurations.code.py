"""Handler for ListLoggingConfigurations — AWS WAFv2."""
def handler(store, request):
    return store.list_logging_configurations(
        scope=request["Scope"],
        next_marker=request.get("NextMarker"),
        limit=request.get("Limit"))
