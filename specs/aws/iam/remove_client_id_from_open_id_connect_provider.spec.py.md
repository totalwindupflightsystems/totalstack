---
id: "@specs/aws/iam/remove_client_id_from_open_id_connect_provider"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_RemoveClientIDFromOpenIDConnectProvider"
---

# RemoveClientIDFromOpenIDConnectProvider

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/remove_client_id_from_open_id_connect_provider
> **spec:implements:** @kind:operation RemoveClientIDFromOpenIDConnectProvider
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_RemoveClientIDFromOpenIDConnectProvider.spec.md

Removes the specified client ID (also known as audience) from the list of client IDs registered for the specified IAM OpenID Connect (OIDC) provider resource object. This operation is idempotent; it does not fail or return an error if you try to remove a client ID that does not exist.

## Input Shape: RemoveClientIDFromOpenIDConnectProviderRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientID | Any  # complex shape | ✓ | The client ID (also known as audience) to remove from the IAM OIDC provider resource. For more information about client  |
| OpenIDConnectProviderArn | Any  # complex shape | ✓ | The Amazon Resource Name (ARN) of the IAM OIDC provider resource to remove the client ID from. You can get a list of OID |

## Errors
- **ConcurrentModificationException**: The request was rejected because multiple requests to change this object were submitted simultaneously. Wait a few minutes and submit your request again.
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def remove_client_id_from_open_id_connect_provider(store, request: dict) -> dict:
    """Removes the specified client ID (also known as audience) from the list of client IDs registered for the specified IAM OpenID Connect (OIDC) provider resource object. This operation is idempotent; it d"""
    client_id = request.get("ClientID", "").strip() if isinstance(request.get("ClientID"), str) else request.get("ClientID")
    open_id_connect_provider_arn = request.get("OpenIDConnectProviderArn", "").strip() if isinstance(request.get("OpenIDConnectProviderArn"), str) else request.get("OpenIDConnectProviderArn")

    if not store.client_id_from_open_id_connect_providers(client_id):
        raise ResourceNotFoundException(f"Resource client_id not found")
    store.delete_client_id_from_open_id_connect_providers(client_id)
    return {}
```
