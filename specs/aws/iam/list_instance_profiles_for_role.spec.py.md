---
id: "@specs/aws/iam/list_instance_profiles_for_role"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_ListInstanceProfilesForRole"
---

# ListInstanceProfilesForRole

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/list_instance_profiles_for_role
> **spec:implements:** @kind:operation ListInstanceProfilesForRole
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_ListInstanceProfilesForRole.spec.md

Lists the instance profiles that have the specified associated IAM role. If there are none, the operation returns an empty list. For more information about instance profiles, go to Using instance profiles in the IAM User Guide . You can paginate the results using the MaxItems and Marker parameters.

## Input Shape: ListInstanceProfilesForRoleRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Marker | Any  # complex shape |  | Use this parameter only when paginating results and only after you receive a response indicating that the results are tr |
| MaxItems | Any  # complex shape |  | Use this only when paginating results to indicate the maximum number of items you want in the response. If additional it |
| RoleName | Any  # complex shape | ✓ | The name of the role to list instance profiles for. This parameter allows (through its regex pattern ) a string of chara |

## Output Shape: ListInstanceProfilesForRoleResponse

- **InstanceProfiles** (Any  # complex shape): A list of instance profiles.
- **IsTruncated** (Any  # complex shape): A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent 
- **Marker** (Any  # complex shape): When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequen

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def list_instance_profiles_for_role(store, request: dict) -> dict:
    """Lists the instance profiles that have the specified associated IAM role. If there are none, the operation returns an empty list. For more information about instance profiles, go to Using instance prof"""
    role_name = request.get("RoleName", "").strip() if isinstance(request.get("RoleName"), str) else request.get("RoleName")
    if not role_name:
        raise ValidationException("RoleName is required")

    items = store.list_instance_profiles_for_roles()
    return {"InstanceProfiles": list(items.values())}
```
