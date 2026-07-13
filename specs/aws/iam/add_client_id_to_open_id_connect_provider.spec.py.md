---
id: "@specs/aws/iam/add_client_id_to_open_id_connect_provider"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_AddClientIDToOpenIDConnectProvider"
---

# AddClientIDToOpenIDConnectProvider

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/add_client_id_to_open_id_connect_provider
> **spec:implements:** @kind:operation AddClientIDToOpenIDConnectProvider
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_AddClientIDToOpenIDConnectProvider.spec.md

Adds a new client ID (also known as audience) to the list of client IDs already registered for the specified IAM OpenID Connect (OIDC) provider resource. This operation is idempotent; it does not fail or return an error if you add an existing client ID to the provider.

## Input Shape: AddClientIDToOpenIDConnectProviderRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientID | Any  # complex shape | ✓ | The client ID (also known as audience) to add to the IAM OpenID Connect provider resource. |
| OpenIDConnectProviderArn | Any  # complex shape | ✓ | The Amazon Resource Name (ARN) of the IAM OpenID Connect (OIDC) provider resource to add the client ID to. You can get a |

## Errors
- **ConcurrentModificationException**: The request was rejected because multiple requests to change this object were submitted simultaneously. Wait a few minutes and submit your request again.
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def add_client_id_to_open_id_connect_provider(store, request: dict) -> dict:
    """Adds a new client ID (also known as audience) to the list of client IDs already registered for the specified IAM OpenID Connect (OIDC) provider resource. This operation is idempotent; it does not fail"""
    client_id = request.get("ClientID", "").strip() if isinstance(request.get("ClientID"), str) else request.get("ClientID")
    if not client_id:
        raise ValidationException("ClientID is required")
    open_id_connect_provider_arn = request.get("OpenIDConnectProviderArn", "").strip() if isinstance(request.get("OpenIDConnectProviderArn"), str) else request.get("OpenIDConnectProviderArn")
    if not open_id_connect_provider_arn:
        raise ValidationException("OpenIDConnectProviderArn is required")

    if store.client_id_to_open_id_connect_providers(client_id):
        raise ResourceInUseException(f"Resource client_id already exists")

    record = {
        "OpenIDConnectProviderArn": open_id_connect_provider_arn,
        "ClientID": client_id,
    }

    store.client_id_to_open_id_connect_providers(client_id, record)

    return {
    }
```
