---
id: "@specs/aws/iam/get_open_id_connect_provider"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_GetOpenIDConnectProvider"
---

# GetOpenIDConnectProvider

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/get_open_id_connect_provider
> **spec:implements:** @kind:operation GetOpenIDConnectProvider
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_GetOpenIDConnectProvider.spec.md

Returns information about the specified OpenID Connect (OIDC) provider resource object in IAM.

## Input Shape: GetOpenIDConnectProviderRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| OpenIDConnectProviderArn | Any  # complex shape | ✓ | The Amazon Resource Name (ARN) of the OIDC provider resource object in IAM to get information for. You can get a list of |

## Output Shape: GetOpenIDConnectProviderResponse

- **ClientIDList** (Any  # complex shape): A list of client IDs (also known as audiences) that are associated with the specified IAM OIDC provider resource object.
- **CreateDate** (Any  # complex shape): The date and time when the IAM OIDC provider resource object was created in the Amazon Web Services account.
- **Tags** (Any  # complex shape): A list of tags that are attached to the specified IAM OIDC provider. The returned list of tags is sorted by tag key. For
- **ThumbprintList** (Any  # complex shape): A list of certificate thumbprints that are associated with the specified IAM OIDC provider resource object. For more inf
- **Url** (Any  # complex shape): The URL that the IAM OIDC provider resource object is associated with. For more information, see CreateOpenIDConnectProv

## Errors
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def get_open_id_connect_provider(store, request: dict) -> dict:
    """Returns information about the specified OpenID Connect (OIDC) provider resource object in IAM."""
    open_id_connect_provider_arn = request.get("OpenIDConnectProviderArn", "").strip() if isinstance(request.get("OpenIDConnectProviderArn"), str) else request.get("OpenIDConnectProviderArn")
    if not open_id_connect_provider_arn:
        raise ValidationException("OpenIDConnectProviderArn is required")

    resource = store.open_id_connect_providers(open_id_connect_provider_arn)
    if not resource:
        raise ResourceNotFoundException(f"Resource open_id_connect_provider_arn not found")
    return {"OpenIDConnectProviderArn": open_id_connect_provider_arn, **resource}
```
