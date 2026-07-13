---
id: "@specs/aws/iam/delete_service_specific_credential"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_DeleteServiceSpecificCredential"
---

# DeleteServiceSpecificCredential

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/delete_service_specific_credential
> **spec:implements:** @kind:operation DeleteServiceSpecificCredential
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_DeleteServiceSpecificCredential.spec.md

Deletes the specified service-specific credential.

## Input Shape: DeleteServiceSpecificCredentialRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ServiceSpecificCredentialId | Any  # complex shape | ✓ | The unique identifier of the service-specific credential. You can get this value by calling ListServiceSpecificCredentia |
| UserName | Any  # complex shape |  | The name of the IAM user associated with the service-specific credential. If this value is not specified, then the opera |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.

## Implementation

```speclang
def delete_service_specific_credential(store, request: dict) -> dict:
    """Deletes the specified service-specific credential."""
    service_specific_credential_id = request.get("ServiceSpecificCredentialId", "").strip() if isinstance(request.get("ServiceSpecificCredentialId"), str) else request.get("ServiceSpecificCredentialId")

    if not store.service_specific_credentials(service_specific_credential_id):
        raise ResourceNotFoundException(f"Resource service_specific_credential_id not found")
    store.delete_service_specific_credentials(service_specific_credential_id)
    return {}
```
