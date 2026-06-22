def handler(store, request: dict):
    return store.modify_subnet_group(request["DBSubnetGroupName"], **{k: v for k, v in request.items() if k != "DBSubnetGroupName"})
