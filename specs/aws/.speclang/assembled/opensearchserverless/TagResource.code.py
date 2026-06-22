def tag_resource(store, request):
    return store.tag_resource(
        resourceArn=request["resourceArn"],
        tags=request.get("tags", []))
