# spec:trace: aws/lightsail/update_load_balancer_attribute.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/update-load-balancer-attribute
# spec:generated: DO NOT EDIT — edit the spec instead

def update_load_balancer_attribute(store, request: dict) -> dict:
    """Updates the specified attribute for a load balancer. You can only update one attribute at a time. The update load balancer attribute operation supports tag-based access control via resource tags appli"""
    attribute_name = request.get("attributeName", "").strip() if isinstance(request.get("attributeName"), str) else request.get("attributeName")
    if not attribute_name:
        raise ValidationException("attributeName is required")
    attribute_value = request.get("attributeValue", "").strip() if isinstance(request.get("attributeValue"), str) else request.get("attributeValue")
    if not attribute_value:
        raise ValidationException("attributeValue is required")
    load_balancer_name = request.get("loadBalancerName", "").strip() if isinstance(request.get("loadBalancerName"), str) else request.get("loadBalancerName")
    if not load_balancer_name:
        raise ValidationException("loadBalancerName is required")

    resource = store.load_balancer_attributes(attribute_name)
    if not resource:
        raise ResourceNotFoundException("Resource attribute_name not found")

    # Update mutable fields

    store.load_balancer_attributes(attribute_name, resource)
    return resource

