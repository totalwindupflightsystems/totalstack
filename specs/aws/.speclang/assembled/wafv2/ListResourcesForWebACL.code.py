"""Handler for ListResourcesForWebACL — AWS WAFv2."""
def handler(store, request):
    return store.list_resources_for_web_acl(request["WebACLArn"])
