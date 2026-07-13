---
id: "@specs/aws/cloudformation/record_handler_progress"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_RecordHandlerProgress"
---

# RecordHandlerProgress

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/record_handler_progress
> **spec:implements:** @kind:operation RecordHandlerProgress
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_RecordHandlerProgress.spec.md

Reports progress of a resource handler to CloudFormation. Reserved for use by the CloudFormation CLI . Don't use this API in your code.

## Input Shape: RecordHandlerProgressInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| BearerToken | Any  # complex shape | ✓ | Reserved for use by the CloudFormation CLI . |
| ClientRequestToken | Any  # complex shape |  | Reserved for use by the CloudFormation CLI . |
| CurrentOperationStatus | Any  # complex shape |  | Reserved for use by the CloudFormation CLI . |
| ErrorCode | Any  # complex shape |  | Reserved for use by the CloudFormation CLI . |
| OperationStatus | Any  # complex shape | ✓ | Reserved for use by the CloudFormation CLI . |
| ResourceModel | Any  # complex shape |  | Reserved for use by the CloudFormation CLI . |
| StatusMessage | Any  # complex shape |  | Reserved for use by the CloudFormation CLI . |

## Output Shape: RecordHandlerProgressOutput


## Errors
- **InvalidStateTransitionException**: Error reserved for use by the CloudFormation CLI . CloudFormation doesn't return this error to users.
- **OperationStatusCheckFailedException**: Error reserved for use by the CloudFormation CLI . CloudFormation doesn't return this error to users.

## Implementation

```speclang
def record_handler_progress(store, request: dict) -> dict:
    """Reports progress of a resource handler to CloudFormation. Reserved for use by the CloudFormation CLI . Don't use this API in your code."""
    bearer_token = request.get("BearerToken", "").strip() if isinstance(request.get("BearerToken"), str) else request.get("BearerToken")
    if not bearer_token:
        raise ValidationException("BearerToken is required")
    operation_status = request.get("OperationStatus", "").strip() if isinstance(request.get("OperationStatus"), str) else request.get("OperationStatus")
    if not operation_status:
        raise ValidationException("OperationStatus is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("RecordHandlerProgress", request)
```
