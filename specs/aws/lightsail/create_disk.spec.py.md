---
id: "@specs/aws/lightsail/create_disk"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_CreateDisk"
---

# CreateDisk

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/create_disk
> **spec:implements:** @kind:operation CreateDisk
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_CreateDisk.spec.md

Creates a block storage disk that can be attached to an Amazon Lightsail instance in the same Availability Zone ( us-east-2a ). The create disk operation supports tag-based access control via request tags. For more information, see the Amazon Lightsail Developer Guide .

## Input Shape: CreateDiskRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| addOns | list[Any  # complex shape] |  | An array of objects that represent the add-ons to enable for the new disk. |
| availabilityZone | Any  # complex shape | ✓ | The Availability Zone where you want to create the disk ( us-east-2a ). Use the same Availability Zone as the Lightsail  |
| diskName | Any  # complex shape | ✓ | The unique Lightsail disk name ( my-disk ). |
| sizeInGb | Any  # complex shape | ✓ | The size of the disk in GB ( 32 ). |
| tags | list[Any  # complex shape] |  | The tag keys and optional values to add to the resource during create. Use the TagResource action to tag a resource afte |

## Output Shape: CreateDiskResult

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
def create_disk(store, request: dict) -> dict:
    """Creates a block storage disk that can be attached to an Amazon Lightsail instance in the same Availability Zone ( us-east-2a ). The create disk operation supports tag-based access control via request """
    availability_zone = request.get("availabilityZone", "").strip() if isinstance(request.get("availabilityZone"), str) else request.get("availabilityZone")
    if not availability_zone:
        raise ValidationException("availabilityZone is required")
    disk_name = request.get("diskName", "").strip() if isinstance(request.get("diskName"), str) else request.get("diskName")
    if not disk_name:
        raise ValidationException("diskName is required")
    size_in_gb = request.get("sizeInGb", "").strip() if isinstance(request.get("sizeInGb"), str) else request.get("sizeInGb")
    if not size_in_gb:
        raise ValidationException("sizeInGb is required")

    if store.disks(disk_name):
        raise ResourceInUseException(f"Resource disk_name already exists")

    record = {
        "diskName": disk_name,
        "availabilityZone": availability_zone,
        "sizeInGb": size_in_gb,
        "tags": tags,
        "addOns": add_ons,
    }

    store.disks(disk_name, record)

    return {
        "operations": record.get("operations", {}),
    }
```
