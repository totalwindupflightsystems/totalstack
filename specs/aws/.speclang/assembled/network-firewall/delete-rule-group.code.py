def handler(store, request: dict) -> dict:
    return store.delete_rule_group(
        RuleGroupArn=request.get("RuleGroupArn"),
        RuleGroupName=request.get("RuleGroupName"),
        Type=request.get("Type"),
    )
