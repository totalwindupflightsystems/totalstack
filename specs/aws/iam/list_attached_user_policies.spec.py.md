---
id: "@specs/aws/iam/list_attached_user_policies"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_ListAttachedUserPolicies"
---

# ListAttachedUserPolicies

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/list_attached_user_policies
> **spec:implements:** @kind:operation ListAttachedUserPolicies
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_ListAttachedUserPolicies.spec.md

Lists all managed policies that are attached to the specified IAM user. An IAM user can also have inline policies embedded with it. To list the inline policies for a user, use ListUserPolicies . For information about policies, see Managed policies and inline policies in the IAM User Guide . You can paginate the results using the MaxItems and Marker parameters. You can use the PathPrefix parameter to limit the list of policies to only those matching the specified path prefix. If there are no policies attached to the specified group (or none that match the specified path prefix), the operation returns an empty list.

## Input Shape: ListAttachedUserPoliciesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Marker | Any  # complex shape |  | Use this parameter only when paginating results and only after you receive a response indicating that the results are tr |
| MaxItems | Any  # complex shape |  | Use this only when paginating results to indicate the maximum number of items you want in the response. If additional it |
| PathPrefix | Any  # complex shape |  | The path prefix for filtering the results. This parameter is optional. If it is not included, it defaults to a slash (/) |
| UserName | Any  # complex shape | ✓ | The name (friendly name, not ARN) of the user to list attached policies for. This parameter allows (through its regex pa |

## Output Shape: ListAttachedUserPoliciesResponse

- **AttachedPolicies** (Any  # complex shape): A list of the attached policies.
- **IsTruncated** (Any  # complex shape): A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent 
- **Marker** (Any  # complex shape): When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequen

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def list_attached_user_policies(store, request: dict) -> dict:
    """Lists all managed policies that are attached to the specified IAM user. An IAM user can also have inline policies embedded with it. To list the inline policies for a user, use ListUserPolicies . For i"""
    user_name = request.get("UserName", "").strip() if isinstance(request.get("UserName"), str) else request.get("UserName")
    if not user_name:
        raise ValidationException("UserName is required")

    items = store.list_attached_user_policiess()
    return {"AttachedPolicies": list(items.values())}
```
