def handler(store, request: dict) -> dict:
    return store.update_firewall_policy(
        UpdateToken=request["UpdateToken"],
        FirewallPolicy=request["FirewallPolicy"],
        FirewallPolicyArn=request.get("FirewallPolicyArn"),
        FirewallPolicyName=request.get("FirewallPolicyName"),
        Description=request.get("Description"),
        EncryptionConfiguration=request.get("EncryptionConfiguration"),
    )
