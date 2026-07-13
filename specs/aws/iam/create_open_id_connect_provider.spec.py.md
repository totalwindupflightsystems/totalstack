---
id: "@specs/aws/iam/create_open_id_connect_provider"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_CreateOpenIDConnectProvider"
---

# CreateOpenIDConnectProvider

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/create_open_id_connect_provider
> **spec:implements:** @kind:operation CreateOpenIDConnectProvider
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_CreateOpenIDConnectProvider.spec.md

Creates an IAM entity to describe an identity provider (IdP) that supports OpenID Connect (OIDC) . The OIDC provider that you create with this operation can be used as a principal in a role's trust policy. Such a policy establishes a trust relationship between Amazon Web Services and the OIDC provider. If you are using an OIDC identity provider from Google, Facebook, or Amazon Cognito, you don't need to create a separate IAM identity provider. These OIDC identity providers are already built-in to Amazon Web Services and are available for your use. Instead, you can move directly to creating new roles using your identity provider. To learn more, see Creating a role for web identity or OpenID connect federation in the IAM User Guide . When you create the IAM OIDC provider, you specify the following: The URL of the OIDC identity provider (IdP) to trust A list of client IDs (also known as audiences) that identify the application or applications allowed to authenticate using the OIDC provider A list of tags that are attached to the specified IAM OIDC provider A list of thumbprints of one or more server certificates that the IdP uses You get all of this information from the OIDC IdP you want to use to access Amazon Web Services. Amazon Web Services secures communication with OIDC identity providers (IdPs) using our library of trusted root certificate authorities (CAs) to verify the JSON Web Key Set (JWKS) endpoint's TLS certificate. If your OIDC IdP relies on a certificate that is not signed by one of these trusted CAs, only then we secure communication using the thumbprints set in the IdP's configuration. The trust for the OIDC provider is derived from the IAM provider that this operation creates. Therefore, it is best to limit access to the CreateOpenIDConnectProvider operation to highly privileged users.

## Input Shape: CreateOpenIDConnectProviderRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientIDList | Any  # complex shape |  | Provides a list of client IDs, also known as audiences. When a mobile or web app registers with an OpenID Connect provid |
| Tags | Any  # complex shape |  | A list of tags that you want to attach to the new IAM OpenID Connect (OIDC) provider. Each tag consists of a key name an |
| ThumbprintList | Any  # complex shape |  | A list of server certificate thumbprints for the OpenID Connect (OIDC) identity provider's server certificates. Typicall |
| Url | Any  # complex shape | ✓ | The URL of the identity provider. The URL must begin with https:// and should correspond to the iss claim in the provide |

## Output Shape: CreateOpenIDConnectProviderResponse

- **OpenIDConnectProviderArn** (Any  # complex shape): The Amazon Resource Name (ARN) of the new IAM OpenID Connect provider that is created. For more information, see OpenIDC
- **Tags** (Any  # complex shape): A list of tags that are attached to the new IAM OIDC provider. The returned list of tags is sorted by tag key. For more 

## Errors
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
- **EntityAlreadyExistsException**: The request was rejected because it attempted to create a resource that already exists.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **ConcurrentModificationException**: The request was rejected because multiple requests to change this object were submitted simultaneously. Wait a few minutes and submit your request again.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.
- **OpenIdIdpCommunicationErrorException**: The request failed because IAM cannot connect to the OpenID Connect identity provider URL.

## Implementation

```speclang
def create_open_id_connect_provider(store, request: dict) -> dict:
    """Creates an IAM entity to describe an identity provider (IdP) that supports OpenID Connect (OIDC) . The OIDC provider that you create with this operation can be used as a principal in a role's trust po"""
    url = request.get("Url", "").strip() if isinstance(request.get("Url"), str) else request.get("Url")
    if not url:
        raise ValidationException("Url is required")

    if store.open_id_connect_providers(url):
        raise ResourceInUseException(f"Resource url already exists")

    record = {
        "Url": url,
        "ClientIDList": client_id_list,
        "ThumbprintList": thumbprint_list,
        "Tags": tags,
    }

    store.open_id_connect_providers(url, record)

    return {
        "OpenIDConnectProviderArn": record.get("OpenIDConnectProviderArn", {}),
        "Tags": record.get("Tags", {}),
    }
```
