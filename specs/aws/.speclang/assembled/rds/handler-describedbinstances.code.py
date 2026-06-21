def handler(store, request: dict) -> dict:
    identifier = request.get("DBInstanceIdentifier")
    filters = request.get("Filters")
    return store.describe_instances(identifier, filters)
