def untag_resource(store, request):
    return store.untag_resource(resourceArn=request['resourceArn'], tagKeys=request['tagKeys'])
