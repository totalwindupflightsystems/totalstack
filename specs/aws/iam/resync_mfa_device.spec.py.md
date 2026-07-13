---
id: "@specs/aws/iam/resync_mfa_device"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_ResyncMFADevice"
---

# ResyncMFADevice

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/resync_mfa_device
> **spec:implements:** @kind:operation ResyncMFADevice
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_ResyncMFADevice.spec.md

Synchronizes the specified MFA device with its IAM resource object on the Amazon Web Services servers. For more information about creating and working with virtual MFA devices, see Using a virtual MFA device in the IAM User Guide .

## Input Shape: ResyncMFADeviceRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AuthenticationCode1 | Any  # complex shape | ✓ | An authentication code emitted by the device. The format for this parameter is a sequence of six digits. |
| AuthenticationCode2 | Any  # complex shape | ✓ | A subsequent authentication code emitted by the device. The format for this parameter is a sequence of six digits. |
| SerialNumber | Any  # complex shape | ✓ | Serial number that uniquely identifies the MFA device. This parameter allows (through its regex pattern ) a string of ch |
| UserName | Any  # complex shape | ✓ | The name of the user whose MFA device you want to resynchronize. This parameter allows (through its regex pattern ) a st |

## Errors
- **InvalidAuthenticationCodeException**: The request was rejected because the authentication code was not recognized. The error message describes the specific error.
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.
- **ConcurrentModificationException**: The request was rejected because multiple requests to change this object were submitted simultaneously. Wait a few minutes and submit your request again.

## Implementation

```speclang
def resync_mfa_device(store, request: dict) -> dict:
    """Synchronizes the specified MFA device with its IAM resource object on the Amazon Web Services servers. For more information about creating and working with virtual MFA devices, see Using a virtual MFA"""
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

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("ResyncMFADevice", request)
```
