"""DeleteDeploymentConfig handler for CodeDeploy."""


def delete_deployment_config(store, request):
    deployment_config_name = request.get('deploymentConfigName', '').strip()
    store.deployment_configs.delete_deployment_config(deployment_config_name)
    return {}
