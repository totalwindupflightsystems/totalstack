"""DeleteDeploymentGroup handler for CodeDeploy."""


def delete_deployment_group(store, request):
    application_name = request.get('applicationName', '').strip()
    deployment_group_name = request.get('deploymentGroupName', '').strip()
    store.deployment_groups.delete_deployment_group(application_name, deployment_group_name)
    return {}
