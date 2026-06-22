def handler(store, request: dict):
    return store.describe_instances(request.get("DBInstanceIdentifier"), **{k: v for k, v in request.items() if k != "DBInstanceIdentifier"})
