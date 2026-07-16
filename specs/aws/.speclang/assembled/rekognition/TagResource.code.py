# spec:trace: aws/rekognition/TagResource.spec.py.md#implementation
# spec:id: @specs/aws/rekognition/tagresource
# spec:generated: DO NOT EDIT — edit the spec instead

def execute_tag_resource(store, request):
    """Adds one or more key-value tags to an Amazon Rekognition collection, stream processor, or Custom Labels model. For more information, see Tagging AWS Resources. This operation requires permissions to perform the rekognition:TagResource action."""
    if not request.get("ResourceArn"):
        raise InvalidParameterException(f"{fname} is required")
    if not request.get("Tags"):
        raise InvalidParameterException(f"{fname} is required")
    resource_arn = request["ResourceArn"]
    tags = request["Tags"]
    if resource_arn not in store.tags:
        store.tags[resource_arn] = {}
    store.tags[resource_arn].update(tags)
    return {}

