"""Handler for AssociateWebACL — AWS WAFv2."""
def handler(store, request):
    return store.associate_web_acl(
        web_acl_arn=request["WebACLArn"],
        resource_arn=request["ResourceArn"])
