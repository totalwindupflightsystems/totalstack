---
id: "@specs/aws/iam/list_roles"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_ListRoles"
---

# ListRoles

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/list_roles
> **spec:implements:** @kind:operation ListRoles
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_ListRoles.spec.md

Lists the IAM roles that have the specified path prefix. If there are none, the operation returns an empty list. For more information about roles, see IAM roles in the IAM User Guide . IAM resource-listing operations return a subset of the available attributes for the resource. This operation does not return the following attributes, even though they are an attribute of the returned object: PermissionsBoundary RoleLastUsed Tags To view all of the information for a role, see GetRole . You can paginate the results using the MaxItems and Marker parameters.

## Input Shape: ListRolesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Marker | Any  # complex shape |  | Use this parameter only when paginating results and only after you receive a response indicating that the results are tr |
| MaxItems | Any  # complex shape |  | Use this only when paginating results to indicate the maximum number of items you want in the response. If additional it |
| PathPrefix | Any  # complex shape |  | The path prefix for filtering the results. For example, the prefix /application_abc/component_xyz/ gets all roles whose  |

## Output Shape: ListRolesResponse

- **IsTruncated** (Any  # complex shape): A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent 
- **Marker** (Any  # complex shape): When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequen
- **Roles** (Any  # complex shape): A list of roles.

## Errors
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def list_roles(store, request: dict) -> dict:
    """Lists the IAM roles that have the specified path prefix. If there are none, the operation returns an empty list. For more information about roles, see IAM roles in the IAM User Guide . IAM resource-li"""

    items = store.list_roless()
    return {"Roles": list(items.values())}
```
