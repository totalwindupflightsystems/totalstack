---
id: "@specs/aws/lightsail/create_container_service_deployment"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_CreateContainerServiceDeployment"
---

# CreateContainerServiceDeployment

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/create_container_service_deployment
> **spec:implements:** @kind:operation CreateContainerServiceDeployment
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_CreateContainerServiceDeployment.spec.md

Creates a deployment for your Amazon Lightsail container service. A deployment specifies the containers that will be launched on the container service and their settings, such as the ports to open, the environment variables to apply, and the launch command to run. It also specifies the container that will serve as the public endpoint of the deployment and its settings, such as the HTTP or HTTPS port to use, and the health check configuration. You can deploy containers to your container service using container images from a public registry such as Amazon ECR Public, or from your local machine. For more information, see Creating container images for your Amazon Lightsail container services in the Amazon Lightsail Developer Guide .

## Input Shape: CreateContainerServiceDeploymentRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| containers | dict[str, Any] |  | An object that describes the settings of the containers that will be launched on the container service. |
| publicEndpoint | Any  # complex shape |  | An object that describes the settings of the public endpoint for the container service. |
| serviceName | Any  # complex shape | ✓ | The name of the container service for which to create the deployment. |

## Output Shape: CreateContainerServiceDeploymentResult

- **containerService** (Any  # complex shape): An object that describes a container service.

## Errors
- **ServiceException**: A general service exception.
- **InvalidInputException**: Lightsail throws this exception when user input does not conform to the validation rules of an input field. Domain and distribution APIs are only available in the N. Virginia ( us-east-1 ) Amazon Web 
- **NotFoundException**: Lightsail throws this exception when it cannot find a resource.
- **AccessDeniedException**: Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
- **UnauthenticatedException**: Lightsail throws this exception when the user has not been authenticated.
- **RegionSetupInProgressException**: Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.

## Implementation

```speclang
def create_container_service_deployment(store, request: dict) -> dict:
    """Creates a deployment for your Amazon Lightsail container service. A deployment specifies the containers that will be launched on the container service and their settings, such as the ports to open, th"""
    service_name = request.get("serviceName", "").strip() if isinstance(request.get("serviceName"), str) else request.get("serviceName")
    if not service_name:
        raise ValidationException("serviceName is required")

    if store.container_service_deployments(service_name):
        raise ResourceInUseException(f"Resource service_name already exists")

    record = {
        "serviceName": service_name,
        "containers": containers,
        "publicEndpoint": public_endpoint,
    }

    store.container_service_deployments(service_name, record)

    return {
        "containerService": record.get("containerService", {}),
    }
```
