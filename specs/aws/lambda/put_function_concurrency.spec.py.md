---
id: "@specs/aws/lambda/put_function_concurrency"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_PutFunctionConcurrency"
---

# PutFunctionConcurrency

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/put_function_concurrency
> **spec:implements:** @kind:operation PutFunctionConcurrency
> **AWS Protocol:** rest-json
> **HTTP:** PUT /2017-10-31/functions/{FunctionName}/concurrency
> **@ref:** specs/aws/lambda/docs/API_PutFunctionConcurrency.spec.md

Sets the maximum number of simultaneous executions for a function, and reserves capacity for that concurrency level. Concurrency settings apply to the function as a whole, including all published versions and the unpublished version. Reserving concurrency both ensures that your function has capacity to process the specified number of events simultaneously, and prevents it from scaling beyond that level. Use GetFunction to see the current setting for a function. Use GetAccountSettings to see your Regional concurrency limit. You can reserve concurrency for as many functions as you like, as long as you leave at least 100 simultaneous executions unreserved for functions that aren't configured with a per-function limit. For more information, see Lambda function scaling .

## Input Shape: PutFunctionConcurrencyRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| FunctionName | Any  # complex shape | ✓ | The name or ARN of the Lambda function. Name formats Function name – my-function . Function ARN – arn:aws:lambda:us-west |
| ReservedConcurrentExecutions | Any  # complex shape | ✓ | The number of simultaneous executions to reserve for the function. |

## Output Shape: Concurrency

- **ReservedConcurrentExecutions** (Any  # complex shape): The number of concurrent executions that are reserved for this function. For more information, see Managing Lambda reser

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ResourceConflictException**: The resource already exists, or another operation is in progress.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ResourceNotFoundException**: The resource specified in the request does not exist.

## Implementation

```speclang
def put_function_concurrency(store, request: dict) -> dict:
    """Sets the maximum number of simultaneous executions for a function, and reserves capacity for that concurrency level. Concurrency settings apply to the function as a whole, including all published vers"""
    function_name = request.get("FunctionName", "").strip() if isinstance(request.get("FunctionName"), str) else request.get("FunctionName")
    if not function_name:
        raise ValidationException("FunctionName is required")
    reserved_concurrent_executions = request.get("ReservedConcurrentExecutions", "").strip() if isinstance(request.get("ReservedConcurrentExecutions"), str) else request.get("ReservedConcurrentExecutions")
    if not reserved_concurrent_executions:
        raise ValidationException("ReservedConcurrentExecutions is required")

    if store.function_concurrencys(function_name):
        raise ResourceInUseException(f"Resource function_name already exists")

    record = {
        "FunctionName": function_name,
        "ReservedConcurrentExecutions": reserved_concurrent_executions,
    }

    store.function_concurrencys(function_name, record)

    return {
        "ReservedConcurrentExecutions": record.get("ReservedConcurrentExecutions", {}),
    }
```
