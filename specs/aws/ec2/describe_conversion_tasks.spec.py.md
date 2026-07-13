---
id: "@specs/aws/ec2/describe_conversion_tasks"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeConversionTasks"
---

# DescribeConversionTasks

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_conversion_tasks
> **spec:implements:** @kind:operation DescribeConversionTasks
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeConversionTasks.spec.md

Describes the specified conversion tasks or all your conversion tasks. For more information, see the VM Import/Export User Guide . For information about the import manifest referenced by this API action, see VM Import Manifest .

## Input Shape: DescribeConversionTasksRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ConversionTaskIds | list[Any  # complex shape] |  | The conversion task IDs. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: DescribeConversionTasksResult

- **ConversionTasks** (list[Any  # complex shape]): Information about the conversion tasks.

## Implementation

```speclang
def describe_conversion_tasks(store, request: dict) -> dict:
    """Describes the specified conversion tasks or all your conversion tasks. For more information, see the VM Import/Export User Guide . For information about the import manifest referenced by this API acti"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
