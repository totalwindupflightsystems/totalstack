"""RemoveTagsFromResource handler for Neptune."""


def remove_tags_from_resource(store, request):
    """Remove metadata tags from a Neptune resource."""
    resource_name = request.get('ResourceName', '').strip()
    if not resource_name:
        raise InvalidParameterValueException("ResourceName is required")

    tag_keys = request.get('TagKeys', [])
    if not tag_keys:
        raise InvalidParameterValueException("TagKeys is required")

    resource = _find_resource_by_name(store, resource_name)
    if resource is None:
        raise DBClusterNotFoundFault(f"Resource {resource_name} not found")

    existing_tags = getattr(resource, 'tags', [])
    resource.tags = [t for t in existing_tags if t.get('Key') not in tag_keys]
    return {}
