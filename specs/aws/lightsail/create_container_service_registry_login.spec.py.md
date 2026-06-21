---
id: "@specs/aws/lightsail/create_container_service_registry_login"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_CreateContainerServiceRegistryLogin"
---

# CreateContainerServiceRegistryLogin

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/create_container_service_registry_login
> **spec:implements:** @kind:operation CreateContainerServiceRegistryLogin
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_CreateContainerServiceRegistryLogin.spec.md

Creates a temporary set of log in credentials that you can use to log in to the Docker process on your local machine. After you're logged in, you can use the native Docker commands to push your local container images to the container image registry of your Amazon Lightsail account so that you can use them with your Lightsail container service. The log in credentials expire 12 hours after they are created, at which point you will need to create a new set of log in credentials. You can only push container images to the container service registry of your Lightsail account. You cannot pull container images or perform any other container image management actions on the container service registry. After you push your container images to the container image registry of your Lightsail account, use the RegisterContainerImage action to register the pushed images to a specific Lightsail container service. This action is not required if you install and use the Lightsail Control (lightsailctl) plugin to push container images to your Lightsail container service. For more information, see Pushing and managing container images on your Amazon Lightsail container services in the Amazon Lightsail Developer Guide .

## Input Shape: CreateContainerServiceRegistryLoginRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|

## Output Shape: CreateContainerServiceRegistryLoginResult

- **registryLogin** (Any  # complex shape): An object that describes the log in information for the container service registry of your Lightsail account.

## Errors
- **ServiceException**: A general service exception.
- **InvalidInputException**: Lightsail throws this exception when user input does not conform to the validation rules of an input field. Domain and distribution APIs are only available in the N. Virginia ( us-east-1 ) Amazon Web 
- **NotFoundException**: Lightsail throws this exception when it cannot find a resource.
- **AccessDeniedException**: Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
- **UnauthenticatedException**: Lightsail throws this exception when the user has not been authenticated.
- **RegionSetupInProgressException**: Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.

## Implementation

```speclang
def create_container_service_registry_login(store, request: dict) -> dict:
    """Creates a temporary set of log in credentials that you can use to log in to the Docker process on your local machine. After you're logged in, you can use the native Docker commands to push your local """


    record = {
    }

    store.container_service_registry_logins(record)

    return {
        "registryLogin": record.get("registryLogin", {}),
    }
```
