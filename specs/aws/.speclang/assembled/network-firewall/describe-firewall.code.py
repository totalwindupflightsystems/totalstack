def handler(store, request: dict) -> dict:
    return store.describe_firewall(
        FirewallArn=request.get("FirewallArn"),
        FirewallName=request.get("FirewallName"),
    )
