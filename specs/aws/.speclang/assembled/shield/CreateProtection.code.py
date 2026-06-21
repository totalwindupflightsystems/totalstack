def handler(store, request):
    name = request.get("Name")
    resource_arn = request.get("ResourceArn")
    tags = request.get("Tags")
    return store.create_protection(name=name, resource_arn=resource_arn, tags=tags)
