"""BatchGetDeployments handler for CodeDeploy."""


def batch_get_deployments(store, request):
    deployment_ids = request.get('deploymentIds', [])
    if not deployment_ids:
        raise InvalidInputException("deploymentIds is required")

    deployments = store.deployments.batch_get_deployments(deployment_ids)
    return {'deploymentsInfo': [d.to_dict() for d in deployments]}
