def handler(store, request):
    resource_arn = request.get("ResourceARN")
    tags = request.get("Tags")
    return store.tag_resource(resource_arn=resource_arn, tags=tags)
