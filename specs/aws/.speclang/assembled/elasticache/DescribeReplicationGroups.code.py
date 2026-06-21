# spec:trace: aws/elasticache/DescribeReplicationGroups.spec.py.md#implementation
# spec:id: @specs/aws/elasticache/describereplicationgroups
# spec:generated: DO NOT EDIT — edit the spec instead

def describe_replication_groups(store, request):
    """Handle DescribeReplicationGroups — describe resources."""
    resource_name = request.get("ReplicationGroupId")
    if resource_name:
        if resource_name not in store.replication_groups:
            raise ReplicationGroupNotFoundFault(f"Resource {resource_name} not found")
        return {"ReplicationGroups": [dict(store.replication_groups[resource_name])]}
    else:
        items = [dict(v) for v in store.replication_groups.values()]
        return {"ReplicationGroups": items}

