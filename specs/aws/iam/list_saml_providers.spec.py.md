---
id: "@specs/aws/iam/list_saml_providers"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_ListSAMLProviders"
---

# ListSAMLProviders

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/list_saml_providers
> **spec:implements:** @kind:operation ListSAMLProviders
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_ListSAMLProviders.spec.md

Lists the SAML provider resource objects defined in IAM in the account. IAM resource-listing operations return a subset of the available attributes for the resource. For example, this operation does not return tags, even though they are an attribute of the returned object. To view all of the information for a SAML provider, see GetSAMLProvider . This operation requires Signature Version 4 .

## Input Shape: ListSAMLProvidersRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|

## Output Shape: ListSAMLProvidersResponse

- **SAMLProviderList** (Any  # complex shape): The list of SAML provider resource objects defined in IAM for this Amazon Web Services account.

## Errors
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def list_saml_providers(store, request: dict) -> dict:
    """Lists the SAML provider resource objects defined in IAM in the account. IAM resource-listing operations return a subset of the available attributes for the resource. For example, this operation does n"""

    items = store.list_saml_providerss()
    return {"SAMLProviderList": list(items.values())}
```
