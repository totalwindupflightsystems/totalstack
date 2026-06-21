"""Handler for ListTagOptions — AWS Service Catalog."""
def execute_list_tag_options(store, request):
    result = store.list_tag_options()
    return {"TagOptionDetails": result}
