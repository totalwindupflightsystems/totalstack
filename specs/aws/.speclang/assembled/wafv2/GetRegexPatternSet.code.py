"""Handler for GetRegexPatternSet — AWS WAFv2."""
def handler(store, request):
    record = store.get_regex_pattern_set(
        id=request.get("Id"),
        name=request.get("Name"),
        scope=request["Scope"])
    return {
        "RegexPatternSet": {
            "Id": record.id, "Name": record.name, "ARN": record.arn,
            "RegularExpressionList": record.regular_expression_list,
            "Description": record.description,
            "LockToken": record.lock_token,
        }
    }
