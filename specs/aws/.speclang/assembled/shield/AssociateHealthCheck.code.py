def handler(store, request):
    protection_id = request.get("ProtectionId")
    health_check_arn = request.get("HealthCheckArn")
    return store.associate_health_check(protection_id=protection_id, health_check_arn=health_check_arn)
