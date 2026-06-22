def delete_lifecycle_policy(store, request):
    return store.delete_lifecycle_policy(
        type=request["type"], name=request["name"])
