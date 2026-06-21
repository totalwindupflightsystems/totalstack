"""Handler for DisassociateWebACL — AWS WAFv2."""
def handler(store, request):
    return store.disassociate_web_acl(request["ResourceArn"])
