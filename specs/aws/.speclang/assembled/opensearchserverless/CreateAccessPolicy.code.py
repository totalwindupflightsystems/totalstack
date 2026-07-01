def create_access_policy(store, request):
    return store.create_access_policy(
        type=request.get("type", "data"), name=request.get("name", "access-policy"),
        policy=request.get("policy", {}), description=request.get("description"))
