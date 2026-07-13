---
id: "@specs/aws/iam/delete_open_id_connect_provider"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_DeleteOpenIDConnectProvider"
---

# DeleteOpenIDConnectProvider

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/delete_open_id_connect_provider
> **spec:implements:** @kind:operation DeleteOpenIDConnectProvider
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_DeleteOpenIDConnectProvider.spec.md

Deletes an OpenID Connect identity provider (IdP) resource object in IAM. Deleting an IAM OIDC provider resource does not update any roles that reference the provider as a principal in their trust policies. Any attempt to assume a role that references a deleted provider fails. This operation is idempotent; it does not fail or return an error if you call the operation for a provider that does not exist.

## Input Shape: DeleteOpenIDConnectProviderRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| OpenIDConnectProviderArn | Any  # complex shape | ✓ | The Amazon Resource Name (ARN) of the IAM OpenID Connect provider resource object to delete. You can get a list of OpenI |

## Errors
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def delete_open_id_connect_provider(store, request: dict) -> dict:
    """Deletes an OpenID Connect identity provider (IdP) resource object in IAM. Deleting an IAM OIDC provider resource does not update any roles that reference the provider as a principal in their trust pol"""
    open_id_connect_provider_arn = request.get("OpenIDConnectProviderArn", "").strip() if isinstance(request.get("OpenIDConnectProviderArn"), str) else request.get("OpenIDConnectProviderArn")

    if not store.open_id_connect_providers(open_id_connect_provider_arn):
        raise ResourceNotFoundException(f"Resource open_id_connect_provider_arn not found")
    store.delete_open_id_connect_providers(open_id_connect_provider_arn)
    return {}
```
