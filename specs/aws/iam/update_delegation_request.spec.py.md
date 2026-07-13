---
id: "@specs/aws/iam/update_delegation_request"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_UpdateDelegationRequest"
---

# UpdateDelegationRequest

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/update_delegation_request
> **spec:implements:** @kind:operation UpdateDelegationRequest
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_UpdateDelegationRequest.spec.md

Updates an existing delegation request with additional information. When the delegation request is updated, it reaches the PENDING_APPROVAL state. Once a delegation request has an owner, that owner gets a default permission to update the delegation request. For more details, see Managing Permissions for Delegation Requests .

## Input Shape: UpdateDelegationRequestRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DelegationRequestId | Any  # complex shape | ✓ | The unique identifier of the delegation request to update. |
| Notes | Any  # complex shape |  | Additional notes or comments to add to the delegation request. |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.
- **ConcurrentModificationException**: The request was rejected because multiple requests to change this object were submitted simultaneously. Wait a few minutes and submit your request again.
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.

## Implementation

```speclang
def update_delegation_request(store, request: dict) -> dict:
    """Updates an existing delegation request with additional information. When the delegation request is updated, it reaches the PENDING_APPROVAL state. Once a delegation request has an owner, that owner ge"""
    delegation_request_id = request.get("DelegationRequestId", "").strip() if isinstance(request.get("DelegationRequestId"), str) else request.get("DelegationRequestId")
    if not delegation_request_id:
        raise ValidationException("DelegationRequestId is required")

    resource = store.delegation_requests(delegation_request_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource delegation_request_id not found")

    # Update mutable fields
    if "Notes" in request:
        resource["Notes"] = notes

    store.delegation_requests(delegation_request_id, resource)
    return resource
```
