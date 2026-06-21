# spec:trace: aws/s3/create_bucket.spec.py.md#implementation
# spec:id: @specs/aws/s3/create-bucket
# spec:generated: DO NOT EDIT — edit the spec instead

def create_bucket(store, request: dict) -> dict:
    """Create an S3 bucket."""
    bucket = request.get("Bucket", "").strip() if isinstance(request.get("Bucket"), str) else request.get("Bucket")
    if not bucket:
        raise Exception("Bucket is required")

    if store.buckets(bucket):
        raise BucketAlreadyOwnedByYou(f"Bucket {bucket} already exists")

    store.create_bucket(bucket, request)

    return {}

