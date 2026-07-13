---
id: "@specs/aws/cloudformation/delete_stack"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_DeleteStack"
---

# DeleteStack

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/delete_stack
> **spec:implements:** @kind:operation DeleteStack
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_DeleteStack.spec.md

Deletes a specified stack. Once the call completes successfully, stack deletion starts. Deleted stacks don't show up in the DescribeStacks operation if the deletion has been completed successfully. For more information about deleting a stack, see Delete a stack from the CloudFormation console in the CloudFormation User Guide .

## Input Shape: DeleteStackInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientRequestToken | Any  # complex shape |  | A unique identifier for this DeleteStack request. Specify this token if you plan to retry requests so that CloudFormatio |
| DeletionMode | Any  # complex shape |  | Specifies the deletion mode for the stack. Possible values are: STANDARD - Use the standard behavior. Specifying this va |
| RetainResources | Any  # complex shape |  | For stacks in the DELETE_FAILED state, a list of resource logical IDs that are associated with the resources you want to |
| RoleARN | Any  # complex shape |  | The Amazon Resource Name (ARN) of an IAM role that CloudFormation assumes to delete the stack. CloudFormation uses the r |
| StackName | Any  # complex shape | ✓ | The name or the unique stack ID that's associated with the stack. |

## Errors
- **TokenAlreadyExistsException**: A client request token already exists.

## Implementation

```speclang
def delete_stack(store, request: dict) -> dict:
    """Deletes a specified stack. Once the call completes successfully, stack deletion starts. Deleted stacks don't show up in the DescribeStacks operation if the deletion has been completed successfully. Fo"""
    stack_name = request.get("StackName", "").strip() if isinstance(request.get("StackName"), str) else request.get("StackName")

    if not store.stacks(stack_name):
        raise ResourceNotFoundException(f"Resource stack_name not found")
    store.delete_stacks(stack_name)
    return {}
```
