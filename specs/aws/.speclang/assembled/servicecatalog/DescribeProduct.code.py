"""Handler for DescribeProduct — AWS Service Catalog."""
def execute_describe_product(store, request):
    product_id = request.get("Id")
    if not product_id:
        raise InvalidParametersException("Id is required")
    result = store.get_product(product_id)
    return {"ProductViewDetail": {"ProductViewSummary": result}}
