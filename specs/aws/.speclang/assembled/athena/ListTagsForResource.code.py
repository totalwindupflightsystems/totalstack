# spec:trace: aws/athena/ListTagsForResource.spec.py.md#implementation
# spec:id: @specs/aws/athena/listtagsforresource
# spec:generated: DO NOT EDIT — edit the spec instead

def list_tags_for_resource(store: 'AthenaStore', request: dict) -> dict:
    """List tags for an Athena resource."""
    arn = request.get('ResourceARN')
    if not arn:
        raise InvalidRequestException('ResourceARN is required')
    tags = store.tags.get(arn, {})
    return {'Tags': [{'Key': k, 'Value': v} for k, v in tags.items()]}

