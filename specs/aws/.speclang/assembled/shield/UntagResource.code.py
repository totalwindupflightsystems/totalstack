def handler(store, request):
    resource_arn = request.get("ResourceARN")
    tag_keys = request.get("TagKeys")
    return store.untag_resource(resource_arn=resource_arn, tag_keys=tag_keys)
