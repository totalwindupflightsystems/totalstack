def handler(store, request: dict) -> dict:
    record = store.delete_cluster(
        request["ClusterIdentifier"],
        SkipFinalClusterSnapshot=request.get("SkipFinalClusterSnapshot"),
        FinalClusterSnapshotIdentifier=request.get("FinalClusterSnapshotIdentifier"),
        FinalClusterSnapshotRetentionPeriod=request.get("FinalClusterSnapshotRetentionPeriod"))
    return {"Cluster": record.to_dict()}
