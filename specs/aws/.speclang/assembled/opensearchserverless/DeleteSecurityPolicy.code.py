def delete_security_policy(store, request):
    return store.delete_security_policy(
        type=request["type"], name=request["name"])
