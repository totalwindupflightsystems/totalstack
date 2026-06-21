def handler(store, request: dict) -> dict:
    """DeleteDBSubnetGroup handler."""
    store.delete_db_subnet_group(
        db_subnet_group_name=request["DBSubnetGroupName"])
    return {}
