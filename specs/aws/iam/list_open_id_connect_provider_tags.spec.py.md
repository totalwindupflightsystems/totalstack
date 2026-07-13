---
id: "@specs/aws/iam/list_open_id_connect_provider_tags"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_ListOpenIDConnectProviderTags"
---

# ListOpenIDConnectProviderTags

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/list_open_id_connect_provider_tags
> **spec:implements:** @kind:operation ListOpenIDConnectProviderTags
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_ListOpenIDConnectProviderTags.spec.md

Lists the tags that are attached to the specified OpenID Connect (OIDC)-compatible identity provider. The returned list of tags is sorted by tag key. For more information, see About web identity federation . For more information about tagging, see Tagging IAM resources in the IAM User Guide .

## Input Shape: ListOpenIDConnectProviderTagsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Marker | Any  # complex shape |  | Use this parameter only when paginating results and only after you receive a response indicating that the results are tr |
| MaxItems | Any  # complex shape |  | Use this only when paginating results to indicate the maximum number of items you want in the response. If additional it |
| OpenIDConnectProviderArn | Any  # complex shape | ✓ | The ARN of the OpenID Connect (OIDC) identity provider whose tags you want to see. This parameter allows (through its re |

## Output Shape: ListOpenIDConnectProviderTagsResponse

- **IsTruncated** (Any  # complex shape): A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent 
- **Marker** (Any  # complex shape): When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequen
- **Tags** (Any  # complex shape): The list of tags that are currently attached to the OpenID Connect (OIDC) identity provider. Each tag consists of a key 

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.

## Implementation

```speclang
def list_open_id_connect_provider_tags(store, request: dict) -> dict:
    """Lists the tags that are attached to the specified OpenID Connect (OIDC)-compatible identity provider. The returned list of tags is sorted by tag key. For more information, see About web identity feder"""
    open_id_connect_provider_arn = request.get("OpenIDConnectProviderArn", "").strip() if isinstance(request.get("OpenIDConnectProviderArn"), str) else request.get("OpenIDConnectProviderArn")

    if not store.open_id_connect_provider_tagss(open_id_connect_provider_arn):
        raise ResourceNotFoundException(f"Resource open_id_connect_provider_arn not found")
    store.delete_open_id_connect_provider_tagss(open_id_connect_provider_arn)
    return {}
```
