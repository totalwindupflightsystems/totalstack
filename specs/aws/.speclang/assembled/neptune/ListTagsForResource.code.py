"""ListTagsForResource handler for Neptune."""


def _find_resource_by_name(store, resource_name):
    """Find a Neptune resource by name/ARN."""
    lower = resource_name.lower()
    for v in store.db_clusters.values():
        if lower in (v.db_cluster_identifier, getattr(v, 'db_cluster_arn', '')):
            return v
    for v in store.db_instances.values():
        if lower in (v.db_instance_identifier, getattr(v, 'db_instance_arn', '')):
            return v
    return None


def list_tags_for_resource(store, request):
    """List all tags on a Neptune resource."""
    resource_name = request.get('ResourceName', '').strip()
    if not resource_name:
        raise InvalidParameterValueException("ResourceName is required")

    resource = find_resource_by_name(store, resource_name)
    if resource is None:
        raise DBClusterNotFoundFault(f"Resource {resource_name} not found")

    return {'TagList': getattr(resource, 'tags', [])}
