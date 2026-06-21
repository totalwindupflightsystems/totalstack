# spec:trace: aws/mediaconvert/TagOperations.spec.py.md#implementation
# spec:id: @specs/aws/mediaconvert/tagoperations
# spec:generated: DO NOT EDIT — edit the spec instead

def execute_tag_resource(store, request):
    """Add tags to a resource."""
    arn = request.get('Arn')
    tags = request.get('Tags', {})
    
    if not arn:
        raise InvalidParameterException("Arn is required")
    if not tags:
        raise InvalidParameterException("Tags is required")
    
    current_tags = store.tags.get(arn, {})
    current_tags.update(tags)
    store.tags[arn] = current_tags
    
    return {}


def execute_untag_resource(store, request):
    """Remove tags from a resource."""
    arn = request.get('Arn')
    tag_keys = request.get('TagKeys', [])
    
    if not arn:
        raise InvalidParameterException("Arn is required")
    
    current_tags = store.tags.get(arn, {})
    for key in tag_keys:
        current_tags.pop(key, None)
    
    if current_tags:
        store.tags[arn] = current_tags
    elif arn in store.tags:
        del store.tags[arn]
    
    return {}


def execute_list_tags_for_resource(store, request):
    """List tags for a resource."""
    arn = request.get('Arn')
    if not arn:
        raise InvalidParameterException("Arn is required")
    
    tags = store.tags.get(arn, {})
    return {"ResourceTags": {"Arn": arn, "Tags": tags}}

