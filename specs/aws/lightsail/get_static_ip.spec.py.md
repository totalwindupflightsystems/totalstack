---
id: "@specs/aws/lightsail/get_static_ip"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_GetStaticIp"
---

# GetStaticIp

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/get_static_ip
> **spec:implements:** @kind:operation GetStaticIp
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_GetStaticIp.spec.md

Returns information about an Amazon Lightsail static IP.

## Input Shape: GetStaticIpRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| staticIpName | Any  # complex shape | ✓ | The name of the static IP in Lightsail. |

## Output Shape: GetStaticIpResult

- **staticIp** (Any  # complex shape): An array of key-value pairs containing information about the requested static IP.

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
def get_static_ip(store, request: dict) -> dict:
    """Returns information about an Amazon Lightsail static IP."""
    static_ip_name = request.get("staticIpName", "").strip() if isinstance(request.get("staticIpName"), str) else request.get("staticIpName")
    if not static_ip_name:
        raise ValidationException("staticIpName is required")

    resource = store.static_ips(static_ip_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource static_ip_name not found")
    return {"staticIpName": static_ip_name, **resource}
```
