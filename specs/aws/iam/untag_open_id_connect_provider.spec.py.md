---
id: "@specs/aws/iam/untag_open_id_connect_provider"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_UntagOpenIDConnectProvider"
---

# UntagOpenIDConnectProvider

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/untag_open_id_connect_provider
> **spec:implements:** @kind:operation UntagOpenIDConnectProvider
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_UntagOpenIDConnectProvider.spec.md

Removes the specified tags from the specified OpenID Connect (OIDC)-compatible identity provider in IAM. For more information about OIDC providers, see About web identity federation . For more information about tagging, see Tagging IAM resources in the IAM User Guide .

## Input Shape: UntagOpenIDConnectProviderRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| OpenIDConnectProviderArn | Any  # complex shape | ✓ | The ARN of the OIDC provider in IAM from which you want to remove tags. This parameter allows (through its regex pattern |
| TagKeys | Any  # complex shape | ✓ | A list of key names as a simple array of strings. The tags with matching keys are removed from the specified OIDC provid |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
- **ConcurrentModificationException**: The request was rejected because multiple requests to change this object were submitted simultaneously. Wait a few minutes and submit your request again.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def untag_open_id_connect_provider(store, request: dict) -> dict:
    """Removes the specified tags from the specified OpenID Connect (OIDC)-compatible identity provider in IAM. For more information about OIDC providers, see About web identity federation . For more informa"""
    open_id_connect_provider_arn = request.get("OpenIDConnectProviderArn", "").strip() if isinstance(request.get("OpenIDConnectProviderArn"), str) else request.get("OpenIDConnectProviderArn")
    if not open_id_connect_provider_arn:
        raise ValidationException("OpenIDConnectProviderArn is required")
    tag_keys = request.get("TagKeys", "").strip() if isinstance(request.get("TagKeys"), str) else request.get("TagKeys")
    if not tag_keys:
        raise ValidationException("TagKeys is required")

    # Tag/untag resource
    resource_arn = request.get("ResourceARN", request.get("ResourceName", ""))
    store.tag_resource(resource_arn, request.get("Tags", []))
    return {}
```
