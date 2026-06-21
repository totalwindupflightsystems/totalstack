"""ListDeploymentConfigs handler for CodeDeploy."""


def list_deployment_configs(store, request):
    next_token = request.get('nextToken')
    names, _ = store.deployment_configs.list_deployment_configs(next_token=next_token)
    return {'deploymentConfigsList': names}
