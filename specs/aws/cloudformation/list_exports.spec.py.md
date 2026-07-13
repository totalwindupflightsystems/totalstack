---
id: "@specs/aws/cloudformation/list_exports"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_ListExports"
---

# ListExports

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/list_exports
> **spec:implements:** @kind:operation ListExports
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_ListExports.spec.md

Lists all exported output values in the account and Region in which you call this action. Use this action to see the exported output values that you can import into other stacks. To import values, use the Fn::ImportValue function. For more information, see Get exported outputs from a deployed CloudFormation stack .

## Input Shape: ListExportsInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| NextToken | Any  # complex shape |  | The token for the next set of items to return. (You received this token from a previous call.) |

## Output Shape: ListExportsOutput

- **Exports** (Any  # complex shape): The output for the ListExports action.
- **NextToken** (Any  # complex shape): If the output exceeds 100 exported output values, a string that identifies the next page of exports. If there is no addi

## Implementation

```speclang
def list_exports(store, request: dict) -> dict:
    """Lists all exported output values in the account and Region in which you call this action. Use this action to see the exported output values that you can import into other stacks. To import values, use"""

    items = store.list_exportss()
    return {"Exports": list(items.values())}
```
