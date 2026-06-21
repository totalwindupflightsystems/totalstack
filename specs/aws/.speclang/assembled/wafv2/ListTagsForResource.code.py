"""Handler for ListTagsForResource — AWS WAFv2."""
def handler(store, request):
    return store.list_tags_for_resource(request["ResourceARN"])
