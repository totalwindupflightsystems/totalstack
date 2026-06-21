"""Handler for DeleteRegexPatternSet — AWS WAFv2."""
def handler(store, request):
    return store.delete_regex_pattern_set(
        id=request.get("Id"),
        name=request.get("Name"),
        scope=request["Scope"],
        lock_token=request["LockToken"])
