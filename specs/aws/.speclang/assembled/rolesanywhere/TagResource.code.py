def handler(store, request):
    store.tag_resource(request["resourceArn"], request["tags"])
    return {}
