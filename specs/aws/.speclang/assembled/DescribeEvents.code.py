
def describe_events(store, request):
    """Handle DescribeEvents — describe resources."""
    items = list(store.events)
    return {Events: items}
