---
id: "@specs/aws/iam/get_delegation_request"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_GetDelegationRequest"
---

# GetDelegationRequest

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/get_delegation_request
> **spec:implements:** @kind:operation GetDelegationRequest
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_GetDelegationRequest.spec.md

Retrieves information about a specific delegation request. If a delegation request has no owner or owner account, GetDelegationRequest for that delegation request can be called by any account. If the owner account is assigned but there is no owner id, only identities within that owner account can call GetDelegationRequest for the delegation request. Once the delegation request is fully owned, the owner of the request gets a default permission to get that delegation request. For more details, see Managing Permissions for Delegation Requests .

## Input Shape: GetDelegationRequestRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DelegationPermissionCheck | Any  # complex shape |  | Specifies whether to perform a permission check for the delegation request. If set to true, the GetDelegationRequest API |
| DelegationRequestId | Any  # complex shape | ✓ | The unique identifier of the delegation request to retrieve. |

## Output Shape: GetDelegationRequestResponse

- **DelegationRequest** (Any  # complex shape): The delegation request object containing all details about the request.
- **PermissionCheckResult** (Any  # complex shape): The result of the permission check, indicating whether the caller has sufficient permissions to cover the requested perm
- **PermissionCheckStatus** (Any  # complex shape): The status of the permission check for the delegation request. This value indicates the status of the process to check w

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def get_delegation_request(store, request: dict) -> dict:
    """Retrieves information about a specific delegation request. If a delegation request has no owner or owner account, GetDelegationRequest for that delegation request can be called by any account. If the """
    delegation_request_id = request.get("DelegationRequestId", "").strip() if isinstance(request.get("DelegationRequestId"), str) else request.get("DelegationRequestId")
    if not delegation_request_id:
        raise ValidationException("DelegationRequestId is required")

    resource = store.delegation_requests(delegation_request_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource delegation_request_id not found")
    return {"DelegationRequestId": delegation_request_id, **resource}
```
