def handler(store, request: dict):
    return store.create_subnet_group(request["DBSubnetGroupName"], request["DBSubnetGroupDescription"], request["SubnetIds"])
