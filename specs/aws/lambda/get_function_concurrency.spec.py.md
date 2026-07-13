---
id: "@specs/aws/lambda/get_function_concurrency"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_GetFunctionConcurrency"
---

# GetFunctionConcurrency

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/get_function_concurrency
> **spec:implements:** @kind:operation GetFunctionConcurrency
> **AWS Protocol:** rest-json
> **HTTP:** GET /2019-09-30/functions/{FunctionName}/concurrency
> **@ref:** specs/aws/lambda/docs/API_GetFunctionConcurrency.spec.md

Returns details about the reserved concurrency configuration for a function. To set a concurrency limit for a function, use PutFunctionConcurrency .

## Input Shape: GetFunctionConcurrencyRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| FunctionName | Any  # complex shape | ✓ | The name or ARN of the Lambda function. Name formats Function name – my-function . Function ARN – arn:aws:lambda:us-west |

## Output Shape: GetFunctionConcurrencyResponse

- **ReservedConcurrentExecutions** (Any  # complex shape): The number of simultaneous executions that are reserved for the function.

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ResourceNotFoundException**: The resource specified in the request does not exist.

## Implementation

```speclang
def get_function_concurrency(store, request: dict) -> dict:
    """Returns details about the reserved concurrency configuration for a function. To set a concurrency limit for a function, use PutFunctionConcurrency ."""
    function_name = request.get("FunctionName", "").strip() if isinstance(request.get("FunctionName"), str) else request.get("FunctionName")
    if not function_name:
        raise ValidationException("FunctionName is required")

    resource = store.function_concurrencys(function_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource function_name not found")
    return {"FunctionName": function_name, **resource}
```
