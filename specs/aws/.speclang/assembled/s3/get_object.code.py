# spec:trace: aws/s3/get_object.spec.py.md#implementation
# spec:id: @specs/aws/s3/get-object
# spec:generated: DO NOT EDIT — edit the spec instead

def get_object(store, request: dict) -> dict:
    """Retrieve an object from S3."""
    bucket = request.get("Bucket", "").strip() if isinstance(request.get("Bucket"), str) else request.get("Bucket")
    if not bucket:
        raise Exception("Bucket is required")
    key = request.get("Key", "").strip() if isinstance(request.get("Key"), str) else request.get("Key")
    if not key:
        raise Exception("Key is required")

    result = store.get_object(bucket, key)
    return {"Bucket": bucket, **result}
