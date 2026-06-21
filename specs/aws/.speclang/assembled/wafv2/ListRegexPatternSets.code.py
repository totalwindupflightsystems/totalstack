"""Handler for ListRegexPatternSets — AWS WAFv2."""
def handler(store, request):
    return store.list_regex_pattern_sets(
        scope=request["Scope"],
        next_marker=request.get("NextMarker"),
        limit=request.get("Limit"))
