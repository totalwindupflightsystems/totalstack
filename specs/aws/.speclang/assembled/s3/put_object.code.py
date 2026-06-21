# spec:trace: aws/s3/put_object.spec.py.md#implementation
# spec:id: @specs/aws/s3/put-object
# spec:generated: DO NOT EDIT — edit the spec instead

def put_object(store, request: dict) -> dict:
    """Put an object in an S3 bucket."""
    bucket = request.get("Bucket", "").strip() if isinstance(request.get("Bucket"), str) else request.get("Bucket")
    if not bucket:
        raise Exception("Bucket is required")
    key = request.get("Key", "").strip() if isinstance(request.get("Key"), str) else request.get("Key")
    if not key:
        raise Exception("Key is required")

    body = request.get("Body", b"")
    metadata = request.get("Metadata")
    result = store.put_object(bucket, key, body, metadata)
    return result
