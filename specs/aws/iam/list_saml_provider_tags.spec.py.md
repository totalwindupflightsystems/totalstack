---
id: "@specs/aws/iam/list_saml_provider_tags"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_ListSAMLProviderTags"
---

# ListSAMLProviderTags

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/list_saml_provider_tags
> **spec:implements:** @kind:operation ListSAMLProviderTags
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_ListSAMLProviderTags.spec.md

Lists the tags that are attached to the specified Security Assertion Markup Language (SAML) identity provider. The returned list of tags is sorted by tag key. For more information, see About SAML 2.0-based federation . For more information about tagging, see Tagging IAM resources in the IAM User Guide .

## Input Shape: ListSAMLProviderTagsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Marker | Any  # complex shape |  | Use this parameter only when paginating results and only after you receive a response indicating that the results are tr |
| MaxItems | Any  # complex shape |  | Use this only when paginating results to indicate the maximum number of items you want in the response. If additional it |
| SAMLProviderArn | Any  # complex shape | ✓ | The ARN of the Security Assertion Markup Language (SAML) identity provider whose tags you want to see. This parameter al |

## Output Shape: ListSAMLProviderTagsResponse

- **IsTruncated** (Any  # complex shape): A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent 
- **Marker** (Any  # complex shape): When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequen
- **Tags** (Any  # complex shape): The list of tags that are currently attached to the Security Assertion Markup Language (SAML) identity provider. Each ta

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.

## Implementation

```speclang
def list_saml_provider_tags(store, request: dict) -> dict:
    """Lists the tags that are attached to the specified Security Assertion Markup Language (SAML) identity provider. The returned list of tags is sorted by tag key. For more information, see About SAML 2.0-"""
    saml_provider_arn = request.get("SAMLProviderArn", "").strip() if isinstance(request.get("SAMLProviderArn"), str) else request.get("SAMLProviderArn")
    if not saml_provider_arn:
        raise ValidationException("SAMLProviderArn is required")

    items = store.list_saml_provider_tagss()
    return {"Tags": list(items.values())}
```
