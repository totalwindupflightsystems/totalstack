"""Handler for UpdateProvisionedProduct — AWS Service Catalog."""
def execute_update_provisioned_product(store, request):
    provisioned_product_id = request.get("ProvisionedProductId")
    if not provisioned_product_id:
        raise InvalidParametersException("ProvisionedProductId is required")
    product_id = request.get("ProductId", "")
    provisioning_artifact_id = request.get("ProvisioningArtifactId", "")
    path_id = request.get("PathId", "")
    result = store.update_provisioned_product(provisioned_product_id, product_id,
                                             provisioning_artifact_id, path_id)
    return {"ProvisionedProductDetail": result}
