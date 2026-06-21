# spec:trace: aws/lightsail/create_bucket.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/create-bucket
# spec:generated: DO NOT EDIT — edit the spec instead

def create_bucket(store, request: dict) -> dict:
    """Creates an Amazon Lightsail bucket. A bucket is a cloud storage resource available in the Lightsail object storage service. Use buckets to store objects such as data and its descriptive metadata. For """
    bucket_name = request.get("bucketName", "").strip() if isinstance(request.get("bucketName"), str) else request.get("bucketName")
    if not bucket_name:
        raise ValidationException("bucketName is required")
    bundle_id = request.get("bundleId", "").strip() if isinstance(request.get("bundleId"), str) else request.get("bundleId")
    if not bundle_id:
        raise ValidationException("bundleId is required")

    if store.buckets(bucket_name):
        raise ResourceInUseException("Resource bucket_name already exists")

    tags = request.get("tags", [])
    enable_object_versioning = request.get("enableObjectVersioning", False)

    record = {
        "bucketName": bucket_name,
        "bundleId": bundle_id,
        "tags": tags,
        "enableObjectVersioning": enable_object_versioning,
    }

    store.buckets(bucket_name, record)

    return {
        "bucket": record.get("bucket", {}),
        "operations": record.get("operations", {}),
    }

