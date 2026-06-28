def handler(store, request: dict) -> dict:
    rec = store.firewalls(request.get("FirewallArn"))
    if not rec and "FirewallName" in request:
        for f in store.firewalls():
            if f.FirewallName == request["FirewallName"]:
                rec = f
                break
    if not rec:
        raise ResourceNotFoundException("Firewall not found")
    rec.FirewallPolicyArn = request["FirewallPolicyArn"]
    return {"FirewallArn": rec.FirewallArn, "FirewallName": rec.FirewallName, "FirewallPolicyArn": rec.FirewallPolicyArn, "UpdateToken": "update-token"}
