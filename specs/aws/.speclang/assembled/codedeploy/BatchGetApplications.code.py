"""BatchGetApplications handler for CodeDeploy."""


def batch_get_applications(store, request):
    application_names = request.get('applicationNames', [])
    if not application_names:
        raise InvalidInputException("applicationNames is required")

    apps = store.applications.batch_get_applications(application_names)
    return {'applicationsInfo': [a.to_dict() for a in apps]}
