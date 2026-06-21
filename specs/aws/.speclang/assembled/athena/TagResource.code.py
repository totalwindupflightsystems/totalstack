# spec:trace: aws/athena/TagResource.spec.py.md#implementation
# spec:id: @specs/aws/athena/tagresource
# spec:generated: DO NOT EDIT — edit the spec instead

def tag_resource(store: 'AthenaStore', request: dict) -> dict:
    """Tag an Athena resource."""
    arn = request.get('ResourceARN')
    tags = request.get('Tags', [])
    if not arn:
        raise InvalidRequestException('ResourceARN is required')
    if arn not in store.tags:
        store.tags[arn] = {}
    for t in tags:
        store.tags[arn][t['Key']] = t['Value']
    return {}

