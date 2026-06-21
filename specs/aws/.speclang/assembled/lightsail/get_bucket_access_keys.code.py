# spec:trace: aws/lightsail/get_bucket_access_keys.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-bucket-access-keys
# spec:generated: DO NOT EDIT — edit the spec instead

def get_bucket_access_keys(store, request: dict) -> dict:
    """Returns the existing access key IDs for the specified Amazon Lightsail bucket. This action does not return the secret access key value of an access key. You can get a secret access key only when you c"""
    bucket_name = request.get("bucketName", "").strip() if isinstance(request.get("bucketName"), str) else request.get("bucketName")
    if not bucket_name:
        raise ValidationException("bucketName is required")

    resource = store.bucket_access_keyss(bucket_name)
    if not resource:
        raise ResourceNotFoundException("Resource bucket_name not found")
    return {"bucketName": bucket_name, **resource}

