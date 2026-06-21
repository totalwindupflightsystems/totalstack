"""DescribeDBClusters handler for Neptune."""


def describe_db_clusters(store, request):
    """Describe Neptune DB clusters."""
    identifier = request.get('DBClusterIdentifier', '').strip() or None
    max_records = request.get('MaxRecords', 100)

    clusters = store.list_clusters(
        db_cluster_identifier=identifier,
        max_records=max_records,
    )
    return {
        'DBClusters': [c.to_dict() for c in clusters],
    }
