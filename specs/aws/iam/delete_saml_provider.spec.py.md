---
id: "@specs/aws/iam/delete_saml_provider"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_DeleteSAMLProvider"
---

# DeleteSAMLProvider

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/delete_saml_provider
> **spec:implements:** @kind:operation DeleteSAMLProvider
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_DeleteSAMLProvider.spec.md

Deletes a SAML provider resource in IAM. Deleting the provider resource from IAM does not update any roles that reference the SAML provider resource's ARN as a principal in their trust policies. Any attempt to assume a role that references a non-existent provider resource ARN fails. This operation requires Signature Version 4 .

## Input Shape: DeleteSAMLProviderRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| SAMLProviderArn | Any  # complex shape | ✓ | The Amazon Resource Name (ARN) of the SAML provider to delete. |

## Errors
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def delete_saml_provider(store, request: dict) -> dict:
    """Deletes a SAML provider resource in IAM. Deleting the provider resource from IAM does not update any roles that reference the SAML provider resource's ARN as a principal in their trust policies. Any a"""
    saml_provider_arn = request.get("SAMLProviderArn", "").strip() if isinstance(request.get("SAMLProviderArn"), str) else request.get("SAMLProviderArn")

    if not store.saml_providers(saml_provider_arn):
        raise ResourceNotFoundException(f"Resource saml_provider_arn not found")
    store.delete_saml_providers(saml_provider_arn)
    return {}
```
