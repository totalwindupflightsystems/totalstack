def handler(store, request):
    resource_arn = request.get("ResourceARN")
    return store.list_tags_for_resource(resource_arn=resource_arn)
