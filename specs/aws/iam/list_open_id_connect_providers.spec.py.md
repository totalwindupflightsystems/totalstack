---
id: "@specs/aws/iam/list_open_id_connect_providers"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_ListOpenIDConnectProviders"
---

# ListOpenIDConnectProviders

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/list_open_id_connect_providers
> **spec:implements:** @kind:operation ListOpenIDConnectProviders
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_ListOpenIDConnectProviders.spec.md

Lists information about the IAM OpenID Connect (OIDC) provider resource objects defined in the Amazon Web Services account. IAM resource-listing operations return a subset of the available attributes for the resource. For example, this operation does not return tags, even though they are an attribute of the returned object. To view all of the information for an OIDC provider, see GetOpenIDConnectProvider .

## Input Shape: ListOpenIDConnectProvidersRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|

## Output Shape: ListOpenIDConnectProvidersResponse

- **OpenIDConnectProviderList** (Any  # complex shape): The list of IAM OIDC provider resource objects defined in the Amazon Web Services account.

## Errors
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def list_open_id_connect_providers(store, request: dict) -> dict:
    """Lists information about the IAM OpenID Connect (OIDC) provider resource objects defined in the Amazon Web Services account. IAM resource-listing operations return a subset of the available attributes """

    return {}
```
