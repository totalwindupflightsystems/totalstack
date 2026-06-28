def handler(store, request: dict) -> dict:
    return store.update_subnet_change_protection(
        FirewallArn=request.get("FirewallArn"),
        FirewallName=request.get("FirewallName"),
        SubnetChangeProtection=request["SubnetChangeProtection"],
    )
