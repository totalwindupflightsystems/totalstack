"""Handler for ListProvisioningArtifacts — AWS Service Catalog."""
def execute_list_provisioning_artifacts(store, request):
    product_id = request.get("ProductId")
    if not product_id:
        raise InvalidParametersException("ProductId is required")
    result = store.list_provisioning_artifacts(product_id)
    return {"ProvisioningArtifactDetails": result}
