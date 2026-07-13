---
id: "@specs/aws/cloudformation/continue_update_rollback"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_ContinueUpdateRollback"
---

# ContinueUpdateRollback

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/continue_update_rollback
> **spec:implements:** @kind:operation ContinueUpdateRollback
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_ContinueUpdateRollback.spec.md

Continues rolling back a stack from UPDATE_ROLLBACK_FAILED to UPDATE_ROLLBACK_COMPLETE state. Depending on the cause of the failure, you can manually fix the error and continue the rollback. By continuing the rollback, you can return your stack to a working state (the UPDATE_ROLLBACK_COMPLETE state) and then try to update the stack again. A stack enters the UPDATE_ROLLBACK_FAILED state when CloudFormation can't roll back all changes after a failed stack update. For example, this might occur when a stack attempts to roll back to an old database that was deleted outside of CloudFormation. Because CloudFormation doesn't know the instance was deleted, it assumes the instance still exists and attempts to roll back to it, causing the update rollback to fail. For more information, see Continue rolling back an update in the CloudFormation User Guide . For information for troubleshooting a failed update rollback, see Update rollback failed .

## Input Shape: ContinueUpdateRollbackInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientRequestToken | Any  # complex shape |  | A unique identifier for this ContinueUpdateRollback request. Specify this token if you plan to retry requests so that Cl |
| ResourcesToSkip | Any  # complex shape |  | A list of the logical IDs of the resources that CloudFormation skips during the continue update rollback operation. You  |
| RoleARN | Any  # complex shape |  | The Amazon Resource Name (ARN) of an IAM role that CloudFormation assumes to roll back the stack. CloudFormation uses th |
| StackName | Any  # complex shape | ✓ | The name or the unique ID of the stack that you want to continue rolling back. Don't specify the name of a nested stack  |

## Output Shape: ContinueUpdateRollbackOutput


## Errors
- **TokenAlreadyExistsException**: A client request token already exists.

## Implementation

```speclang
def continue_update_rollback(store, request: dict) -> dict:
    """Continues rolling back a stack from UPDATE_ROLLBACK_FAILED to UPDATE_ROLLBACK_COMPLETE state. Depending on the cause of the failure, you can manually fix the error and continue the rollback. By contin"""
    stack_name = request.get("StackName", "").strip() if isinstance(request.get("StackName"), str) else request.get("StackName")
    if not stack_name:
        raise ValidationException("StackName is required")

    resource = store.continue_update_rollbacks(stack_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource stack_name not found")

    # Update mutable fields
    if "RoleARN" in request:
        resource["RoleARN"] = role_arn
    if "ResourcesToSkip" in request:
        resource["ResourcesToSkip"] = resources_to_skip
    if "ClientRequestToken" in request:
        resource["ClientRequestToken"] = client_request_token

    store.continue_update_rollbacks(stack_name, resource)
    return resource
```
