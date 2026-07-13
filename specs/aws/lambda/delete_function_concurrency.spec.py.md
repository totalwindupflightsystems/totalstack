---
id: "@specs/aws/lambda/delete_function_concurrency"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_DeleteFunctionConcurrency"
---

# DeleteFunctionConcurrency

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/delete_function_concurrency
> **spec:implements:** @kind:operation DeleteFunctionConcurrency
> **AWS Protocol:** rest-json
> **HTTP:** DELETE /2017-10-31/functions/{FunctionName}/concurrency
> **@ref:** specs/aws/lambda/docs/API_DeleteFunctionConcurrency.spec.md

Removes a concurrent execution limit from a function.

## Input Shape: DeleteFunctionConcurrencyRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| FunctionName | Any  # complex shape | ✓ | The name or ARN of the Lambda function. Name formats Function name – my-function . Function ARN – arn:aws:lambda:us-west |

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ResourceConflictException**: The resource already exists, or another operation is in progress.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ResourceNotFoundException**: The resource specified in the request does not exist.

## Implementation

```speclang
def delete_function_concurrency(store, request: dict) -> dict:
    """Removes a concurrent execution limit from a function."""
    function_name = request.get("FunctionName", "").strip() if isinstance(request.get("FunctionName"), str) else request.get("FunctionName")

    if not store.function_concurrencys(function_name):
        raise ResourceNotFoundException(f"Resource function_name not found")
    store.delete_function_concurrencys(function_name)
    return {}
```
