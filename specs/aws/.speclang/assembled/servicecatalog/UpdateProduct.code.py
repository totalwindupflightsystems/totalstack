"""Handler for UpdateProduct — AWS Service Catalog."""
def execute_update_product(store, request):
    product_id = request.get("Id")
    if not product_id:
        raise InvalidParametersException("Id is required")
    name = request.get("Name", "")
    owner = request.get("Owner", "")
    description = request.get("Description", "")
    result = store.update_product(product_id, name, owner, description)
    return {"ProductViewDetail": {"ProductViewSummary": result}}
