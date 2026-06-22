
def execute_untag_resource(store, request):
    """Removes one or more tags from an Amazon Rekognition collection, stream processor, or Custom Labels model. This operation requires permissions to perform the rekognition:UntagResource action."""
    if not request.get("ResourceArn"):
        raise InvalidParameterException(f"{fname} is required")
    if not request.get("TagKeys"):
        raise InvalidParameterException(f"{fname} is required")
    resource_arn = request["ResourceArn"]
    tag_keys = request["TagKeys"]
    if resource_arn in store.tags:
        for key in tag_keys:
            store.tags[resource_arn].pop(key, None)
    return {}
