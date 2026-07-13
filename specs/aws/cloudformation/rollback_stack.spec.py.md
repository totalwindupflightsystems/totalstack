---
id: "@specs/aws/cloudformation/rollback_stack"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_RollbackStack"
---

# RollbackStack

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/rollback_stack
> **spec:implements:** @kind:operation RollbackStack
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_RollbackStack.spec.md

When specifying RollbackStack , you preserve the state of previously provisioned resources when an operation fails. You can check the status of the stack through the DescribeStacks operation. Rolls back the specified stack to the last known stable state from CREATE_FAILED or UPDATE_FAILED stack statuses. This operation will delete a stack if it doesn't contain a last known stable state. A last known stable state includes any status in a *_COMPLETE . This includes the following stack statuses. CREATE_COMPLETE UPDATE_COMPLETE UPDATE_ROLLBACK_COMPLETE IMPORT_COMPLETE IMPORT_ROLLBACK_COMPLETE

## Input Shape: RollbackStackInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientRequestToken | Any  # complex shape |  | A unique identifier for this RollbackStack request. |
| RetainExceptOnCreate | Any  # complex shape |  | When set to true , newly created resources are deleted when the operation rolls back. This includes newly created resour |
| RoleARN | Any  # complex shape |  | The Amazon Resource Name (ARN) of an IAM role that CloudFormation assumes to rollback the stack. |
| StackName | Any  # complex shape | ✓ | The name that's associated with the stack. |

## Output Shape: RollbackStackOutput

- **OperationId** (Any  # complex shape): A unique identifier for this rollback operation that can be used to track the operation's progress and events.
- **StackId** (Any  # complex shape): Unique identifier of the stack.

## Errors
- **TokenAlreadyExistsException**: A client request token already exists.

## Implementation

```speclang
def rollback_stack(store, request: dict) -> dict:
    """When specifying RollbackStack , you preserve the state of previously provisioned resources when an operation fails. You can check the status of the stack through the DescribeStacks operation. Rolls ba"""
    stack_name = request.get("StackName", "").strip() if isinstance(request.get("StackName"), str) else request.get("StackName")
    if not stack_name:
        raise ValidationException("StackName is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("RollbackStack", request)
```
