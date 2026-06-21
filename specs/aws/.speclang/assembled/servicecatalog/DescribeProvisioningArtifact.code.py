"""Handler for DescribeProvisioningArtifact — AWS Service Catalog."""
def execute_describe_provisioning_artifact(store, request):
    product_id = request.get("ProductId", "")
    provisioning_artifact_id = request.get("ProvisioningArtifactId")
    if not provisioning_artifact_id:
        raise InvalidParametersException("ProvisioningArtifactId is required")
    result = store.get_provisioning_artifact(product_id, provisioning_artifact_id)
    return {"ProvisioningArtifactDetail": result}
