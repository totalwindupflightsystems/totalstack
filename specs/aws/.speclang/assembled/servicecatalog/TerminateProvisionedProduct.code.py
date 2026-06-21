"""Handler for TerminateProvisionedProduct — AWS Service Catalog."""
def execute_terminate_provisioned_product(store, request):
    provisioned_product_id = request.get("ProvisionedProductId", request.get("Id", ""))
    if not provisioned_product_id:
        raise InvalidParametersException("ProvisionedProductId is required")
    store.terminate_provisioned_product(provisioned_product_id)
    return {}
