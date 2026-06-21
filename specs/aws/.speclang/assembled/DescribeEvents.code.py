// spec:trace spec=/home/kara/totalstack/specs/aws/elasticache/DescribeEvents.spec.py.md#input-shape-describeeventsmessage
// spec:generated DO NOT EDIT — edit the spec instead

def describe_events(store, request):
    """Handle DescribeEvents — describe resources."""
    items = list(store.events)
    return {Events: items}