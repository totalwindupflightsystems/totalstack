---
id: "@specs/aws/iam/list_policies"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_ListPolicies"
---

# ListPolicies

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/list_policies
> **spec:implements:** @kind:operation ListPolicies
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_ListPolicies.spec.md

Lists all the managed policies that are available in your Amazon Web Services account, including your own customer-defined managed policies and all Amazon Web Services managed policies. You can filter the list of policies that is returned using the optional OnlyAttached , Scope , and PathPrefix parameters. For example, to list only the customer managed policies in your Amazon Web Services account, set Scope to Local . To list only Amazon Web Services managed policies, set Scope to AWS . You can paginate the results using the MaxItems and Marker parameters. For more information about managed policies, see Managed policies and inline policies in the IAM User Guide . IAM resource-listing operations return a subset of the available attributes for the resource. For example, this operation does not return tags, even though they are an attribute of the returned object. To view all of the information for a customer manged policy, see GetPolicy .

## Input Shape: ListPoliciesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Marker | Any  # complex shape |  | Use this parameter only when paginating results and only after you receive a response indicating that the results are tr |
| MaxItems | Any  # complex shape |  | Use this only when paginating results to indicate the maximum number of items you want in the response. If additional it |
| OnlyAttached | Any  # complex shape |  | A flag to filter the results to only the attached policies. When OnlyAttached is true , the returned list contains only  |
| PathPrefix | Any  # complex shape |  | The path prefix for filtering the results. This parameter is optional. If it is not included, it defaults to a slash (/) |
| PolicyUsageFilter | Any  # complex shape |  | The policy usage method to use for filtering the results. To list only permissions policies, set PolicyUsageFilter to Pe |
| Scope | Any  # complex shape |  | The scope to use for filtering the results. To list only Amazon Web Services managed policies, set Scope to AWS . To lis |

## Output Shape: ListPoliciesResponse

- **IsTruncated** (Any  # complex shape): A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent 
- **Marker** (Any  # complex shape): When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequen
- **Policies** (Any  # complex shape): A list of policies.

## Errors
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def list_policies(store, request: dict) -> dict:
    """Lists all the managed policies that are available in your Amazon Web Services account, including your own customer-defined managed policies and all Amazon Web Services managed policies. You can filter"""

    items = store.list_policiess()
    return {"Policies": list(items.values())}
```
