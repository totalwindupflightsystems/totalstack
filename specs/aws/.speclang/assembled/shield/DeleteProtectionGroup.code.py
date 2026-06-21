def handler(store, request):
    protection_group_id = request.get("ProtectionGroupId")
    return store.delete_protection_group(protection_group_id=protection_group_id)
