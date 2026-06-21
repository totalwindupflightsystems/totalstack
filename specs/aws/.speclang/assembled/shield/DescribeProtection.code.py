def handler(store, request):
    protection_id = request.get("ProtectionId")
    resource_arn = request.get("ResourceArn")
    return store.describe_protection(protection_id=protection_id, resource_arn=resource_arn)
