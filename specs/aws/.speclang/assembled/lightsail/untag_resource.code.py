# spec:trace: aws/lightsail/untag_resource.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/untag-resource
# spec:generated: DO NOT EDIT — edit the spec instead

def untag_resource(store, request: dict) -> dict:
    """Deletes the specified set of tag keys and their values from the specified Amazon Lightsail resource. The untag resource operation supports tag-based access control via request tags and resource tags a"""
    resource_name = request.get("resourceName", "").strip() if isinstance(request.get("resourceName"), str) else request.get("resourceName")
    if not resource_name:
        raise ValidationException("resourceName is required")
    tag_keys = request.get("tagKeys", "").strip() if isinstance(request.get("tagKeys"), str) else request.get("tagKeys")
    if not tag_keys:
        raise ValidationException("tagKeys is required")

    # Tag/untag resource
    resource_arn = request.get("ResourceARN", request.get("ResourceName", ""))
    store.tag_resource(resource_arn, request.get("Tags", []))
    return {}

