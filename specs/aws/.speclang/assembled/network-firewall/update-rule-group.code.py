def handler(store, request: dict) -> dict:
    return store.update_rule_group(
        UpdateToken=request["UpdateToken"],
        RuleGroupArn=request.get("RuleGroupArn"),
        RuleGroupName=request.get("RuleGroupName"),
        Type=request.get("Type"),
        RuleGroup=request.get("RuleGroup"),
        Description=request.get("Description"),
        Rules=request.get("Rules"),
        EncryptionConfiguration=request.get("EncryptionConfiguration"),
    )
