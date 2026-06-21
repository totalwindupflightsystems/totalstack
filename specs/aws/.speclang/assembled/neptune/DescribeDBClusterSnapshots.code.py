"""DescribeDBClusterSnapshots handler for Neptune."""


def describe_db_cluster_snapshots(store, request):
    """Describe DB cluster snapshots."""
    cluster_id = request.get('DBClusterIdentifier', '').strip() or None
    snapshot_id = request.get('DBClusterSnapshotIdentifier', '').strip() or None
    snapshot_type = request.get('SnapshotType', '').strip() or None
    max_records = request.get('MaxRecords', 100)

    if snapshot_id:
        snap = store.get_snapshot(snapshot_id)
        return {'DBClusterSnapshots': [snap.to_dict()]}

    snaps = store.list_snapshots(
        db_cluster_identifier=cluster_id,
        snapshot_type=snapshot_type,
        max_records=max_records,
    )
    return {'DBClusterSnapshots': [s.to_dict() for s in snaps]}
