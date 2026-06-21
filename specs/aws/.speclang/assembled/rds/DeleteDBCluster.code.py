def handler(store, request: dict) -> dict:
    """DeleteDBCluster handler."""
    return store.delete_db_cluster(
        db_cluster_identifier=request["DBClusterIdentifier"],
        skip_final_snapshot=request.get("SkipFinalSnapshot", False),
        final_db_snapshot_identifier=request.get("FinalDBSnapshotIdentifier"))
