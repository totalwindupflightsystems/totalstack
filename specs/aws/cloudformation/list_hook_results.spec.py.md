---
id: "@specs/aws/cloudformation/list_hook_results"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_ListHookResults"
---

# ListHookResults

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/list_hook_results
> **spec:implements:** @kind:operation ListHookResults
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_ListHookResults.spec.md

Returns summaries of invoked Hooks. For more information, see View invocation summaries for CloudFormation Hooks in the CloudFormation Hooks User Guide . This operation supports the following parameter combinations: No parameters: Returns all Hook invocation summaries. TypeArn only: Returns summaries for a specific Hook. TypeArn and Status : Returns summaries for a specific Hook filtered by status. TargetId and TargetType : Returns summaries for a specific Hook invocation target.

## Input Shape: ListHookResultsInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| NextToken | Any  # complex shape |  | The token for the next set of items to return. (You received this token from a previous call.) |
| Status | Any  # complex shape |  | Filters results by the status of Hook invocations. Can only be used in combination with TypeArn . Valid values are: HOOK |
| TargetId | Any  # complex shape |  | Filters results by the unique identifier of the target the Hook was invoked against. For change sets, this is the change |
| TargetType | Any  # complex shape |  | Filters results by target type. Currently, only CHANGE_SET and CLOUD_CONTROL are supported filter options. Required when |
| TypeArn | Any  # complex shape |  | Filters results by the ARN of the Hook. Can be used alone or in combination with Status . |

## Output Shape: ListHookResultsOutput

- **HookResults** (Any  # complex shape): A list of HookResultSummary structures that provides the status and Hook status reason for each Hook invocation for the 
- **NextToken** (Any  # complex shape): Pagination token, null or empty if no more results.
- **TargetId** (Any  # complex shape): The unique identifier of the Hook invocation target.
- **TargetType** (Any  # complex shape): The target type.

## Errors
- **HookResultNotFoundException**: The specified target doesn't have any requested Hook invocations.

## Implementation

```speclang
def list_hook_results(store, request: dict) -> dict:
    """Returns summaries of invoked Hooks. For more information, see View invocation summaries for CloudFormation Hooks in the CloudFormation Hooks User Guide . This operation supports the following paramete"""

    items = store.list_hook_resultss()
    return {"HookResults": list(items.values())}
```
