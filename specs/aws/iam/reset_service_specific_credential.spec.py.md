---
id: "@specs/aws/iam/reset_service_specific_credential"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_ResetServiceSpecificCredential"
---

# ResetServiceSpecificCredential

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/reset_service_specific_credential
> **spec:implements:** @kind:operation ResetServiceSpecificCredential
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_ResetServiceSpecificCredential.spec.md

Resets the password for a service-specific credential. The new password is Amazon Web Services generated and cryptographically strong. It cannot be configured by the user. Resetting the password immediately invalidates the previous password associated with this user.

## Input Shape: ResetServiceSpecificCredentialRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ServiceSpecificCredentialId | Any  # complex shape | ✓ | The unique identifier of the service-specific credential. This parameter allows (through its regex pattern ) a string of |
| UserName | Any  # complex shape |  | The name of the IAM user associated with the service-specific credential. If this value is not specified, then the opera |

## Output Shape: ResetServiceSpecificCredentialResponse

- **ServiceSpecificCredential** (Any  # complex shape): A structure with details about the updated service-specific credential, including the new password. This is the only tim

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.

## Implementation

```speclang
def reset_service_specific_credential(store, request: dict) -> dict:
    """Resets the password for a service-specific credential. The new password is Amazon Web Services generated and cryptographically strong. It cannot be configured by the user. Resetting the password immed"""
    service_specific_credential_id = request.get("ServiceSpecificCredentialId", "").strip() if isinstance(request.get("ServiceSpecificCredentialId"), str) else request.get("ServiceSpecificCredentialId")
    if not service_specific_credential_id:
        raise ValidationException("ServiceSpecificCredentialId is required")

    resource = store.reset_service_specific_credentials(service_specific_credential_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource service_specific_credential_id not found")

    # Update mutable fields
    if "UserName" in request:
        resource["UserName"] = user_name

    store.reset_service_specific_credentials(service_specific_credential_id, resource)
    return resource
```
