"""Handler for UpdateRuleGroup — AWS WAFv2."""
def handler(store, request):
    return store.update_rule_group(
        id=request.get("Id"),
        name=request["Name"],
        scope=request["Scope"],
        lock_token=request["LockToken"],
        visibility_config=request["VisibilityConfig"],
        description=request.get("Description", ""),
        rules=request.get("Rules"))
