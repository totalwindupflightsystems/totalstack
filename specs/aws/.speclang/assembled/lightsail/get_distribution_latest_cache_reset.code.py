# spec:trace: aws/lightsail/get_distribution_latest_cache_reset.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-distribution-latest-cache-reset
# spec:generated: DO NOT EDIT — edit the spec instead

def get_distribution_latest_cache_reset(store, request: dict) -> dict:
    """Returns the timestamp and status of the last cache reset of a specific Amazon Lightsail content delivery network (CDN) distribution."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)

