---
id: "@specs/aws/iam/update_service_specific_credential"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_UpdateServiceSpecificCredential"
---

# UpdateServiceSpecificCredential

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/update_service_specific_credential
> **spec:implements:** @kind:operation UpdateServiceSpecificCredential
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_UpdateServiceSpecificCredential.spec.md

Sets the status of a service-specific credential to Active or Inactive . Service-specific credentials that are inactive cannot be used for authentication to the service. This operation can be used to disable a user's service-specific credential as part of a credential rotation work flow.

## Input Shape: UpdateServiceSpecificCredentialRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ServiceSpecificCredentialId | Any  # complex shape | ✓ | The unique identifier of the service-specific credential. This parameter allows (through its regex pattern ) a string of |
| Status | Any  # complex shape | ✓ | The status to be assigned to the service-specific credential. |
| UserName | Any  # complex shape |  | The name of the IAM user associated with the service-specific credential. If you do not specify this value, then the ope |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.

## Implementation

```speclang
def update_service_specific_credential(store, request: dict) -> dict:
    """Sets the status of a service-specific credential to Active or Inactive . Service-specific credentials that are inactive cannot be used for authentication to the service. This operation can be used to """
    service_specific_credential_id = request.get("ServiceSpecificCredentialId", "").strip() if isinstance(request.get("ServiceSpecificCredentialId"), str) else request.get("ServiceSpecificCredentialId")
    if not service_specific_credential_id:
        raise ValidationException("ServiceSpecificCredentialId is required")
    status = request.get("Status", "").strip() if isinstance(request.get("Status"), str) else request.get("Status")
    if not status:
        raise ValidationException("Status is required")

    resource = store.service_specific_credentials(service_specific_credential_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource service_specific_credential_id not found")

    # Update mutable fields
    if "UserName" in request:
        resource["UserName"] = user_name

    store.service_specific_credentials(service_specific_credential_id, resource)
    return resource
```
