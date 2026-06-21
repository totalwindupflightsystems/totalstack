"""ListApplications handler for CodeDeploy."""


def list_applications(store, request):
    next_token = request.get('nextToken')
    names, _ = store.applications.list_applications(next_token=next_token)
    return {'applications': names}
