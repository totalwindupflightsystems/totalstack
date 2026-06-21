"""Handler for TagResource — AWS WAFv2."""
def handler(store, request):
    return store.tag_resource(
        resource_arn=request["ResourceARN"],
        tags=request["Tags"])
