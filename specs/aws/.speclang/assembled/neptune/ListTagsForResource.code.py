"""ListTagsForResource handler for Neptune."""


def list_tags_for_resource(store, request):
    """List all tags on a Neptune resource."""
    resource_name = request.get('ResourceName', '').strip()
    if not resource_name:
        raise InvalidParameterValueException("ResourceName is required")

    resource = _find_resource_by_name(store, resource_name)
    if resource is None:
        raise DBClusterNotFoundFault(f"Resource {resource_name} not found")

    return {'TagList': getattr(resource, 'tags', [])}
