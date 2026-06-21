"""Handler for DeleteRuleGroup — AWS WAFv2."""
def handler(store, request):
    return store.delete_rule_group(
        id=request.get("Id"),
        name=request.get("Name"),
        scope=request["Scope"],
        lock_token=request["LockToken"])
