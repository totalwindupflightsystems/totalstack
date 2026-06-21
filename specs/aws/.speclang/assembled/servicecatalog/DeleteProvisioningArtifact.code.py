"""Handler for DeleteProvisioningArtifact — AWS Service Catalog."""
def execute_delete_provisioning_artifact(store, request):
    product_id = request.get("ProductId", "")
    provisioning_artifact_id = request.get("ProvisioningArtifactId")
    if not provisioning_artifact_id:
        raise InvalidParametersException("ProvisioningArtifactId is required")
    store.delete_provisioning_artifact(product_id, provisioning_artifact_id)
    return {}
