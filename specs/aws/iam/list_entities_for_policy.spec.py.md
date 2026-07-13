---
id: "@specs/aws/iam/list_entities_for_policy"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_ListEntitiesForPolicy"
---

# ListEntitiesForPolicy

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/list_entities_for_policy
> **spec:implements:** @kind:operation ListEntitiesForPolicy
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_ListEntitiesForPolicy.spec.md

Lists all IAM users, groups, and roles that the specified managed policy is attached to. You can use the optional EntityFilter parameter to limit the results to a particular type of entity (users, groups, or roles). For example, to list only the roles that are attached to the specified policy, set EntityFilter to Role . You can paginate the results using the MaxItems and Marker parameters.

## Input Shape: ListEntitiesForPolicyRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| EntityFilter | Any  # complex shape |  | The entity type to use for filtering the results. For example, when EntityFilter is Role , only the roles that are attac |
| Marker | Any  # complex shape |  | Use this parameter only when paginating results and only after you receive a response indicating that the results are tr |
| MaxItems | Any  # complex shape |  | Use this only when paginating results to indicate the maximum number of items you want in the response. If additional it |
| PathPrefix | Any  # complex shape |  | The path prefix for filtering the results. This parameter is optional. If it is not included, it defaults to a slash (/) |
| PolicyArn | Any  # complex shape | ✓ | The Amazon Resource Name (ARN) of the IAM policy for which you want the versions. For more information about ARNs, see A |
| PolicyUsageFilter | Any  # complex shape |  | The policy usage method to use for filtering the results. To list only permissions policies, set PolicyUsageFilter to Pe |

## Output Shape: ListEntitiesForPolicyResponse

- **IsTruncated** (Any  # complex shape): A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent 
- **Marker** (Any  # complex shape): When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequen
- **PolicyGroups** (Any  # complex shape): A list of IAM groups that the policy is attached to.
- **PolicyRoles** (Any  # complex shape): A list of IAM roles that the policy is attached to.
- **PolicyUsers** (Any  # complex shape): A list of IAM users that the policy is attached to.

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def list_entities_for_policy(store, request: dict) -> dict:
    """Lists all IAM users, groups, and roles that the specified managed policy is attached to. You can use the optional EntityFilter parameter to limit the results to a particular type of entity (users, gro"""
    policy_arn = request.get("PolicyArn", "").strip() if isinstance(request.get("PolicyArn"), str) else request.get("PolicyArn")
    if not policy_arn:
        raise ValidationException("PolicyArn is required")

    items = store.list_entities_for_policys()
    return {"PolicyGroups": list(items.values())}
```
