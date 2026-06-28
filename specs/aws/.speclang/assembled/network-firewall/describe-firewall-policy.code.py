def handler(store, request: dict) -> dict:
    return store.describe_firewall_policy(
        FirewallPolicyArn=request.get("FirewallPolicyArn"),
        FirewallPolicyName=request.get("FirewallPolicyName"),
    )
