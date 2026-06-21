---
id: "@specs/aws/lightsail/get_container_service_deployments"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_GetContainerServiceDeployments"
---

# GetContainerServiceDeployments

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/get_container_service_deployments
> **spec:implements:** @kind:operation GetContainerServiceDeployments
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_GetContainerServiceDeployments.spec.md

Returns the deployments for your Amazon Lightsail container service A deployment specifies the settings, such as the ports and launch command, of containers that are deployed to your container service. The deployments are ordered by version in ascending order. The newest version is listed at the top of the response. A set number of deployments are kept before the oldest one is replaced with the newest one. For more information, see Amazon Lightsail endpoints and quotas in the Amazon Web Services General Reference .

## Input Shape: GetContainerServiceDeploymentsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| serviceName | Any  # complex shape | ✓ | The name of the container service for which to return deployments. |

## Output Shape: GetContainerServiceDeploymentsResult

- **deployments** (list[Any  # complex shape]): An array of objects that describe deployments for a container service.

## Errors
- **ServiceException**: A general service exception.
- **InvalidInputException**: Lightsail throws this exception when user input does not conform to the validation rules of an input field. Domain and distribution APIs are only available in the N. Virginia ( us-east-1 ) Amazon Web 
- **NotFoundException**: Lightsail throws this exception when it cannot find a resource.
- **AccessDeniedException**: Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
- **UnauthenticatedException**: Lightsail throws this exception when the user has not been authenticated.
- **RegionSetupInProgressException**: Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.

## Implementation

```speclang
def get_container_service_deployments(store, request: dict) -> dict:
    """Returns the deployments for your Amazon Lightsail container service A deployment specifies the settings, such as the ports and launch command, of containers that are deployed to your container service"""
    service_name = request.get("serviceName", "").strip() if isinstance(request.get("serviceName"), str) else request.get("serviceName")
    if not service_name:
        raise ValidationException("serviceName is required")

    resource = store.container_service_deploymentss(service_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource service_name not found")
    return {"serviceName": service_name, **resource}
```
