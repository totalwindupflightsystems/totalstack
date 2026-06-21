"""GetDeployment handler for CodeDeploy."""


def get_deployment(store, request):
    deployment_id = request.get('deploymentId', '').strip()
    deployment = store.deployments.get_deployment(deployment_id)
    return {'deploymentInfo': deployment.to_dict()}
