"""Handler for ListRuleGroups — AWS WAFv2."""
def handler(store, request):
    return store.list_rule_groups(
        scope=request["Scope"],
        next_marker=request.get("NextMarker"),
        limit=request.get("Limit"))
