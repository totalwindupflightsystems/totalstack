def handler(store, request: dict) -> dict:
    record = store.create_cluster_subnet_group(
        request["ClusterSubnetGroupName"],
        request["Description"],
        request["SubnetIds"],
        Tags=request.get("Tags"))
    return {"ClusterSubnetGroup": record.to_dict()}
