def handler(store, request: dict):
    return store.modify_instance(request["DBInstanceIdentifier"], **{k: v for k, v in request.items() if k != "DBInstanceIdentifier"})
