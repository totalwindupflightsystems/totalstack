def handler(store, request: dict) -> dict:
    return store.describe_cluster_subnet_groups(
        ClusterSubnetGroupName=request.get("ClusterSubnetGroupName"))
