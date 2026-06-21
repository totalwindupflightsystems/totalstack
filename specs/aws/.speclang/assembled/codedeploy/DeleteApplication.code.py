"""DeleteApplication handler for CodeDeploy."""


def delete_application(store, request):
    application_name = request.get('applicationName', '').strip()
    store.applications.delete_application(application_name)
    return {}
