---
id: "@specs/aws/lightsail/get_instance_access_details"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_GetInstanceAccessDetails"
---

# GetInstanceAccessDetails

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/get_instance_access_details
> **spec:implements:** @kind:operation GetInstanceAccessDetails
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_GetInstanceAccessDetails.spec.md

Returns temporary SSH keys you can use to connect to a specific virtual private server, or instance . The get instance access details operation supports tag-based access control via resource tags applied to the resource identified by instance name . For more information, see the Amazon Lightsail Developer Guide .

## Input Shape: GetInstanceAccessDetailsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| instanceName | Any  # complex shape | ✓ | The name of the instance to access. |
| protocol | Any  # complex shape |  | The protocol to use to connect to your instance. Defaults to ssh . |

## Output Shape: GetInstanceAccessDetailsResult

- **accessDetails** (Any  # complex shape): An array of key-value pairs containing information about a get instance access request.

## Errors
- **ServiceException**: A general service exception.
- **InvalidInputException**: Lightsail throws this exception when user input does not conform to the validation rules of an input field. Domain and distribution APIs are only available in the N. Virginia ( us-east-1 ) Amazon Web 
- **NotFoundException**: Lightsail throws this exception when it cannot find a resource.
- **OperationFailureException**: Lightsail throws this exception when an operation fails to execute.
- **AccessDeniedException**: Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
- **AccountSetupInProgressException**: Lightsail throws this exception when an account is still in the setup in progress state.
- **RegionSetupInProgressException**: Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.
- **UnauthenticatedException**: Lightsail throws this exception when the user has not been authenticated.

## Implementation

```speclang
def get_instance_access_details(store, request: dict) -> dict:
    """Returns temporary SSH keys you can use to connect to a specific virtual private server, or instance . The get instance access details operation supports tag-based access control via resource tags appl"""
    instance_name = request.get("instanceName", "").strip() if isinstance(request.get("instanceName"), str) else request.get("instanceName")
    if not instance_name:
        raise ValidationException("instanceName is required")

    resource = store.instance_access_detailss(instance_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource instance_name not found")
    return {"instanceName": instance_name, **resource}
```
