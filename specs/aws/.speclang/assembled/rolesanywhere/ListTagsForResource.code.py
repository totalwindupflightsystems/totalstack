def handler(store, request):
    tags = store.list_tags(request["resourceArn"])
    return {"tags": tags}
