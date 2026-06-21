"""CreateDeploymentGroup handler for CodeDeploy."""


def create_deployment_group(store, request):
    application_name = request.get('applicationName', '').strip()
    deployment_group_name = request.get('deploymentGroupName', '').strip()
    service_role_arn = request.get('serviceRoleArn', '').strip()

    # Verify application exists
    store.applications.get_application(application_name)

    # Validate deployment config if specified
    deployment_config_name = request.get('deploymentConfigName')
    if deployment_config_name:
        store.deployment_configs.get_deployment_config(deployment_config_name)

    group = store.deployment_groups.create_deployment_group(
        application_name=application_name,
        deployment_group_name=deployment_group_name,
        service_role_arn=service_role_arn,
        deploymentConfigName=deployment_config_name,
        ec2TagFilters=request.get('ec2TagFilters', []),
        onPremisesInstanceTagFilters=request.get('onPremisesInstanceTagFilters', []),
        autoScalingGroups=request.get('autoScalingGroups', []),
        triggerConfigurations=request.get('triggerConfigurations', []),
        alarmConfiguration=request.get('alarmConfiguration'),
        autoRollbackConfiguration=request.get('autoRollbackConfiguration'),
        deploymentStyle=request.get('deploymentStyle'),
        loadBalancerInfo=request.get('loadBalancerInfo'),
        blueGreenDeploymentConfiguration=request.get('blueGreenDeploymentConfiguration'),
        outdatedInstancesStrategy=request.get('outdatedInstancesStrategy', 'UPDATE'),
        tags=request.get('tags', []),
    )
    return {'deploymentGroupId': group.deploymentGroupId}
