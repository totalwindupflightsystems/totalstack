---
id: "@specs/aws/iam/list_delegation_requests"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_ListDelegationRequests"
---

# ListDelegationRequests

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/list_delegation_requests
> **spec:implements:** @kind:operation ListDelegationRequests
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_ListDelegationRequests.spec.md

Lists delegation requests based on the specified criteria. If a delegation request has no owner, even if it is assigned to a specific account, it will not be part of the ListDelegationRequests output for that account. For more details, see Managing Permissions for Delegation Requests .

## Input Shape: ListDelegationRequestsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Marker | Any  # complex shape |  | Use this parameter only when paginating results and only after you receive a response indicating that the results are tr |
| MaxItems | Any  # complex shape |  | Use this only when paginating results to indicate the maximum number of items you want in the response. If additional it |
| OwnerId | Any  # complex shape |  | The owner ID to filter delegation requests by. |

## Output Shape: ListDelegationRequestsResponse

- **DelegationRequests** (Any  # complex shape): A list of delegation requests that match the specified criteria.
- **Marker** (Any  # complex shape): When isTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequen
- **isTruncated** (Any  # complex shape): A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent 

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.

## Implementation

```speclang
def list_delegation_requests(store, request: dict) -> dict:
    """Lists delegation requests based on the specified criteria. If a delegation request has no owner, even if it is assigned to a specific account, it will not be part of the ListDelegationRequests output """

    items = store.list_delegation_requestss()
    return {"DelegationRequests": list(items.values())}
```
