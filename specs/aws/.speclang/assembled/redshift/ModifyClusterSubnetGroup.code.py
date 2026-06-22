def handler(store, request: dict) -> dict:
    record = store.modify_cluster_subnet_group(
        request["ClusterSubnetGroupName"],
        request["SubnetIds"],
        Description=request.get("Description"))
    return {"ClusterSubnetGroup": record.to_dict()}
