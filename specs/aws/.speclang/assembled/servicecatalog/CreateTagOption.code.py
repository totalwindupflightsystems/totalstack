"""Handler for CreateTagOption — AWS Service Catalog."""
def execute_create_tag_option(store, request):
    key = request.get("Key")
    value = request.get("Value")
    if not key:
        raise InvalidParametersException("Key is required")
    if not value:
        raise InvalidParametersException("Value is required")
    result = store.create_tag_option(key, value)
    return {"TagOptionDetail": result}
