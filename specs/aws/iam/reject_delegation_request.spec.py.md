---
id: "@specs/aws/iam/reject_delegation_request"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_RejectDelegationRequest"
---

# RejectDelegationRequest

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/reject_delegation_request
> **spec:implements:** @kind:operation RejectDelegationRequest
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_RejectDelegationRequest.spec.md

Rejects a delegation request, denying the requested temporary access. Once a request is rejected, it cannot be accepted or updated later. Rejected requests expire after 7 days. When rejecting a request, an optional explanation can be added using the Notes request parameter. For more details, see Managing Permissions for Delegation Requests .

## Input Shape: RejectDelegationRequestRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DelegationRequestId | Any  # complex shape | ✓ | The unique identifier of the delegation request to reject. |
| Notes | Any  # complex shape |  | Optional notes explaining the reason for rejecting the delegation request. |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.
- **ConcurrentModificationException**: The request was rejected because multiple requests to change this object were submitted simultaneously. Wait a few minutes and submit your request again.
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.

## Implementation

```speclang
def reject_delegation_request(store, request: dict) -> dict:
    """Rejects a delegation request, denying the requested temporary access. Once a request is rejected, it cannot be accepted or updated later. Rejected requests expire after 7 days. When rejecting a reques"""
    delegation_request_id = request.get("DelegationRequestId", "").strip() if isinstance(request.get("DelegationRequestId"), str) else request.get("DelegationRequestId")
    if not delegation_request_id:
        raise ValidationException("DelegationRequestId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("RejectDelegationRequest", request)
```
