"""DeleteDBCluster handler for Neptune."""


def delete_db_cluster(store, request):
    """Delete a Neptune DB cluster."""
    identifier = request.get('DBClusterIdentifier', '').strip()
    if not identifier:
        raise InvalidParameterValueException("DBClusterIdentifier is required")

    skip_final = request.get('SkipFinalSnapshot', False)
    final_snapshot_id = request.get('FinalDBSnapshotIdentifier', '')

    cluster = store.delete_cluster(
        identifier,
        skip_final_snapshot=skip_final,
        final_db_snapshot_identifier=final_snapshot_id,
    )
    return {'DBCluster': cluster.to_dict()}
