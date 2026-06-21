"""UpdateDeploymentGroup handler for CodeDeploy."""


def update_deployment_group(store, request):
    application_name = request.get('applicationName', '').strip()
    current_deployment_group_name = request.get('currentDeploymentGroupName', '').strip()
    new_deployment_group_name = request.get('newDeploymentGroupName', '').strip()

    # Verify deployment config if being changed
    deployment_config_name = request.get('deploymentConfigName')
    if deployment_config_name:
        store.deployment_configs.get_deployment_config(deployment_config_name)

    update_kwargs = {}
    field_mapping = {
        'serviceRoleArn': 'serviceRoleArn',
        'deploymentConfigName': 'deploymentConfigName',
        'ec2TagFilters': 'ec2TagFilters',
        'onPremisesInstanceTagFilters': 'onPremisesInstanceTagFilters',
        'autoScalingGroups': 'autoScalingGroups',
        'triggerConfigurations': 'triggerConfigurations',
        'alarmConfiguration': 'alarmConfiguration',
        'autoRollbackConfiguration': 'autoRollbackConfiguration',
        'deploymentStyle': 'deploymentStyle',
        'loadBalancerInfo': 'loadBalancerInfo',
        'blueGreenDeploymentConfiguration': 'blueGreenDeploymentConfiguration',
        'outdatedInstancesStrategy': 'outdatedInstancesStrategy',
    }
    for request_key, attr_name in field_mapping.items():
        if request_key in request:
            update_kwargs[attr_name] = request[request_key]

    group = store.deployment_groups.update_deployment_group(
        application_name=application_name,
        current_deployment_group_name=current_deployment_group_name,
        new_deployment_group_name=new_deployment_group_name if new_deployment_group_name else None,
        **update_kwargs,
    )
    return {}
