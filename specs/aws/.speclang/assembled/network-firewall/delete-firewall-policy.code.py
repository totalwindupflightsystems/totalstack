def handler(store, request: dict) -> dict:
    return store.delete_firewall_policy(
        FirewallPolicyArn=request.get("FirewallPolicyArn"),
        FirewallPolicyName=request.get("FirewallPolicyName"),
    )
