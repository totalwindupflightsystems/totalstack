def list_tags_for_resource(store, request):
    return store.list_tags_for_resource(resourceArn=request['resourceArn'])
