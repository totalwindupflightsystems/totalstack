def handler(store, request: dict) -> dict:
    sn = request.get("SubnetGroupName")
    return store.describe_subnet_groups(SubnetGroupName=sn)

