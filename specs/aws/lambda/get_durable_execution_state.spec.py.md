---
id: "@specs/aws/lambda/get_durable_execution_state"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_GetDurableExecutionState"
---

# GetDurableExecutionState

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/get_durable_execution_state
> **spec:implements:** @kind:operation GetDurableExecutionState
> **AWS Protocol:** rest-json
> **HTTP:** GET /2025-12-01/durable-executions/{DurableExecutionArn}/state
> **@ref:** specs/aws/lambda/docs/API_GetDurableExecutionState.spec.md

Retrieves the current execution state required for the replay process during durable function execution. This API is used by the Lambda durable functions SDK to get state information needed for replay. You typically don't need to call this API directly as the SDK handles state management automatically. The response contains operations ordered by start sequence number in ascending order. Completed operations with children don't include child operation details since they don't need to be replayed.

## Input Shape: GetDurableExecutionStateRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CheckpointToken | Any  # complex shape | ✓ | A checkpoint token that identifies the current state of the execution. This token is provided by the Lambda runtime and  |
| DurableExecutionArn | Any  # complex shape | ✓ | The Amazon Resource Name (ARN) of the durable execution. |
| Marker | str |  | If NextMarker was returned from a previous request, use this value to retrieve the next page of operations. Each paginat |
| MaxItems | Any  # complex shape |  | The maximum number of operations to return per call. You can use Marker to retrieve additional pages of results. The def |

## Output Shape: GetDurableExecutionStateResponse

- **NextMarker** (str): If present, indicates that more operations are available. Use this value as the Marker parameter in a subsequent request
- **Operations** (Any  # complex shape): An array of operations that represent the current state of the durable execution. Operations are ordered by their start 

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ServiceException**: The Lambda service encountered an internal error.

## Implementation

```speclang
def get_durable_execution_state(store, request: dict) -> dict:
    """Retrieves the current execution state required for the replay process during durable function execution. This API is used by the Lambda durable functions SDK to get state information needed for replay"""
    checkpoint_token = request.get("CheckpointToken", "").strip() if isinstance(request.get("CheckpointToken"), str) else request.get("CheckpointToken")
    if not checkpoint_token:
        raise ValidationException("CheckpointToken is required")
    durable_execution_arn = request.get("DurableExecutionArn", "").strip() if isinstance(request.get("DurableExecutionArn"), str) else request.get("DurableExecutionArn")
    if not durable_execution_arn:
        raise ValidationException("DurableExecutionArn is required")

    resource = store.durable_execution_states(durable_execution_arn)
    if not resource:
        raise ResourceNotFoundException(f"Resource durable_execution_arn not found")
    return {"DurableExecutionArn": durable_execution_arn, **resource}
```
