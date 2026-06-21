# spec:trace: aws/rekognition/ListTagsForResource.spec.py.md#implementation
# spec:id: @specs/aws/rekognition/listtagsforresource
# spec:generated: DO NOT EDIT — edit the spec instead

@dataclass
def execute_list_tags_for_resource(store, request):
    """Returns a list of tags in an Amazon Rekognition collection, stream processor, or Custom Labels model. This operation requires permissions to perform the rekognition:ListTagsForResource action."""
    if not request.get("ResourceArn"):
        raise InvalidParameterException(f"{fname} is required")
    resource_arn = request["ResourceArn"]
    tags = store.tags.get(resource_arn, {})
    return {"Tags": tags}

