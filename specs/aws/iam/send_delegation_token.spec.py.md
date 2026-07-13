---
id: "@specs/aws/iam/send_delegation_token"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_SendDelegationToken"
---

# SendDelegationToken

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/send_delegation_token
> **spec:implements:** @kind:operation SendDelegationToken
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_SendDelegationToken.spec.md

Sends the exchange token for an accepted delegation request. The exchange token is sent to the partner via an asynchronous notification channel, established by the partner. The delegation request must be in the ACCEPTED state when calling this API. After the SendDelegationToken API call is successful, the request transitions to a FINALIZED state and cannot be rolled back. However, a user may reject an accepted request before the SendDelegationToken API is called. For more details, see Managing Permissions for Delegation Requests .

## Input Shape: SendDelegationTokenRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DelegationRequestId | Any  # complex shape | ✓ | The unique identifier of the delegation request for which to send the token. |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.
- **ConcurrentModificationException**: The request was rejected because multiple requests to change this object were submitted simultaneously. Wait a few minutes and submit your request again.
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.

## Implementation

```speclang
def send_delegation_token(store, request: dict) -> dict:
    """Sends the exchange token for an accepted delegation request. The exchange token is sent to the partner via an asynchronous notification channel, established by the partner. The delegation request must"""
    delegation_request_id = request.get("DelegationRequestId", "").strip() if isinstance(request.get("DelegationRequestId"), str) else request.get("DelegationRequestId")
    if not delegation_request_id:
        raise ValidationException("DelegationRequestId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("SendDelegationToken", request)
```
