def handler(store, request: dict) -> dict:
    return store.describe_firewall_metadata(
        FirewallArn=request.get("FirewallArn"),
        FirewallName=request.get("FirewallName"),
    )
