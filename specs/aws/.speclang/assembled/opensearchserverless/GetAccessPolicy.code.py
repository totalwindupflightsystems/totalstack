def get_access_policy(store, request):
    return store.get_access_policy(
        type=request["type"], name=request["name"])
