def handler(store, request):
    protection_group_id = request.get("ProtectionGroupId")
    next_token = request.get("NextToken")
    max_results = request.get("MaxResults")
    return store.list_resources_in_protection_group(protection_group_id=protection_group_id, next_token=next_token, max_results=max_results)
