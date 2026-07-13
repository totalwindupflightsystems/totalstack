---
id: "@specs/aws/iam/deactivate_mfa_device"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_DeactivateMFADevice"
---

# DeactivateMFADevice

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/deactivate_mfa_device
> **spec:implements:** @kind:operation DeactivateMFADevice
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_DeactivateMFADevice.spec.md

Deactivates the specified MFA device and removes it from association with the user name for which it was originally enabled. For more information about creating and working with virtual MFA devices, see Enabling a virtual multi-factor authentication (MFA) device in the IAM User Guide .

## Input Shape: DeactivateMFADeviceRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| SerialNumber | Any  # complex shape | ✓ | The serial number that uniquely identifies the MFA device. For virtual MFA devices, the serial number is the device ARN. |
| UserName | Any  # complex shape |  | The name of the user whose MFA device you want to deactivate. This parameter is optional. If no user name is included, i |

## Errors
- **EntityTemporarilyUnmodifiableException**: The request was rejected because it referenced an entity that is temporarily unmodifiable, such as a user name that was deleted and then recreated. The error indicates that the request is likely to su
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.
- **ConcurrentModificationException**: The request was rejected because multiple requests to change this object were submitted simultaneously. Wait a few minutes and submit your request again.

## Implementation

```speclang
def deactivate_mfa_device(store, request: dict) -> dict:
    """Deactivates the specified MFA device and removes it from association with the user name for which it was originally enabled. For more information about creating and working with virtual MFA devices, s"""
    serial_number = request.get("SerialNumber", "").strip() if isinstance(request.get("SerialNumber"), str) else request.get("SerialNumber")
    if not serial_number:
        raise ValidationException("SerialNumber is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("DeactivateMFADevice", request)
```
