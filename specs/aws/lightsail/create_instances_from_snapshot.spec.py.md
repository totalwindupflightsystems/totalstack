---
id: "@specs/aws/lightsail/create_instances_from_snapshot"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_CreateInstancesFromSnapshot"
---

# CreateInstancesFromSnapshot

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/create_instances_from_snapshot
> **spec:implements:** @kind:operation CreateInstancesFromSnapshot
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_CreateInstancesFromSnapshot.spec.md

Creates one or more new instances from a manual or automatic snapshot of an instance. The create instances from snapshot operation supports tag-based access control via request tags and resource tags applied to the resource identified by instance snapshot name . For more information, see the Amazon Lightsail Developer Guide .

## Input Shape: CreateInstancesFromSnapshotRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| addOns | list[Any  # complex shape] |  | An array of objects representing the add-ons to enable for the new instance. |
| attachedDiskMapping | dict[str, Any] |  | An object containing information about one or more disk mappings. |
| availabilityZone | Any  # complex shape | ✓ | The Availability Zone where you want to create your instances. Use the following formatting: us-east-2a (case sensitive) |
| bundleId | Any  # complex shape | ✓ | The bundle of specification information for your virtual private server (or instance ), including the pricing plan ( mic |
| instanceNames | list[Any  # complex shape] | ✓ | The names for your new instances. |
| instanceSnapshotName | Any  # complex shape |  | The name of the instance snapshot on which you are basing your new instances. Use the get instance snapshots operation t |
| ipAddressType | Any  # complex shape |  | The IP address type for the instance. The possible values are ipv4 for IPv4 only, ipv6 for IPv6 only, and dualstack for  |
| keyPairName | Any  # complex shape |  | The name for your key pair. |
| restoreDate | Any  # complex shape |  | The date of the automatic snapshot to use for the new instance. Use the get auto snapshots operation to identify the dat |
| sourceInstanceName | Any  # complex shape |  | The name of the source instance from which the source automatic snapshot was created. Constraints: This parameter cannot |
| tags | list[Any  # complex shape] |  | The tag keys and optional values to add to the resource during create. Use the TagResource action to tag a resource afte |
| useLatestRestorableAutoSnapshot | Any  # complex shape |  | A Boolean value to indicate whether to use the latest available automatic snapshot. Constraints: This parameter cannot b |
| userData | Any  # complex shape |  | You can create a launch script that configures a server with additional user data. For example, apt-get -y update . Depe |

## Output Shape: CreateInstancesFromSnapshotResult

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
def create_instances_from_snapshot(store, request: dict) -> dict:
    """Creates one or more new instances from a manual or automatic snapshot of an instance. The create instances from snapshot operation supports tag-based access control via request tags and resource tags """
    availability_zone = request.get("availabilityZone", "").strip() if isinstance(request.get("availabilityZone"), str) else request.get("availabilityZone")
    if not availability_zone:
        raise ValidationException("availabilityZone is required")
    bundle_id = request.get("bundleId", "").strip() if isinstance(request.get("bundleId"), str) else request.get("bundleId")
    if not bundle_id:
        raise ValidationException("bundleId is required")
    instance_names = request.get("instanceNames", "").strip() if isinstance(request.get("instanceNames"), str) else request.get("instanceNames")
    if not instance_names:
        raise ValidationException("instanceNames is required")

    if store.instances_from_snapshots(instance_names):
        raise ResourceInUseException(f"Resource instance_names already exists")

    record = {
        "instanceNames": instance_names,
        "attachedDiskMapping": attached_disk_mapping,
        "availabilityZone": availability_zone,
        "instanceSnapshotName": instance_snapshot_name,
        "bundleId": bundle_id,
        "userData": user_data,
        "keyPairName": key_pair_name,
        "tags": tags,
        "addOns": add_ons,
        "ipAddressType": ip_address_type,
        "sourceInstanceName": source_instance_name,
        "restoreDate": restore_date,
        "useLatestRestorableAutoSnapshot": use_latest_restorable_auto_snapshot,
    }

    store.instances_from_snapshots(instance_names, record)

    return {
        "operations": record.get("operations", {}),
    }
```
