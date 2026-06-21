def handler(store, request: dict) -> dict:
    name = request.get("DBSubnetGroupName")
    return store.describe_subnet_groups(name)
