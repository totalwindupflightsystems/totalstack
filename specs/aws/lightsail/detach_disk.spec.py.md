---
id: "@specs/aws/lightsail/detach_disk"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_DetachDisk"
---

# DetachDisk

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/detach_disk
> **spec:implements:** @kind:operation DetachDisk
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_DetachDisk.spec.md

Detaches a stopped block storage disk from a Lightsail instance. Make sure to unmount any file systems on the device within your operating system before stopping the instance and detaching the disk. The detach disk operation supports tag-based access control via resource tags applied to the resource identified by disk name . For more information, see the Amazon Lightsail Developer Guide .

## Input Shape: DetachDiskRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| diskName | Any  # complex shape | ✓ | The unique name of the disk you want to detach from your instance ( my-disk ). |

## Output Shape: DetachDiskResult

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
def detach_disk(store, request: dict) -> dict:
    """Detaches a stopped block storage disk from a Lightsail instance. Make sure to unmount any file systems on the device within your operating system before stopping the instance and detaching the disk. T"""
    disk_name = request.get("diskName", "").strip() if isinstance(request.get("diskName"), str) else request.get("diskName")
    if not disk_name:
        raise ValidationException("diskName is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("DetachDisk", request)
```
