---
id: "@specs/aws/iam/untag_saml_provider"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_UntagSAMLProvider"
---

# UntagSAMLProvider

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/untag_saml_provider
> **spec:implements:** @kind:operation UntagSAMLProvider
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_UntagSAMLProvider.spec.md

Removes the specified tags from the specified Security Assertion Markup Language (SAML) identity provider in IAM. For more information about these providers, see About web identity federation . For more information about tagging, see Tagging IAM resources in the IAM User Guide .

## Input Shape: UntagSAMLProviderRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| SAMLProviderArn | Any  # complex shape | ✓ | The ARN of the SAML identity provider in IAM from which you want to remove tags. This parameter allows (through its rege |
| TagKeys | Any  # complex shape | ✓ | A list of key names as a simple array of strings. The tags with matching keys are removed from the specified SAML identi |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
- **ConcurrentModificationException**: The request was rejected because multiple requests to change this object were submitted simultaneously. Wait a few minutes and submit your request again.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def untag_saml_provider(store, request: dict) -> dict:
    """Removes the specified tags from the specified Security Assertion Markup Language (SAML) identity provider in IAM. For more information about these providers, see About web identity federation . For mo"""
    saml_provider_arn = request.get("SAMLProviderArn", "").strip() if isinstance(request.get("SAMLProviderArn"), str) else request.get("SAMLProviderArn")
    if not saml_provider_arn:
        raise ValidationException("SAMLProviderArn is required")
    tag_keys = request.get("TagKeys", "").strip() if isinstance(request.get("TagKeys"), str) else request.get("TagKeys")
    if not tag_keys:
        raise ValidationException("TagKeys is required")

    # Tag/untag resource
    resource_arn = request.get("ResourceARN", request.get("ResourceName", ""))
    store.tag_resource(resource_arn, request.get("Tags", []))
    return {}
```
