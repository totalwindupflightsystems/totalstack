"""Handler for CreateProduct — AWS Service Catalog."""
def execute_create_product(store, request):
    name = request.get("Name")
    owner = request.get("Owner")
    product_type = request.get("ProductType")
    if not name:
        raise InvalidParametersException("Name is required")
    if not owner:
        raise InvalidParametersException("Owner is required")
    if not product_type:
        raise InvalidParametersException("ProductType is required")
    desc = request.get("Description", "")
    distributor = request.get("Distributor", "")
    support_desc = request.get("SupportDescription", "")
    support_email = request.get("SupportEmail", "")
    support_url = request.get("SupportUrl", "")
    result = store.create_product(name, owner, product_type, desc,
                                  distributor, support_desc, support_email, support_url)
    return {"ProductViewDetail": {"ProductViewSummary": result}}
