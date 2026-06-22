def handler(store, request: dict) -> dict:
    return store.describe_clusters(
        ClusterIdentifier=request.get("ClusterIdentifier"),
        Marker=request.get("Marker"),
        MaxRecords=request.get("MaxRecords"))
