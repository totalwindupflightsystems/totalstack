def create_lifecycle_policy(store, request):
    return store.create_lifecycle_policy(
        type=request.get("type", "retention"), name=request.get("name", "lifecycle-policy"),
        policy=request.get("policy", {}), description=request.get("description"))
