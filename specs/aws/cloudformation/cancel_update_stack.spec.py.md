---
id: "@specs/aws/cloudformation/cancel_update_stack"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_CancelUpdateStack"
---

# CancelUpdateStack

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/cancel_update_stack
> **spec:implements:** @kind:operation CancelUpdateStack
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_CancelUpdateStack.spec.md

Cancels an update on the specified stack. If the call completes successfully, the stack rolls back the update and reverts to the previous stack configuration. You can cancel only stacks that are in the UPDATE_IN_PROGRESS state.

## Input Shape: CancelUpdateStackInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientRequestToken | Any  # complex shape |  | A unique identifier for this CancelUpdateStack request. Specify this token if you plan to retry requests so that CloudFo |
| StackName | Any  # complex shape | ✓ | If you don't pass a parameter to StackName , the API returns a response that describes all resources in the account. The |

## Errors
- **TokenAlreadyExistsException**: A client request token already exists.

## Implementation

```speclang
def cancel_update_stack(store, request: dict) -> dict:
    """Cancels an update on the specified stack. If the call completes successfully, the stack rolls back the update and reverts to the previous stack configuration. You can cancel only stacks that are in th"""
    stack_name = request.get("StackName", "").strip() if isinstance(request.get("StackName"), str) else request.get("StackName")

    if not store.update_stacks(stack_name):
        raise ResourceNotFoundException(f"Resource stack_name not found")
    store.delete_update_stacks(stack_name)
    return {}
```
