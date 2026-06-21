"""CreateDeploymentConfig handler for CodeDeploy."""


def create_deployment_config(store, request):
    deployment_config_name = request.get('deploymentConfigName', '').strip()
    minimum_healthy_hosts = request.get('minimumHealthyHosts')
    compute_platform = request.get('computePlatform', 'Server')

    if minimum_healthy_hosts:
        mhh_type = minimum_healthy_hosts.get('type', '')
        if mhh_type not in ('HOST_COUNT', 'FLEET_PERCENT'):
            raise InvalidMinimumHealthyHostValueException(
                "minimumHealthyHosts.type must be HOST_COUNT or FLEET_PERCENT")
        value = minimum_healthy_hosts.get('value', 0)
        if mhh_type == 'FLEET_PERCENT' and (value < 1 or value > 99):
            raise InvalidMinimumHealthyHostValueException(
                "FLEET_PERCENT value must be between 1 and 99")
        if mhh_type == 'HOST_COUNT' and value < 0:
            raise InvalidMinimumHealthyHostValueException(
                "HOST_COUNT value must be non-negative")

    if compute_platform not in ('Server', 'Lambda', 'ECS'):
        raise InvalidComputePlatformException(
            f"Invalid computePlatform '{compute_platform}'")

    config = store.deployment_configs.create_deployment_config(
        deployment_config_name=deployment_config_name,
        minimum_healthy_hosts=minimum_healthy_hosts,
        compute_platform=compute_platform,
        trafficRoutingConfig=request.get('trafficRoutingConfig'),
        zonalConfig=request.get('zonalConfig'),
    )
    return {'deploymentConfigId': config.deploymentConfigId}
