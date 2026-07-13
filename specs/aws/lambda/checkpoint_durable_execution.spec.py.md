---
id: "@specs/aws/lambda/checkpoint_durable_execution"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_CheckpointDurableExecution"
---

# CheckpointDurableExecution

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/checkpoint_durable_execution
> **spec:implements:** @kind:operation CheckpointDurableExecution
> **AWS Protocol:** rest-json
> **HTTP:** POST /2025-12-01/durable-executions/{DurableExecutionArn}/checkpoint
> **@ref:** specs/aws/lambda/docs/API_CheckpointDurableExecution.spec.md

Saves the progress of a durable function execution during runtime. This API is used by the Lambda durable functions SDK to checkpoint completed steps and schedule asynchronous operations. You typically don't need to call this API directly as the SDK handles checkpointing automatically. Each checkpoint operation consumes the current checkpoint token and returns a new one for the next checkpoint. This ensures that checkpoints are applied in the correct order and prevents duplicate or out-of-order state updates.

## Input Shape: CheckpointDurableExecutionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CheckpointToken | Any  # complex shape | ✓ | A unique token that identifies the current checkpoint state. This token is provided by the Lambda runtime and must be us |
| ClientToken | Any  # complex shape |  | An optional idempotency token to ensure that duplicate checkpoint requests are handled correctly. If provided, Lambda us |
| DurableExecutionArn | Any  # complex shape | ✓ | The Amazon Resource Name (ARN) of the durable execution. |
| Updates | Any  # complex shape |  | An array of state updates to apply during this checkpoint. Each update represents a change to the execution state, such  |

## Output Shape: CheckpointDurableExecutionResponse

- **CheckpointToken** (Any  # complex shape): A new checkpoint token to use for the next checkpoint operation. This token replaces the one provided in the request and
- **NewExecutionState** (Any  # complex shape): Updated execution state information that includes any changes that occurred since the last checkpoint, such as completed

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ServiceException**: The Lambda service encountered an internal error.

## Implementation

```speclang
def checkpoint_durable_execution(store, request: dict) -> dict:
    """Saves the progress of a durable function execution during runtime. This API is used by the Lambda durable functions SDK to checkpoint completed steps and schedule asynchronous operations. You typicall"""
    checkpoint_token = request.get("CheckpointToken", "").strip() if isinstance(request.get("CheckpointToken"), str) else request.get("CheckpointToken")
    if not checkpoint_token:
        raise ValidationException("CheckpointToken is required")
    durable_execution_arn = request.get("DurableExecutionArn", "").strip() if isinstance(request.get("DurableExecutionArn"), str) else request.get("DurableExecutionArn")
    if not durable_execution_arn:
        raise ValidationException("DurableExecutionArn is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("CheckpointDurableExecution", request)
```
