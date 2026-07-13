---
id: "@specs/aws/iam/associate_delegation_request"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_AssociateDelegationRequest"
---

# AssociateDelegationRequest

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/associate_delegation_request
> **spec:implements:** @kind:operation AssociateDelegationRequest
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_AssociateDelegationRequest.spec.md

Associates a delegation request with the current identity. If the partner that created the delegation request has specified the owner account during creation, only an identity from that owner account can call the AssociateDelegationRequest API for the specified delegation request. Once the AssociateDelegationRequest API call is successful, the ARN of the current calling identity will be stored as the ownerId of the request. If the partner that created the delegation request has not specified the owner account during creation, any caller from any account can call the AssociateDelegationRequest API for the delegation request. Once this API call is successful, the ARN of the current calling identity will be stored as the ownerId and the Amazon Web Services account ID of the current calling identity will be stored as the ownerAccount of the request. For more details, see Managing Permissions for Delegation Requests .

## Input Shape: AssociateDelegationRequestRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DelegationRequestId | Any  # complex shape | ✓ | The unique identifier of the delegation request to associate. |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.
- **ConcurrentModificationException**: The request was rejected because multiple requests to change this object were submitted simultaneously. Wait a few minutes and submit your request again.
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.

## Implementation

```speclang
def associate_delegation_request(store, request: dict) -> dict:
    """Associates a delegation request with the current identity. If the partner that created the delegation request has specified the owner account during creation, only an identity from that owner account """
    delegation_request_id = request.get("DelegationRequestId", "").strip() if isinstance(request.get("DelegationRequestId"), str) else request.get("DelegationRequestId")
    if not delegation_request_id:
        raise ValidationException("DelegationRequestId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AssociateDelegationRequest", request)
```
