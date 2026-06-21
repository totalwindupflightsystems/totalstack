"""DeleteDBClusterSnapshot handler for Neptune."""


def delete_db_cluster_snapshot(store, request):
    """Delete a DB cluster snapshot."""
    snapshot_id = request.get('DBClusterSnapshotIdentifier', '').strip()
    if not snapshot_id:
        raise InvalidParameterValueException("DBClusterSnapshotIdentifier is required")

    snap = store.delete_snapshot(snapshot_id)
    return {'DBClusterSnapshot': snap.to_dict()}
