---
id: "@specs/aws/iam/create_virtual_mfa_device"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_CreateVirtualMFADevice"
---

# CreateVirtualMFADevice

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/create_virtual_mfa_device
> **spec:implements:** @kind:operation CreateVirtualMFADevice
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_CreateVirtualMFADevice.spec.md

Creates a new virtual MFA device for the Amazon Web Services account. After creating the virtual MFA, use EnableMFADevice to attach the MFA device to an IAM user. For more information about creating and working with virtual MFA devices, see Using a virtual MFA device in the IAM User Guide . For information about the maximum number of MFA devices you can create, see IAM and STS quotas in the IAM User Guide . The seed information contained in the QR code and the Base32 string should be treated like any other secret access information. In other words, protect the seed information as you would your Amazon Web Services access keys or your passwords. After you provision your virtual device, you should ensure that the information is destroyed following secure procedures.

## Input Shape: CreateVirtualMFADeviceRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Path | Any  # complex shape |  | The path for the virtual MFA device. For more information about paths, see IAM identifiers in the IAM User Guide . This  |
| Tags | Any  # complex shape |  | A list of tags that you want to attach to the new IAM virtual MFA device. Each tag consists of a key name and an associa |
| VirtualMFADeviceName | Any  # complex shape | ✓ | The name of the virtual MFA device, which must be unique. Use with path to uniquely identify a virtual MFA device. This  |

## Output Shape: CreateVirtualMFADeviceResponse

- **VirtualMFADevice** (Any  # complex shape): A structure containing details about the new virtual MFA device.

## Errors
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
- **EntityAlreadyExistsException**: The request was rejected because it attempted to create a resource that already exists.
- **ConcurrentModificationException**: The request was rejected because multiple requests to change this object were submitted simultaneously. Wait a few minutes and submit your request again.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def create_virtual_mfa_device(store, request: dict) -> dict:
    """Creates a new virtual MFA device for the Amazon Web Services account. After creating the virtual MFA, use EnableMFADevice to attach the MFA device to an IAM user. For more information about creating a"""
    virtual_mfa_device_name = request.get("VirtualMFADeviceName", "").strip() if isinstance(request.get("VirtualMFADeviceName"), str) else request.get("VirtualMFADeviceName")
    if not virtual_mfa_device_name:
        raise ValidationException("VirtualMFADeviceName is required")

    if store.virtual_mfa_devices(virtual_mfa_device_name):
        raise ResourceInUseException(f"Resource virtual_mfa_device_name already exists")

    record = {
        "Path": path,
        "VirtualMFADeviceName": virtual_mfa_device_name,
        "Tags": tags,
    }

    store.virtual_mfa_devices(virtual_mfa_device_name, record)

    return {
        "VirtualMFADevice": record.get("VirtualMFADevice", {}),
    }
```
