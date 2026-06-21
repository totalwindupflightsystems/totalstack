# spec:trace: aws/lightsail/create_container_service_registry_login.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/create-container-service-registry-login
# spec:generated: DO NOT EDIT — edit the spec instead

def create_container_service_registry_login(store, request: dict) -> dict:
    """Creates a temporary set of log in credentials that you can use to log in to the Docker process on your local machine. After you're logged in, you can use the native Docker commands to push your local """


    record = {
    }

    store.container_service_registry_logins(record)

    return {
        "registryLogin": record.get("registryLogin", {}),
    }

