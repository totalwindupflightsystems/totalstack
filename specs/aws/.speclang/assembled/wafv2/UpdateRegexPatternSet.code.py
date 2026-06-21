"""Handler for UpdateRegexPatternSet — AWS WAFv2."""
def handler(store, request):
    return store.update_regex_pattern_set(
        id=request.get("Id"),
        name=request["Name"],
        scope=request["Scope"],
        lock_token=request["LockToken"],
        regular_expression_list=request["RegularExpressionList"],
        description=request.get("Description", ""))
