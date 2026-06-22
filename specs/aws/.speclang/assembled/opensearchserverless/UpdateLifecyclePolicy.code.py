def update_lifecycle_policy(store, request):
    return store.update_lifecycle_policy(
        type=request["type"], name=request["name"],
        policyVersion=request["policyVersion"],
        description=request.get("description"),
        policy=request.get("policy"))
