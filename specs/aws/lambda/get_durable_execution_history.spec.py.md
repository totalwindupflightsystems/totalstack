---
id: "@specs/aws/lambda/get_durable_execution_history"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_GetDurableExecutionHistory"
---

# GetDurableExecutionHistory

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/get_durable_execution_history
> **spec:implements:** @kind:operation GetDurableExecutionHistory
> **AWS Protocol:** rest-json
> **HTTP:** GET /2025-12-01/durable-executions/{DurableExecutionArn}/history
> **@ref:** specs/aws/lambda/docs/API_GetDurableExecutionHistory.spec.md

Retrieves the execution history for a durable execution , showing all the steps, callbacks, and events that occurred during the execution. This provides a detailed audit trail of the execution's progress over time. The history is available while the execution is running and for a retention period after it completes (1-90 days, default 30 days). You can control whether to include execution data such as step results and callback payloads.

## Input Shape: GetDurableExecutionHistoryRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DurableExecutionArn | Any  # complex shape | ✓ | The Amazon Resource Name (ARN) of the durable execution. |
| IncludeExecutionData | Any  # complex shape |  | Specifies whether to include execution data such as step results and callback payloads in the history events. Set to tru |
| Marker | str |  | If NextMarker was returned from a previous request, use this value to retrieve the next page of results. Each pagination |
| MaxItems | Any  # complex shape |  | The maximum number of history events to return per call. You can use Marker to retrieve additional pages of results. The |
| ReverseOrder | Any  # complex shape |  | When set to true , returns the history events in reverse chronological order (newest first). By default, events are retu |

## Output Shape: GetDurableExecutionHistoryResponse

- **Events** (Any  # complex shape): An array of execution history events, ordered chronologically unless ReverseOrder is set to true . Each event represents
- **NextMarker** (str): If present, indicates that more history events are available. Use this value as the Marker parameter in a subsequent req

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ServiceException**: The Lambda service encountered an internal error.
- **ResourceNotFoundException**: The resource specified in the request does not exist.

## Implementation

```speclang
def get_durable_execution_history(store, request: dict) -> dict:
    """Retrieves the execution history for a durable execution , showing all the steps, callbacks, and events that occurred during the execution. This provides a detailed audit trail of the execution's progr"""
    durable_execution_arn = request.get("DurableExecutionArn", "").strip() if isinstance(request.get("DurableExecutionArn"), str) else request.get("DurableExecutionArn")
    if not durable_execution_arn:
        raise ValidationException("DurableExecutionArn is required")

    resource = store.durable_execution_historys(durable_execution_arn)
    if not resource:
        raise ResourceNotFoundException(f"Resource durable_execution_arn not found")
    return {"DurableExecutionArn": durable_execution_arn, **resource}
```
