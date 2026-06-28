def handler(store, request):
    store.untag_resource(request["resourceArn"], request["tagKeys"])
    return {}
