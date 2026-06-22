def delete_access_policy(store, request):
    return store.delete_access_policy(
        type=request["type"], name=request["name"])
