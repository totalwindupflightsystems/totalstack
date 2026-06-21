# spec:trace: aws/lightsail/get_bucket_bundles.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-bucket-bundles
# spec:generated: DO NOT EDIT — edit the spec instead

def get_bucket_bundles(store, request: dict) -> dict:
    """Returns the bundles that you can apply to a Amazon Lightsail bucket. The bucket bundle specifies the monthly cost, storage quota, and data transfer quota for a bucket. Use the UpdateBucketBundle actio"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)

