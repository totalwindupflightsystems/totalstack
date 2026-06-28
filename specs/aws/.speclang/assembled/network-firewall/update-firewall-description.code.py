def handler(store, request: dict) -> dict:
    return store.update_firewall_description(
        FirewallArn=request.get("FirewallArn"),
        FirewallName=request.get("FirewallName"),
        Description=request.get("Description", ""),
    )
