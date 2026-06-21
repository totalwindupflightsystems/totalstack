def handler(store, request):
    role_arn = request.get("RoleArn")
    return store.associate_drt_role(role_arn=role_arn)
