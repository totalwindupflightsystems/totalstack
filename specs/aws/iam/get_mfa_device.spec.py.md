---
id: "@specs/aws/iam/get_mfa_device"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_GetMFADevice"
---

# GetMFADevice

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/get_mfa_device
> **spec:implements:** @kind:operation GetMFADevice
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_GetMFADevice.spec.md

Retrieves information about an MFA device for a specified user.

## Input Shape: GetMFADeviceRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| SerialNumber | Any  # complex shape | ✓ | Serial number that uniquely identifies the MFA device. For this API, we only accept FIDO security key ARNs . |
| UserName | Any  # complex shape |  | The friendly name identifying the user. |

## Output Shape: GetMFADeviceResponse

- **Certifications** (Any  # complex shape): The certifications of a specified user's MFA device. We currently provide FIPS-140-2, FIPS-140-3, and FIDO certification
- **EnableDate** (Any  # complex shape): The date that a specified user's MFA device was first enabled.
- **SerialNumber** (Any  # complex shape): Serial number that uniquely identifies the MFA device. For this API, we only accept FIDO security key ARNs .
- **UserName** (Any  # complex shape): The friendly name identifying the user.

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def get_mfa_device(store, request: dict) -> dict:
    """Retrieves information about an MFA device for a specified user."""
    serial_number = request.get("SerialNumber", "").strip() if isinstance(request.get("SerialNumber"), str) else request.get("SerialNumber")
    if not serial_number:
        raise ValidationException("SerialNumber is required")

    resource = store.mfa_devices(serial_number)
    if not resource:
        raise ResourceNotFoundException(f"Resource serial_number not found")
    return {"SerialNumber": serial_number, **resource}
```
