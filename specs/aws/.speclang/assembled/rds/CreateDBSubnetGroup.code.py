def handler(store, request: dict) -> dict:
    """CreateDBSubnetGroup handler."""
    return store.create_db_subnet_group(
        db_subnet_group_name=request["DBSubnetGroupName"],
        db_subnet_group_description=request["DBSubnetGroupDescription"],
        subnet_ids=request["SubnetIds"],
        tags=request.get("Tags"))
