def create_security_policy(store, request):
    return store.create_security_policy(
        type=request.get("type", "encryption"), name=request.get("name", "security-policy"),
        policy=request.get("policy", {}), description=request.get("description"))
