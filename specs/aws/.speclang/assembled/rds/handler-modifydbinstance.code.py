def handler(store, request: dict) -> dict:
    identifier = request["DBInstanceIdentifier"]
    kwargs = {k: v for k, v in request.items() if k != "DBInstanceIdentifier" and v is not None}
    return store.modify_instance(identifier, **kwargs)
