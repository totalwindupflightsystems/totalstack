"""AddTagsToResource handler for Neptune."""


def add_tags_to_resource(store, request):
    """Add metadata tags to a Neptune resource."""
    resource_name = request.get('ResourceName', '').strip()
    if not resource_name:
        raise InvalidParameterValueException("ResourceName is required")

    tags = request.get('Tags', [])
    if not tags:
        raise InvalidParameterValueException("Tags is required")

    # Find resource by ARN or identifier match
    resource = _find_resource_by_name(store, resource_name)
    if resource is None:
        raise DBClusterNotFoundFault(f"Resource {resource_name} not found")

    existing_tags = getattr(resource, 'tags', [])
    for tag in tags:
        key = tag.get('Key', '')
        value = tag.get('Value', '')
        existing_tags = [t for t in existing_tags if t.get('Key') != key]
        existing_tags.append({'Key': key, 'Value': value})
    resource.tags = existing_tags
    return {}


def _find_resource_by_name(store, resource_name):
    """Find a resource by ARN or identifier."""
    lower_name = resource_name.lower()
    # Check clusters
    for k, v in store.db_clusters.items():
        if lower_name in (k, resource_name):
            return v
    # Check instances
    for k, v in store.db_instances.items():
        if lower_name in (k, resource_name):
            return v
    # Check snapshots
    for k, v in store.db_cluster_snapshots.items():
        if lower_name in (k, resource_name):
            return v
    # Check subnet groups
    for k, v in store.db_subnet_groups.items():
        if lower_name in (k, resource_name):
            return v
    # Check param groups
    for k, v in store.db_cluster_parameter_groups.items():
        if lower_name in (k, resource_name):
            return v
    for k, v in store.db_parameter_groups.items():
        if lower_name in (k, resource_name):
            return v
    return None
