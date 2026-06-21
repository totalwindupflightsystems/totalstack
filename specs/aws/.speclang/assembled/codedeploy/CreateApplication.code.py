"""CreateApplication handler for CodeDeploy."""
import uuid


def create_application(store, request):
    application_name = request.get('applicationName', '').strip()
    compute_platform = request.get('computePlatform', 'Server')

    if compute_platform not in ('Server', 'Lambda', 'ECS'):
        raise InvalidInputException(
            f"Invalid computePlatform '{compute_platform}'. Must be Server, Lambda, or ECS")

    app = store.applications.create_application(
        application_name=application_name,
        compute_platform=compute_platform,
        applicationId=str(uuid.uuid4()),
    )
    return {'applicationId': app.applicationId}
