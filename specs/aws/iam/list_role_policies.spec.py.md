---
id: "@specs/aws/iam/list_role_policies"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_ListRolePolicies"
---

# ListRolePolicies

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/list_role_policies
> **spec:implements:** @kind:operation ListRolePolicies
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_ListRolePolicies.spec.md

Lists the names of the inline policies that are embedded in the specified IAM role. An IAM role can also have managed policies attached to it. To list the managed policies that are attached to a role, use ListAttachedRolePolicies . For more information about policies, see Managed policies and inline policies in the IAM User Guide . You can paginate the results using the MaxItems and Marker parameters. If there are no inline policies embedded with the specified role, the operation returns an empty list.

## Input Shape: ListRolePoliciesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Marker | Any  # complex shape |  | Use this parameter only when paginating results and only after you receive a response indicating that the results are tr |
| MaxItems | Any  # complex shape |  | Use this only when paginating results to indicate the maximum number of items you want in the response. If additional it |
| RoleName | Any  # complex shape | ✓ | The name of the role to list policies for. This parameter allows (through its regex pattern ) a string of characters con |

## Output Shape: ListRolePoliciesResponse

- **IsTruncated** (Any  # complex shape): A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent 
- **Marker** (Any  # complex shape): When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequen
- **PolicyNames** (Any  # complex shape): A list of policy names.

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def list_role_policies(store, request: dict) -> dict:
    """Lists the names of the inline policies that are embedded in the specified IAM role. An IAM role can also have managed policies attached to it. To list the managed policies that are attached to a role,"""
    role_name = request.get("RoleName", "").strip() if isinstance(request.get("RoleName"), str) else request.get("RoleName")
    if not role_name:
        raise ValidationException("RoleName is required")

    items = store.list_role_policiess()
    return {"PolicyNames": list(items.values())}
```
