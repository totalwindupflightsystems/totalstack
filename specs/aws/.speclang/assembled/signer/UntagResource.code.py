def handler(store, request):
    resourceArn = request["resourceArn"]
    tagKeys = request["tagKeys"]
    store.untag_resource(resourceArn, tagKeys)
    return {}
