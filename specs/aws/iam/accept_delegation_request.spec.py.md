---
id: "@specs/aws/iam/accept_delegation_request"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_AcceptDelegationRequest"
---

# AcceptDelegationRequest

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/accept_delegation_request
> **spec:implements:** @kind:operation AcceptDelegationRequest
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_AcceptDelegationRequest.spec.md

Accepts a delegation request, granting the requested temporary access. Once the delegation request is accepted, it is eligible to send the exchange token to the partner. The SendDelegationToken API has to be explicitly called to send the delegation token. At the time of acceptance, IAM records the details and the state of the identity that called this API. This is the identity that gets mapped to the delegated credential. An accepted request may be rejected before the exchange token is sent to the partner.

## Input Shape: AcceptDelegationRequestRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DelegationRequestId | Any  # complex shape | ✓ | The unique identifier of the delegation request to accept. |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.
- **ConcurrentModificationException**: The request was rejected because multiple requests to change this object were submitted simultaneously. Wait a few minutes and submit your request again.

## Implementation

```speclang
def accept_delegation_request(store, request: dict) -> dict:
    """Accepts a delegation request, granting the requested temporary access. Once the delegation request is accepted, it is eligible to send the exchange token to the partner. The SendDelegationToken API ha"""
    delegation_request_id = request.get("DelegationRequestId", "").strip() if isinstance(request.get("DelegationRequestId"), str) else request.get("DelegationRequestId")
    if not delegation_request_id:
        raise ValidationException("DelegationRequestId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AcceptDelegationRequest", request)
```
