"""Handler for CreateRegexPatternSet — AWS WAFv2."""
def handler(store, request):
    name = request.get("Name")
    scope = request.get("Scope")
    if not name:
        raise WAFInvalidParameterException("Name is required")
    if not scope:
        raise WAFInvalidParameterException("Scope is required")
    if not request.get("RegularExpressionList"):
        raise WAFInvalidParameterException("RegularExpressionList is required")
    return store.create_regex_pattern_set(
        name=name,
        scope=scope,
        regular_expression_list=request["RegularExpressionList"],
        description=request.get("Description", ""),
        tags=request.get("Tags"))
