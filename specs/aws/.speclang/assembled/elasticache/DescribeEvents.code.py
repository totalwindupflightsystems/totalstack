# spec:trace: aws/elasticache/DescribeEvents.spec.py.md#implementation
# spec:id: @specs/aws/elasticache/describeevents
# spec:generated: DO NOT EDIT — edit the spec instead

def describe_events(store, request):
    """Handle DescribeEvents — describe resources."""
    items = list(store.events)
    return {"Events": items}

