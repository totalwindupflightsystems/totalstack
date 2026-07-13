---
id: "@specs/aws/iam/list_user_policies"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_ListUserPolicies"
---

# ListUserPolicies

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/list_user_policies
> **spec:implements:** @kind:operation ListUserPolicies
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_ListUserPolicies.spec.md

Lists the names of the inline policies embedded in the specified IAM user. An IAM user can also have managed policies attached to it. To list the managed policies that are attached to a user, use ListAttachedUserPolicies . For more information about policies, see Managed policies and inline policies in the IAM User Guide . You can paginate the results using the MaxItems and Marker parameters. If there are no inline policies embedded with the specified user, the operation returns an empty list.

## Input Shape: ListUserPoliciesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Marker | Any  # complex shape |  | Use this parameter only when paginating results and only after you receive a response indicating that the results are tr |
| MaxItems | Any  # complex shape |  | Use this only when paginating results to indicate the maximum number of items you want in the response. If additional it |
| UserName | Any  # complex shape | ✓ | The name of the user to list policies for. This parameter allows (through its regex pattern ) a string of characters con |

## Output Shape: ListUserPoliciesResponse

- **IsTruncated** (Any  # complex shape): A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent 
- **Marker** (Any  # complex shape): When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequen
- **PolicyNames** (Any  # complex shape): A list of policy names.

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def list_user_policies(store, request: dict) -> dict:
    """Lists the names of the inline policies embedded in the specified IAM user. An IAM user can also have managed policies attached to it. To list the managed policies that are attached to a user, use List"""
    user_name = request.get("UserName", "").strip() if isinstance(request.get("UserName"), str) else request.get("UserName")
    if not user_name:
        raise ValidationException("UserName is required")

    items = store.list_user_policiess()
    return {"PolicyNames": list(items.values())}
```
