def create_lifecycle_policy(store, request):
    return store.create_lifecycle_policy(
        type=request.get("type",""), name=request.get("name",""),
        policy=request.get("policy",""), description=request.get("description"))
