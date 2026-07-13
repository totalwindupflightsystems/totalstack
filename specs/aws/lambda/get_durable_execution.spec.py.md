---
id: "@specs/aws/lambda/get_durable_execution"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_GetDurableExecution"
---

# GetDurableExecution

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/get_durable_execution
> **spec:implements:** @kind:operation GetDurableExecution
> **AWS Protocol:** rest-json
> **HTTP:** GET /2025-12-01/durable-executions/{DurableExecutionArn}
> **@ref:** specs/aws/lambda/docs/API_GetDurableExecution.spec.md

Retrieves detailed information about a specific durable execution , including its current status, input payload, result or error information, and execution metadata such as start time and usage statistics.

## Input Shape: GetDurableExecutionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DurableExecutionArn | Any  # complex shape | ✓ | The Amazon Resource Name (ARN) of the durable execution. |

## Output Shape: GetDurableExecutionResponse

- **DurableExecutionArn** (Any  # complex shape): The Amazon Resource Name (ARN) of the durable execution.
- **DurableExecutionName** (Any  # complex shape): The name of the durable execution. This is either the name you provided when invoking the function, or a system-generate
- **EndTimestamp** (Any  # complex shape): The date and time when the durable execution ended, in Unix timestamp format. This field is only present if the executio
- **Error** (Any  # complex shape): Error information if the durable execution failed. This field is only present when the execution status is FAILED , TIME
- **FunctionArn** (Any  # complex shape): The Amazon Resource Name (ARN) of the Lambda function that was invoked to start this durable execution.
- **InputPayload** (Any  # complex shape): The JSON input payload that was provided when the durable execution was started. For asynchronous invocations, this is l
- **Result** (Any  # complex shape): The JSON result returned by the durable execution if it completed successfully. This field is only present when the exec
- **StartTimestamp** (Any  # complex shape): The date and time when the durable execution started, in Unix timestamp format.
- **Status** (Any  # complex shape): The current status of the durable execution. Valid values are RUNNING , SUCCEEDED , FAILED , TIMED_OUT , and STOPPED .
- **TraceHeader** (Any  # complex shape): The trace headers associated with the durable execution.
- **Version** (Any  # complex shape): The version of the Lambda function that was invoked for this durable execution. This ensures that all replays during the

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ServiceException**: The Lambda service encountered an internal error.
- **ResourceNotFoundException**: The resource specified in the request does not exist.

## Implementation

```speclang
def get_durable_execution(store, request: dict) -> dict:
    """Retrieves detailed information about a specific durable execution , including its current status, input payload, result or error information, and execution metadata such as start time and usage statis"""
    durable_execution_arn = request.get("DurableExecutionArn", "").strip() if isinstance(request.get("DurableExecutionArn"), str) else request.get("DurableExecutionArn")
    if not durable_execution_arn:
        raise ValidationException("DurableExecutionArn is required")

    resource = store.durable_executions(durable_execution_arn)
    if not resource:
        raise ResourceNotFoundException(f"Resource durable_execution_arn not found")
    return {"DurableExecutionArn": durable_execution_arn, **resource}
```
