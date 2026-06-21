"""Handler for GetWebACL — AWS WAFv2."""
def handler(store, request):
    return store.get_web_acl(
        id=request.get("Id"),
        name=request.get("Name"),
        scope=request["Scope"]).to_dict()
