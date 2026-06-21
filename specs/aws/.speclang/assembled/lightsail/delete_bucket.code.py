# spec:trace: aws/lightsail/delete_bucket.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/delete-bucket
# spec:generated: DO NOT EDIT — edit the spec instead

def delete_bucket(store, request: dict) -> dict:
    """Deletes a Amazon Lightsail bucket. When you delete your bucket, the bucket name is released and can be reused for a new bucket in your account or another Amazon Web Services account."""
    bucket_name = request.get("bucketName", "").strip() if isinstance(request.get("bucketName"), str) else request.get("bucketName")

    if not store.buckets(bucket_name):
        raise ResourceNotFoundException("Resource bucket_name not found")
    store.delete_buckets(bucket_name)
    return {}

