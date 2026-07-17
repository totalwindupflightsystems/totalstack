"""RemoveTagsFromResource handler for Neptune."""


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


def remove_tags_from_resource(store, request):
    """Remove tags from a Neptune resource."""
    resource_name = request.get('ResourceName', '').strip()
    if not resource_name:
        raise InvalidParameterValueException("ResourceName is required")

    tag_keys = request.get('TagKeys', [])
    if not tag_keys:
        raise InvalidParameterValueException("TagKeys is required")

    resource = find_resource_by_name(store, resource_name)
    if resource is None:
        raise DBClusterNotFoundFault(f"Resource {resource_name} not found")

    tags = getattr(resource, 'tags', [])
    setattr(resource, 'tags', [t for t in tags if t.get('Key') not in tag_keys])
    return {}
