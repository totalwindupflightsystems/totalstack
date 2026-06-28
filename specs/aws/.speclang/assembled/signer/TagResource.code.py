def handler(store, request):
    resourceArn = request["resourceArn"]
    tags = request["tags"]
    store.tag_resource(resourceArn, tags)
    return {}
