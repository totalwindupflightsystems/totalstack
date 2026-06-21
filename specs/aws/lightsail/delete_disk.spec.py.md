---
id: "@specs/aws/lightsail/delete_disk"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_DeleteDisk"
---

# DeleteDisk

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/delete_disk
> **spec:implements:** @kind:operation DeleteDisk
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_DeleteDisk.spec.md

Deletes the specified block storage disk. The disk must be in the available state (not attached to a Lightsail instance). The disk may remain in the deleting state for several minutes. The delete disk operation supports tag-based access control via resource tags applied to the resource identified by disk name . For more information, see the Amazon Lightsail Developer Guide .

## Input Shape: DeleteDiskRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| diskName | Any  # complex shape | ✓ | The unique name of the disk you want to delete ( my-disk ). |
| forceDeleteAddOns | Any  # complex shape |  | A Boolean value to indicate whether to delete all add-ons for the disk. |

## Output Shape: DeleteDiskResult

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
def delete_disk(store, request: dict) -> dict:
    """Deletes the specified block storage disk. The disk must be in the available state (not attached to a Lightsail instance). The disk may remain in the deleting state for several minutes. The delete disk"""
    disk_name = request.get("diskName", "").strip() if isinstance(request.get("diskName"), str) else request.get("diskName")

    if not store.disks(disk_name):
        raise ResourceNotFoundException(f"Resource disk_name not found")
    store.delete_disks(disk_name)
    return {}
```
