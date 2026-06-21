---
id: "@specs/aws/lightsail/get_disk"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_GetDisk"
---

# GetDisk

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/get_disk
> **spec:implements:** @kind:operation GetDisk
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_GetDisk.spec.md

Returns information about a specific block storage disk.

## Input Shape: GetDiskRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| diskName | Any  # complex shape | ✓ | The name of the disk ( my-disk ). |

## Output Shape: GetDiskResult

- **disk** (Any  # complex shape): An object containing information about the disk.

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
def get_disk(store, request: dict) -> dict:
    """Returns information about a specific block storage disk."""
    disk_name = request.get("diskName", "").strip() if isinstance(request.get("diskName"), str) else request.get("diskName")
    if not disk_name:
        raise ValidationException("diskName is required")

    resource = store.disks(disk_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource disk_name not found")
    return {"diskName": disk_name, **resource}
```
