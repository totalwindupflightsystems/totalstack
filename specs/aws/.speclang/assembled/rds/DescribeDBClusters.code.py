def handler(store, request: dict) -> dict:
    """DescribeDBClusters handler."""
    result = store.describe_db_clusters(
        db_cluster_identifier=request.get("DBClusterIdentifier"))
    if isinstance(result, list):
        return {"DBClusters": result}
    return {"DBClusters": [result]}
