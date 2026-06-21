"""Handler for DescribeProvisionedProduct — AWS Service Catalog."""
def execute_describe_provisioned_product(store, request):
    provisioned_product_id = request.get("Id", request.get("ProvisionedProductId", ""))
    if not provisioned_product_id:
        raise InvalidParametersException("ProvisionedProductId is required")
    result = store.get_provisioned_product(provisioned_product_id)
    return {"ProvisionedProductDetail": result}
