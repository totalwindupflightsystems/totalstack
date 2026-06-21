"""Handler for GetWebACLForResource — AWS WAFv2."""
def handler(store, request):
    return store.get_web_acl_for_resource(request["ResourceArn"])
