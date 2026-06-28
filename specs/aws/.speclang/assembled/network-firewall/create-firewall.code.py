def handler(store, request: dict) -> dict:
    return store.create_firewall(
        FirewallName=request["FirewallName"],
        FirewallPolicyArn=request["FirewallPolicyArn"],
        VpcId=request.get("VpcId"),
        SubnetMappings=request.get("SubnetMappings"),
        DeleteProtection=request.get("DeleteProtection", False),
        SubnetChangeProtection=request.get("SubnetChangeProtection", False),
        FirewallPolicyChangeProtection=request.get("FirewallPolicyChangeProtection", False),
        Description=request.get("Description", ""),
        Tags=request.get("Tags"),
        EncryptionConfiguration=request.get("EncryptionConfiguration"),
    )
