---
id: "@specs/aws/iam/list_groups_for_user"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_ListGroupsForUser"
---

# ListGroupsForUser

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/list_groups_for_user
> **spec:implements:** @kind:operation ListGroupsForUser
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_ListGroupsForUser.spec.md

Lists the IAM groups that the specified IAM user belongs to. You can paginate the results using the MaxItems and Marker parameters.

## Input Shape: ListGroupsForUserRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Marker | Any  # complex shape |  | Use this parameter only when paginating results and only after you receive a response indicating that the results are tr |
| MaxItems | Any  # complex shape |  | Use this only when paginating results to indicate the maximum number of items you want in the response. If additional it |
| UserName | Any  # complex shape | ✓ | The name of the user to list groups for. This parameter allows (through its regex pattern ) a string of characters consi |

## Output Shape: ListGroupsForUserResponse

- **Groups** (Any  # complex shape): A list of groups.
- **IsTruncated** (Any  # complex shape): A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent 
- **Marker** (Any  # complex shape): When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequen

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def list_groups_for_user(store, request: dict) -> dict:
    """Lists the IAM groups that the specified IAM user belongs to. You can paginate the results using the MaxItems and Marker parameters."""
    user_name = request.get("UserName", "").strip() if isinstance(request.get("UserName"), str) else request.get("UserName")
    if not user_name:
        raise ValidationException("UserName is required")

    items = store.list_groups_for_users()
    return {"Groups": list(items.values())}
```
