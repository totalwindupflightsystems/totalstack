"""UpdateApplication handler for CodeDeploy."""


def update_application(store, request):
    application_name = request.get('applicationName', '').strip()
    new_application_name = request.get('newApplicationName', '').strip()

    app = store.applications.update_application(
        application_name=application_name if application_name else None,
        new_application_name=new_application_name if new_application_name else None,
    )
    return {}
