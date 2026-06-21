def handler(store, request):
    protection_group_id = request.get("ProtectionGroupId")
    aggregation = request.get("Aggregation")
    pattern = request.get("Pattern")
    resource_type = request.get("ResourceType")
    members = request.get("Members")
    tags = request.get("Tags")
    return store.create_protection_group(protection_group_id=protection_group_id, aggregation=aggregation, pattern=pattern, resource_type=resource_type, members=members, tags=tags)
