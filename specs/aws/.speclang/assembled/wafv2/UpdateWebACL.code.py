"""Handler for UpdateWebACL — AWS WAFv2."""
def handler(store, request):
    return store.update_web_acl(
        id=request.get("Id"),
        name=request["Name"],
        scope=request["Scope"],
        lock_token=request["LockToken"],
        default_action=request["DefaultAction"],
        visibility_config=request["VisibilityConfig"],
        description=request.get("Description", ""),
        rules=request.get("Rules"))
