# spec:trace: aws/lightsail/create_bucket_access_key.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/create-bucket-access-key
# spec:generated: DO NOT EDIT — edit the spec instead

def create_bucket_access_key(store, request: dict) -> dict:
    """Creates a new access key for the specified Amazon Lightsail bucket. Access keys consist of an access key ID and corresponding secret access key. Access keys grant full programmatic access to the speci"""
    bucket_name = request.get("bucketName", "").strip() if isinstance(request.get("bucketName"), str) else request.get("bucketName")
    if not bucket_name:
        raise ValidationException("bucketName is required")

    if store.bucket_access_keys(bucket_name):
        raise ResourceInUseException("Resource bucket_name already exists")

    record = {
        "bucketName": bucket_name,
    }

    store.bucket_access_keys(bucket_name, record)

    return {
        "accessKey": record.get("accessKey", {}),
        "operations": record.get("operations", {}),
    }

