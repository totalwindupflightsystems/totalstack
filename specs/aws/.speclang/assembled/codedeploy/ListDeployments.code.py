"""ListDeployments handler for CodeDeploy."""


def list_deployments(store, request):
    application_name = request.get('applicationName', '').strip()
    deployment_group_name = request.get('deploymentGroupName', '').strip()
    include_only_statuses = request.get('includeOnlyStatuses')
    create_time_range = request.get('createTimeRange')
    next_token = request.get('nextToken')

    ids, _ = store.deployments.list_deployments(
        application_name=application_name if application_name else None,
        deployment_group_name=deployment_group_name if deployment_group_name else None,
        include_only_statuses=include_only_statuses,
        create_time_range=create_time_range,
        next_token=next_token,
    )
    return {'deployments': ids}
