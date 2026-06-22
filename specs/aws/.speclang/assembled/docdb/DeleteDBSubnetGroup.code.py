def handler(store, request: dict):
    return store.delete_subnet_group(request["DBSubnetGroupName"])
