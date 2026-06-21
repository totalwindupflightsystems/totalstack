"""Handler for CreateProvisioningArtifact — AWS Service Catalog."""
def execute_create_provisioning_artifact(store, request):
    product_id = request.get("ProductId")
    name = request.get("Parameters", {}).get("Name", request.get("Name", ""))
    if not product_id:
        raise InvalidParametersException("ProductId is required")
    if not name:
        raise InvalidParametersException("Name is required")
    desc = request.get("Parameters", {}).get("Description", request.get("Description", ""))
    result = store.create_provisioning_artifact(product_id, name, desc)
    return {"ProvisioningArtifactDetail": result}
