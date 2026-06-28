def handler(store, request: dict) -> dict:
    return store.create_firewall_policy(
        FirewallPolicyName=request["FirewallPolicyName"],
        FirewallPolicy=request["FirewallPolicy"],
        Description=request.get("Description", ""),
        Tags=request.get("Tags"),
        EncryptionConfiguration=request.get("EncryptionConfiguration"),
    )
