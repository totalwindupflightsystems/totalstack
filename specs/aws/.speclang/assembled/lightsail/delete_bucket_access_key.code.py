# spec:trace: aws/lightsail/delete_bucket_access_key.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/delete-bucket-access-key
# spec:generated: DO NOT EDIT — edit the spec instead

def delete_bucket_access_key(store, request: dict) -> dict:
    """Deletes an access key for the specified Amazon Lightsail bucket. We recommend that you delete an access key if the secret access key is compromised. For more information about access keys, see Creatin"""
    request.get("accessKeyId", "").strip() if isinstance(request.get("accessKeyId"), str) else request.get("accessKeyId")
    bucket_name = request.get("bucketName", "").strip() if isinstance(request.get("bucketName"), str) else request.get("bucketName")

    if not store.bucket_access_keys(bucket_name):
        raise ResourceNotFoundException("Resource bucket_name not found")
    store.delete_bucket_access_keys(bucket_name)
    return {}

