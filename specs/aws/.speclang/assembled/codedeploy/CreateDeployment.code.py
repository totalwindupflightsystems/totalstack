"""CreateDeployment handler for CodeDeploy."""


def create_deployment(store, request):
    application_name = request.get('applicationName', '').strip()
    deployment_group_name = request.get('deploymentGroupName', '').strip()
    revision = request.get('revision')
    deployment_config_name = request.get('deploymentConfigName')

    # Verify application exists
    store.applications.get_application(application_name)

    # Verify deployment group if specified
    if deployment_group_name:
        store.deployment_groups.get_deployment_group(application_name, deployment_group_name)

    # Verify revision if specified
    if not revision:
        revision = {
            'revisionType': 'S3',
            's3Location': {
                'bucket': 'test-bucket',
                'key': 'test-key',
                'bundleType': 'zip',
            }
        }

    if revision.get('revisionType') not in ('S3', 'GitHub', 'String', 'AppSpecContent'):
        raise InvalidRevisionException(
            f"Invalid revisionType '{revision.get('revisionType')}'")

    # Verify deployment config if specified
    if deployment_config_name:
        store.deployment_configs.get_deployment_config(deployment_config_name)

    deployment = store.deployments.create_deployment(
        application_name=application_name,
        deployment_group_name=deployment_group_name,
        revision=revision,
        deploymentConfigName=deployment_config_name,
        description=request.get('description', ''),
        fileExistsBehavior=request.get('fileExistsBehavior', 'DISALLOW'),
        updateOutdatedInstancesOnly=request.get('updateOutdatedInstancesOnly', False),
        ignoreApplicationStopFailures=request.get('ignoreApplicationStopFailures', False),
        targetInstances=request.get('targetInstances'),
    )
    return {'deploymentId': deployment.deploymentId}
