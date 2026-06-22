def list_security_policies(store, request):
    args = {k: v for k, v in request.items() if k != "type"}
    return store.list_security_policies(type=request["type"], **args)
