def handler(store, request: dict) -> dict:
    return store.delete_subnet_group(request["DBSubnetGroupName"])
