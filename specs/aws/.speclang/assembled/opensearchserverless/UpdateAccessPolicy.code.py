def update_access_policy(store, request):
    return store.update_access_policy(
        type=request["type"], name=request["name"],
        policyVersion=request["policyVersion"],
        description=request.get("description"),
        policy=request.get("policy"))
