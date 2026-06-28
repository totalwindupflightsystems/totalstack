def handler(store, request: dict) -> dict:
    return store.update_firewall_delete_protection(
        FirewallArn=request.get("FirewallArn"),
        FirewallName=request.get("FirewallName"),
        DeleteProtection=request["DeleteProtection"],
    )
