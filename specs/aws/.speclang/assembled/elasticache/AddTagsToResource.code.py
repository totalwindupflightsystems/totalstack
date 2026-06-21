# spec:trace: aws/elasticache/AddTagsToResource.spec.py.md#implementation
# spec:id: @specs/aws/elasticache/addtagstoresource
# spec:generated: DO NOT EDIT — edit the spec instead

def add_tags_to_resource(store, request):
    """Handle AddTagsToResource."""
    resource_name = request.get("ResourceName")
    if not resource_name:
        raise InvalidParameterValueException("ResourceName is required")
    if resource_name not in store.tags:
        store.tags[resource_name] = []
    tags = request.get("Tags", [])
    if not tags:
        raise InvalidParameterValueException("Tags is required")
    for tag in tags:
        store.tags[resource_name].append(tag)
    return {}

