---
id: "@specs/aws/iam/get_saml_provider"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_GetSAMLProvider"
---

# GetSAMLProvider

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/get_saml_provider
> **spec:implements:** @kind:operation GetSAMLProvider
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_GetSAMLProvider.spec.md

Returns the SAML provider metadocument that was uploaded when the IAM SAML provider resource object was created or updated. This operation requires Signature Version 4 .

## Input Shape: GetSAMLProviderRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| SAMLProviderArn | Any  # complex shape | ✓ | The Amazon Resource Name (ARN) of the SAML provider resource object in IAM to get information about. For more informatio |

## Output Shape: GetSAMLProviderResponse

- **AssertionEncryptionMode** (Any  # complex shape): Specifies the encryption setting for the SAML provider.
- **CreateDate** (Any  # complex shape): The date and time when the SAML provider was created.
- **PrivateKeyList** (list[Any  # complex shape]): The private key metadata for the SAML provider.
- **SAMLMetadataDocument** (Any  # complex shape): The XML metadata document that includes information about an identity provider.
- **SAMLProviderUUID** (Any  # complex shape): The unique identifier assigned to the SAML provider.
- **Tags** (Any  # complex shape): A list of tags that are attached to the specified IAM SAML provider. The returned list of tags is sorted by tag key. For
- **ValidUntil** (Any  # complex shape): The expiration date and time for the SAML provider.

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def get_saml_provider(store, request: dict) -> dict:
    """Returns the SAML provider metadocument that was uploaded when the IAM SAML provider resource object was created or updated. This operation requires Signature Version 4 ."""
    saml_provider_arn = request.get("SAMLProviderArn", "").strip() if isinstance(request.get("SAMLProviderArn"), str) else request.get("SAMLProviderArn")
    if not saml_provider_arn:
        raise ValidationException("SAMLProviderArn is required")

    resource = store.saml_providers(saml_provider_arn)
    if not resource:
        raise ResourceNotFoundException(f"Resource saml_provider_arn not found")
    return {"SAMLProviderArn": saml_provider_arn, **resource}
```
