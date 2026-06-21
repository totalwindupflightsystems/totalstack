"""GetDeploymentConfig handler for CodeDeploy."""


def get_deployment_config(store, request):
    deployment_config_name = request.get('deploymentConfigName', '').strip()
    config = store.deployment_configs.get_deployment_config(deployment_config_name)
    return {'deploymentConfigInfo': config.to_dict()}
