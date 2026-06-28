def handler(store, request: dict) -> dict:
    return store.update_firewall_policy_change_protection(
        FirewallArn=request.get("FirewallArn"),
        FirewallName=request.get("FirewallName"),
        FirewallPolicyChangeProtection=request["FirewallPolicyChangeProtection"],
    )
