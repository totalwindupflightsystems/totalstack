"""Handler for ProvisionProduct — AWS Service Catalog."""
def execute_provision_product(store, request):
    product_id = request.get("ProductId")
    provisioned_product_name = request.get("ProvisionedProductName")
    provisioning_artifact_id = request.get("ProvisioningArtifactId")
    if not product_id:
        raise InvalidParametersException("ProductId is required")
    if not provisioned_product_name:
        raise InvalidParametersException("ProvisionedProductName is required")
    if not provisioning_artifact_id:
        raise InvalidParametersException("ProvisioningArtifactId is required")
    path_id = request.get("PathId", "")
    result = store.provision_product(product_id, provisioned_product_name,
                                     provisioning_artifact_id, path_id)
    return {"ProvisionedProductDetail": result}
