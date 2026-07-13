---
id: "@specs/aws/cloudformation/list_imports"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_ListImports"
---

# ListImports

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/list_imports
> **spec:implements:** @kind:operation ListImports
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_ListImports.spec.md

Lists all stacks that are importing an exported output value. To modify or remove an exported output value, first use this action to see which stacks are using it. To see the exported output values in your account, see ListExports . For more information about importing an exported output value, see the Fn::ImportValue function.

## Input Shape: ListImportsInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ExportName | Any  # complex shape | ✓ | The name of the exported output value. CloudFormation returns the stack names that are importing this value. |
| NextToken | Any  # complex shape |  | The token for the next set of items to return. (You received this token from a previous call.) |

## Output Shape: ListImportsOutput

- **Imports** (Any  # complex shape): A list of stack names that are importing the specified exported output value.
- **NextToken** (Any  # complex shape): A string that identifies the next page of exports. If there is no additional page, this value is null.

## Implementation

```speclang
def list_imports(store, request: dict) -> dict:
    """Lists all stacks that are importing an exported output value. To modify or remove an exported output value, first use this action to see which stacks are using it. To see the exported output values in"""
    export_name = request.get("ExportName", "").strip() if isinstance(request.get("ExportName"), str) else request.get("ExportName")
    if not export_name:
        raise ValidationException("ExportName is required")

    items = store.list_importss()
    return {"Imports": list(items.values())}
```
