# spec:trace: aws/lightsail/get_buckets.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-buckets
# spec:generated: DO NOT EDIT — edit the spec instead

def get_buckets(store, request: dict) -> dict:
    """Returns information about one or more Amazon Lightsail buckets. The information returned includes the synchronization status of the Amazon Simple Storage Service (Amazon S3) account-level block public"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)

