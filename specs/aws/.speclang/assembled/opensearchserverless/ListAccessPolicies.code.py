def list_access_policies(store, request):
    args = {k: v for k, v in request.items() if k != "type"}
    return store.list_access_policies(type=request["type"], **args)
