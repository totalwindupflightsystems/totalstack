// spec:trace spec=/home/kara/totalstack/specs/aws/elasticache/RemoveTagsFromResource.spec.py.md#input-shape-removetagsfromresourcemessage
// spec:generated DO NOT EDIT — edit the spec instead

def remove_tags_from_resource(store, request):
    """Handle RemoveTagsFromResource."""
    resource_name = request.get("ResourceName")
    if not resource_name:
        raise InvalidParameterValueException("ResourceName is required")
    if resource_name not in store.tags:
        store.tags[resource_name] = []
    tag_keys = request.get("TagKeys", [])
    if not tag_keys:
        raise InvalidParameterValueException("TagKeys is required")
    store.tags[resource_name] = [
        t for t in store.tags[resource_name]
        if t.get("Key") not in tag_keys
    ]
    return {}