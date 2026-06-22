def get_security_policy(store, request):
    return store.get_security_policy(
        type=request["type"], name=request["name"])
