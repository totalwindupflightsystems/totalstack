# spec:trace: aws/s3/list_buckets.spec.py.md#implementation
# spec:id: @specs/aws/s3/list-buckets
# spec:generated: DO NOT EDIT — edit the spec instead

def list_buckets(store, request: dict) -> dict:
    """List all buckets."""
    items = store.list_buckets()
    return {"Buckets": [{'Name': b['Name']} for b in items]}

