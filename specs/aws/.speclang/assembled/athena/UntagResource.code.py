# spec:trace: aws/athena/UntagResource.spec.py.md#implementation
# spec:id: @specs/aws/athena/untagresource
# spec:generated: DO NOT EDIT — edit the spec instead

def untag_resource(store: 'AthenaStore', request: dict) -> dict:
    """Untag an Athena resource."""
    arn = request.get('ResourceARN')
    keys = request.get('TagKeys', [])
    if not arn:
        raise InvalidRequestException('ResourceARN is required')
    if arn in store.tags:
        for k in keys:
            store.tags[arn].pop(k, None)
    return {}

