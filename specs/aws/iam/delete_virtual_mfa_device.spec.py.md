---
id: "@specs/aws/iam/delete_virtual_mfa_device"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_DeleteVirtualMFADevice"
---

# DeleteVirtualMFADevice

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/delete_virtual_mfa_device
> **spec:implements:** @kind:operation DeleteVirtualMFADevice
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_DeleteVirtualMFADevice.spec.md

Deletes a virtual MFA device. You must deactivate a user's virtual MFA device before you can delete it. For information about deactivating MFA devices, see DeactivateMFADevice .

## Input Shape: DeleteVirtualMFADeviceRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| SerialNumber | Any  # complex shape | ✓ | The serial number that uniquely identifies the MFA device. For virtual MFA devices, the serial number is the same as the |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **DeleteConflictException**: The request was rejected because it attempted to delete a resource that has attached subordinate entities. The error message describes these entities.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.
- **ConcurrentModificationException**: The request was rejected because multiple requests to change this object were submitted simultaneously. Wait a few minutes and submit your request again.

## Implementation

```speclang
def delete_virtual_mfa_device(store, request: dict) -> dict:
    """Deletes a virtual MFA device. You must deactivate a user's virtual MFA device before you can delete it. For information about deactivating MFA devices, see DeactivateMFADevice ."""
    serial_number = request.get("SerialNumber", "").strip() if isinstance(request.get("SerialNumber"), str) else request.get("SerialNumber")

    if not store.virtual_mfa_devices(serial_number):
        raise ResourceNotFoundException(f"Resource serial_number not found")
    store.delete_virtual_mfa_devices(serial_number)
    return {}
```
