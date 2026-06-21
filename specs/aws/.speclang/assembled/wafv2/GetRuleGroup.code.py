"""Handler for GetRuleGroup — AWS WAFv2."""
def handler(store, request):
    record = store.get_rule_group(
        id=request.get("Id"),
        name=request.get("Name"),
        scope=request["Scope"])
    return {
        "RuleGroup": {
            "Id": record.id, "Name": record.name, "ARN": record.arn,
            "Capacity": record.capacity,
            "VisibilityConfig": record.visibility_config,
            "Rules": record.rules,
            "Description": record.description,
            "LockToken": record.lock_token,
        }
    }
