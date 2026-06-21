# spec:trace: aws/lightsail/tag_resource.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/tag-resource
# spec:generated: DO NOT EDIT — edit the spec instead

def tag_resource(store, request: dict) -> dict:
    """Adds one or more tags to the specified Amazon Lightsail resource. Each resource can have a maximum of 50 tags. Each tag consists of a key and an optional value. Tag keys must be unique per resource. F"""
    resource_name = request.get("resourceName", "").strip() if isinstance(request.get("resourceName"), str) else request.get("resourceName")
    if not resource_name:
        raise ValidationException("resourceName is required")
    tags = request.get("tags", "").strip() if isinstance(request.get("tags"), str) else request.get("tags")
    if not tags:
        raise ValidationException("tags is required")

    # Tag/untag resource
    resource_arn = request.get("ResourceARN", request.get("ResourceName", ""))
    store.tag_resource(resource_arn, request.get("Tags", []))
    return {}

