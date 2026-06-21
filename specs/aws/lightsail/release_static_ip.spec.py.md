---
id: "@specs/aws/lightsail/release_static_ip"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_ReleaseStaticIp"
---

# ReleaseStaticIp

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/release_static_ip
> **spec:implements:** @kind:operation ReleaseStaticIp
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_ReleaseStaticIp.spec.md

Deletes a specific static IP from your account.

## Input Shape: ReleaseStaticIpRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| staticIpName | Any  # complex shape | ✓ | The name of the static IP to delete. |

## Output Shape: ReleaseStaticIpResult

- **operations** (list[Any  # complex shape]): An array of objects that describe the result of the action, such as the status of the request, the timestamp of the requ

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
def release_static_ip(store, request: dict) -> dict:
    """Deletes a specific static IP from your account."""
    static_ip_name = request.get("staticIpName", "").strip() if isinstance(request.get("staticIpName"), str) else request.get("staticIpName")
    if not static_ip_name:
        raise ValidationException("staticIpName is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("ReleaseStaticIp", request)
```
