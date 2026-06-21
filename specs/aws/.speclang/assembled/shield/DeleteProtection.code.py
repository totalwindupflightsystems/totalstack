def handler(store, request):
    protection_id = request.get("ProtectionId")
    return store.delete_protection(protection_id=protection_id)
