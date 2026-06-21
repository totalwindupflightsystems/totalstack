# spec:trace: aws/elasticache/ListTagsForResource.spec.py.md#implementation
# spec:id: @specs/aws/elasticache/listtagsforresource
# spec:generated: DO NOT EDIT — edit the spec instead

def list_tags_for_resource(store, request):
    """Handle ListTagsForResource."""
    resource_name = request.get("ResourceName")
    if not resource_name:
        raise InvalidParameterValueException("ResourceName is required")
    if resource_name not in store.tags:
        store.tags[resource_name] = []
    return {"TagList": store.tags[resource_name]}

