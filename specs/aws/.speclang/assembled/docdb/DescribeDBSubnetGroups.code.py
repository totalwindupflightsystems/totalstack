def handler(store, request: dict):
    return store.describe_subnet_groups(request.get("DBSubnetGroupName"), **{k: v for k, v in request.items() if k != "DBSubnetGroupName"})
