def create_access_policy(store, request):
    return store.create_access_policy(
        type=request.get("type",""), name=request.get("name",""),
        policy=request.get("policy",""), description=request.get("description"))
