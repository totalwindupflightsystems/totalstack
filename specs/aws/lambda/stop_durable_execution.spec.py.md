---
id: "@specs/aws/lambda/stop_durable_execution"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_StopDurableExecution"
---

# StopDurableExecution

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/stop_durable_execution
> **spec:implements:** @kind:operation StopDurableExecution
> **AWS Protocol:** rest-json
> **HTTP:** POST /2025-12-01/durable-executions/{DurableExecutionArn}/stop
> **@ref:** specs/aws/lambda/docs/API_StopDurableExecution.spec.md

Stops a running durable execution . The execution transitions to STOPPED status and cannot be resumed. Any in-progress operations are terminated.

## Input Shape: StopDurableExecutionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DurableExecutionArn | Any  # complex shape | ✓ | The Amazon Resource Name (ARN) of the durable execution. |
| Error | Any  # complex shape |  | Optional error details explaining why the execution is being stopped. |

## Output Shape: StopDurableExecutionResponse

- **StopTimestamp** (Any  # complex shape): The timestamp when the execution was stopped (ISO 8601 format).

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ServiceException**: The Lambda service encountered an internal error.
- **ResourceNotFoundException**: The resource specified in the request does not exist.

## Implementation

```speclang
def stop_durable_execution(store, request: dict) -> dict:
    """Stops a running durable execution . The execution transitions to STOPPED status and cannot be resumed. Any in-progress operations are terminated."""
    durable_execution_arn = request.get("DurableExecutionArn", "").strip() if isinstance(request.get("DurableExecutionArn"), str) else request.get("DurableExecutionArn")

    if not store.durable_executions(durable_execution_arn):
        raise ResourceNotFoundException(f"Resource durable_execution_arn not found")
    store.delete_durable_executions(durable_execution_arn)
    return {}
```
