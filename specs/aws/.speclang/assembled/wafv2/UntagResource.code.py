"""Handler for UntagResource — AWS WAFv2."""
def handler(store, request):
    return store.untag_resource(
        resource_arn=request["ResourceARN"],
        tag_keys=request["TagKeys"])
