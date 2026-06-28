def handler(store, request):
    resourceArn = request["resourceArn"]
    tags = store.list_tags(resourceArn)
    return {"tags": tags}
