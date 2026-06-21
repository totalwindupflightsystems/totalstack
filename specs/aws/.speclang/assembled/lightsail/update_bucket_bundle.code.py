# spec:trace: aws/lightsail/update_bucket_bundle.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/update-bucket-bundle
# spec:generated: DO NOT EDIT — edit the spec instead

def update_bucket_bundle(store, request: dict) -> dict:
    """Updates the bundle, or storage plan, of an existing Amazon Lightsail bucket. A bucket bundle specifies the monthly cost, storage space, and data transfer quota for a bucket. You can update a bucket's """
    bucket_name = request.get("bucketName", "").strip() if isinstance(request.get("bucketName"), str) else request.get("bucketName")
    if not bucket_name:
        raise ValidationException("bucketName is required")
    bundle_id = request.get("bundleId", "").strip() if isinstance(request.get("bundleId"), str) else request.get("bundleId")
    if not bundle_id:
        raise ValidationException("bundleId is required")

    resource = store.bucket_bundles(bucket_name)
    if not resource:
        raise ResourceNotFoundException("Resource bucket_name not found")

    # Update mutable fields

    store.bucket_bundles(bucket_name, resource)
    return resource

