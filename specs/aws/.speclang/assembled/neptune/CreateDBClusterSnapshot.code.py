"""CreateDBClusterSnapshot handler for Neptune."""


def create_db_cluster_snapshot(store, request):
    """Create a snapshot of a DB cluster."""
    snapshot_id = request.get('DBClusterSnapshotIdentifier', '').strip()
    if not snapshot_id:
        raise InvalidParameterValueException("DBClusterSnapshotIdentifier is required")

    cluster_id = request.get('DBClusterIdentifier', '').strip()
    if not cluster_id:
        raise InvalidParameterValueException("DBClusterIdentifier is required")

    # Verify cluster exists
    cluster = store.get_cluster(cluster_id)

    snap = store.create_snapshot(
        snapshot_id,
        cluster_id,
        engine=cluster.engine,
        engine_version=cluster.engine_version,
        storage_encrypted=cluster.storage_encrypted,
        kms_key_id=cluster.kms_key_id,
        tags=request.get('Tags', []),
        status='available',
    )
    return {'DBClusterSnapshot': snap.to_dict()}
