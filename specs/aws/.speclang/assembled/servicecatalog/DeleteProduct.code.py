"""Handler for DeleteProduct — AWS Service Catalog."""
def execute_delete_product(store, request):
    product_id = request.get("Id")
    if not product_id:
        raise InvalidParametersException("Id is required")
    store.delete_product(product_id)
    return {}
