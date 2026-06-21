"""ListDeploymentGroups handler for CodeDeploy."""


def list_deployment_groups(store, request):
    application_name = request.get('applicationName', '').strip()
    next_token = request.get('nextToken')

    # Verify application exists
    store.applications.get_application(application_name)

    names, _ = store.deployment_groups.list_deployment_groups(
        application_name, next_token=next_token)
    return {'deploymentGroups': names}
