"""Handler for CreateRuleGroup — AWS WAFv2."""
def handler(store, request):
    name = request.get("Name")
    scope = request.get("Scope")
    if not name:
        raise WAFInvalidParameterException("Name is required")
    if not scope:
        raise WAFInvalidParameterException("Scope is required")
    if not request.get("VisibilityConfig"):
        raise WAFInvalidParameterException("VisibilityConfig is required")
    return store.create_rule_group(
        name=name,
        scope=scope,
        capacity=request.get("Capacity", 0),
        visibility_config=request["VisibilityConfig"],
        description=request.get("Description", ""),
        rules=request.get("Rules"),
        tags=request.get("Tags"),
        custom_response_bodies=request.get("CustomResponseBodies"))
