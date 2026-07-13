---
id: "@specs/aws/iam/get_group"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_GetGroup"
---

# GetGroup

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/get_group
> **spec:implements:** @kind:operation GetGroup
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_GetGroup.spec.md

Returns a list of IAM users that are in the specified IAM group. You can paginate the results using the MaxItems and Marker parameters.

## Input Shape: GetGroupRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| GroupName | Any  # complex shape | ✓ | The name of the group. This parameter allows (through its regex pattern ) a string of characters consisting of upper and |
| Marker | Any  # complex shape |  | Use this parameter only when paginating results and only after you receive a response indicating that the results are tr |
| MaxItems | Any  # complex shape |  | Use this only when paginating results to indicate the maximum number of items you want in the response. If additional it |

## Output Shape: GetGroupResponse

- **Group** (Any  # complex shape): A structure that contains details about the group.
- **IsTruncated** (Any  # complex shape): A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent 
- **Marker** (Any  # complex shape): When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequen
- **Users** (Any  # complex shape): A list of users in the group.

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def get_group(store, request: dict) -> dict:
    """Returns a list of IAM users that are in the specified IAM group. You can paginate the results using the MaxItems and Marker parameters."""
    group_name = request.get("GroupName", "").strip() if isinstance(request.get("GroupName"), str) else request.get("GroupName")
    if not group_name:
        raise ValidationException("GroupName is required")

    resource = store.groups(group_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource group_name not found")
    return {"GroupName": group_name, **resource}
```
