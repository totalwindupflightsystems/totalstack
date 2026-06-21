---
id: "@specs/aws/lightsail/attach_disk"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_AttachDisk"
---

# AttachDisk

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/attach_disk
> **spec:implements:** @kind:operation AttachDisk
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_AttachDisk.spec.md

Attaches a block storage disk to a running or stopped Lightsail instance and exposes it to the instance with the specified disk name. The attach disk operation supports tag-based access control via resource tags applied to the resource identified by disk name . For more information, see the Amazon Lightsail Developer Guide .

## Input Shape: AttachDiskRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| autoMounting | Any  # complex shape |  | A Boolean value used to determine the automatic mounting of a storage volume to a virtual computer. The default value is |
| diskName | Any  # complex shape | ✓ | The unique Lightsail disk name ( my-disk ). |
| diskPath | Any  # complex shape | ✓ | The disk path to expose to the instance ( /dev/xvdf ). |
| instanceName | Any  # complex shape | ✓ | The name of the Lightsail instance where you want to utilize the storage disk. |

## Output Shape: AttachDiskResult

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
def attach_disk(store, request: dict) -> dict:
    """Attaches a block storage disk to a running or stopped Lightsail instance and exposes it to the instance with the specified disk name. The attach disk operation supports tag-based access control via re"""
    disk_name = request.get("diskName", "").strip() if isinstance(request.get("diskName"), str) else request.get("diskName")
    if not disk_name:
        raise ValidationException("diskName is required")
    disk_path = request.get("diskPath", "").strip() if isinstance(request.get("diskPath"), str) else request.get("diskPath")
    if not disk_path:
        raise ValidationException("diskPath is required")
    instance_name = request.get("instanceName", "").strip() if isinstance(request.get("instanceName"), str) else request.get("instanceName")
    if not instance_name:
        raise ValidationException("instanceName is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AttachDisk", request)
```
