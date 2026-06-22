def handler(store, request: dict):
    return store.delete_instance(request["DBInstanceIdentifier"])
