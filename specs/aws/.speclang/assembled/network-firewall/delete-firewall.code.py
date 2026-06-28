def handler(store, request: dict) -> dict:
    return store.delete_firewall(
        FirewallArn=request.get("FirewallArn"),
        FirewallName=request.get("FirewallName"),
    )
