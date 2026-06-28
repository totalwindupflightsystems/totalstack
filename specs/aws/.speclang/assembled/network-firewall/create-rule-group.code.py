def handler(store, request: dict) -> dict:
    return store.create_rule_group(
        RuleGroupName=request["RuleGroupName"],
        Type=request["Type"],
        Capacity=request.get("Capacity"),
        RuleGroup=request.get("RuleGroup"),
        Description=request.get("Description", ""),
        Tags=request.get("Tags"),
        Rules=request.get("Rules"),
        EncryptionConfiguration=request.get("EncryptionConfiguration"),
    )
