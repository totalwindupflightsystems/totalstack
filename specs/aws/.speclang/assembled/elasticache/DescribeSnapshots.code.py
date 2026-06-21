# spec:trace: aws/elasticache/DescribeSnapshots.spec.py.md#implementation
# spec:id: @specs/aws/elasticache/describesnapshots
# spec:generated: DO NOT EDIT — edit the spec instead

def describe_snapshots(store, request):
    """Handle DescribeSnapshots — describe resources."""
    resource_name = request.get("SnapshotName")
    if resource_name:
        if resource_name not in store.snapshots:
            raise SnapshotNotFoundFault(f"Resource {resource_name} not found")
        return {"Snapshots": [dict(store.snapshots[resource_name])]}
    else:
        items = [dict(v) for v in store.snapshots.values()]
        return {"Snapshots": items}

