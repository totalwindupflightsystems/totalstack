---
id: "@specs/aws/iam/update_open_id_connect_provider_thumbprint"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_UpdateOpenIDConnectProviderThumbprint"
---

# UpdateOpenIDConnectProviderThumbprint

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/update_open_id_connect_provider_thumbprint
> **spec:implements:** @kind:operation UpdateOpenIDConnectProviderThumbprint
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_UpdateOpenIDConnectProviderThumbprint.spec.md

Replaces the existing list of server certificate thumbprints associated with an OpenID Connect (OIDC) provider resource object with a new list of thumbprints. The list that you pass with this operation completely replaces the existing list of thumbprints. (The lists are not merged.) Typically, you need to update a thumbprint only when the identity provider certificate changes, which occurs rarely. However, if the provider's certificate does change, any attempt to assume an IAM role that specifies the OIDC provider as a principal fails until the certificate thumbprint is updated. Amazon Web Services secures communication with OIDC identity providers (IdPs) using our library of trusted root certificate authorities (CAs) to verify the JSON Web Key Set (JWKS) endpoint's TLS certificate. If your OIDC IdP relies on a certificate that is not signed by one of these trusted CAs, only then we secure communication using the thumbprints set in the IdP's configuration. Trust for the OIDC provider is derived from the provider certificate and is validated by the thumbprint. Therefore, it is best to limit access to the UpdateOpenIDConnectProviderThumbprint operation to highly privileged users.

## Input Shape: UpdateOpenIDConnectProviderThumbprintRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| OpenIDConnectProviderArn | Any  # complex shape | ✓ | The Amazon Resource Name (ARN) of the IAM OIDC provider resource object for which you want to update the thumbprint. You |
| ThumbprintList | Any  # complex shape | ✓ | A list of certificate thumbprints that are associated with the specified IAM OpenID Connect provider. For more informati |

## Errors
- **ConcurrentModificationException**: The request was rejected because multiple requests to change this object were submitted simultaneously. Wait a few minutes and submit your request again.
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def update_open_id_connect_provider_thumbprint(store, request: dict) -> dict:
    """Replaces the existing list of server certificate thumbprints associated with an OpenID Connect (OIDC) provider resource object with a new list of thumbprints. The list that you pass with this operatio"""
    open_id_connect_provider_arn = request.get("OpenIDConnectProviderArn", "").strip() if isinstance(request.get("OpenIDConnectProviderArn"), str) else request.get("OpenIDConnectProviderArn")
    if not open_id_connect_provider_arn:
        raise ValidationException("OpenIDConnectProviderArn is required")
    thumbprint_list = request.get("ThumbprintList", "").strip() if isinstance(request.get("ThumbprintList"), str) else request.get("ThumbprintList")
    if not thumbprint_list:
        raise ValidationException("ThumbprintList is required")

    resource = store.open_id_connect_provider_thumbprints(open_id_connect_provider_arn)
    if not resource:
        raise ResourceNotFoundException(f"Resource open_id_connect_provider_arn not found")

    # Update mutable fields

    store.open_id_connect_provider_thumbprints(open_id_connect_provider_arn, resource)
    return resource
```
