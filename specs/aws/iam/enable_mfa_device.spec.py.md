---
id: "@specs/aws/iam/enable_mfa_device"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_EnableMFADevice"
---

# EnableMFADevice

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/enable_mfa_device
> **spec:implements:** @kind:operation EnableMFADevice
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_EnableMFADevice.spec.md

Enables the specified MFA device and associates it with the specified IAM user. When enabled, the MFA device is required for every subsequent login by the IAM user associated with the device.

## Input Shape: EnableMFADeviceRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AuthenticationCode1 | Any  # complex shape | ✓ | An authentication code emitted by the device. The format for this parameter is a string of six digits. Submit your reque |
| AuthenticationCode2 | Any  # complex shape | ✓ | A subsequent authentication code emitted by the device. The format for this parameter is a string of six digits. Submit  |
| SerialNumber | Any  # complex shape | ✓ | The serial number that uniquely identifies the MFA device. For virtual MFA devices, the serial number is the device ARN. |
| UserName | Any  # complex shape | ✓ | The name of the IAM user for whom you want to enable the MFA device. This parameter allows (through its regex pattern )  |

## Errors
- **EntityAlreadyExistsException**: The request was rejected because it attempted to create a resource that already exists.
- **EntityTemporarilyUnmodifiableException**: The request was rejected because it referenced an entity that is temporarily unmodifiable, such as a user name that was deleted and then recreated. The error indicates that the request is likely to su
- **InvalidAuthenticationCodeException**: The request was rejected because the authentication code was not recognized. The error message describes the specific error.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.
- **ConcurrentModificationException**: The request was rejected because multiple requests to change this object were submitted simultaneously. Wait a few minutes and submit your request again.

## Implementation

```speclang
def enable_mfa_device(store, request: dict) -> dict:
    """Enables the specified MFA device and associates it with the specified IAM user. When enabled, the MFA device is required for every subsequent login by the IAM user associated with the device."""
    authentication_code1 = request.get("AuthenticationCode1", "").strip() if isinstance(request.get("AuthenticationCode1"), str) else request.get("AuthenticationCode1")
    if not authentication_code1:
        raise ValidationException("AuthenticationCode1 is required")
    authentication_code2 = request.get("AuthenticationCode2", "").strip() if isinstance(request.get("AuthenticationCode2"), str) else request.get("AuthenticationCode2")
    if not authentication_code2:
        raise ValidationException("AuthenticationCode2 is required")
    serial_number = request.get("SerialNumber", "").strip() if isinstance(request.get("SerialNumber"), str) else request.get("SerialNumber")
    if not serial_number:
        raise ValidationException("SerialNumber is required")
    user_name = request.get("UserName", "").strip() if isinstance(request.get("UserName"), str) else request.get("UserName")
    if not user_name:
        raise ValidationException("UserName is required")

    resource = store.enable_mfa_devices(user_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource user_name not found")

    # Update mutable fields

    store.enable_mfa_devices(user_name, resource)
    return resource
```
