"""GetApplication handler for CodeDeploy."""


def get_application(store, request):
    application_name = request.get('applicationName', '').strip()
    app = store.applications.get_application(application_name)
    return {'application': app.to_dict()}
