# spec:trace: aws/lightsail/set_resource_access_for_bucket.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/set-resource-access-for-bucket
# spec:generated: DO NOT EDIT — edit the spec instead

def set_resource_access_for_bucket(store, request: dict) -> dict:
    """Sets the Amazon Lightsail resources that can access the specified Lightsail bucket. Lightsail buckets currently support setting access for Lightsail instances in the same Amazon Web Services Region."""
    access = request.get("access", "").strip() if isinstance(request.get("access"), str) else request.get("access")
    if not access:
        raise ValidationException("access is required")
    bucket_name = request.get("bucketName", "").strip() if isinstance(request.get("bucketName"), str) else request.get("bucketName")
    if not bucket_name:
        raise ValidationException("bucketName is required")
    resource_name = request.get("resourceName", "").strip() if isinstance(request.get("resourceName"), str) else request.get("resourceName")
    if not resource_name:
        raise ValidationException("resourceName is required")

    resource = store.set_resource_access_for_buckets(resource_name)
    if not resource:
        raise ResourceNotFoundException("Resource resource_name not found")

    # Update mutable fields

    store.set_resource_access_for_buckets(resource_name, resource)
    return resource

