---
id: "@specs/aws/lambda/put_function_recursion_config"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_PutFunctionRecursionConfig"
---

# PutFunctionRecursionConfig

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/put_function_recursion_config
> **spec:implements:** @kind:operation PutFunctionRecursionConfig
> **AWS Protocol:** rest-json
> **HTTP:** PUT /2024-08-31/functions/{FunctionName}/recursion-config
> **@ref:** specs/aws/lambda/docs/API_PutFunctionRecursionConfig.spec.md

Sets your function's recursive loop detection configuration. When you configure a Lambda function to output to the same service or resource that invokes the function, it's possible to create an infinite recursive loop. For example, a Lambda function might write a message to an Amazon Simple Queue Service (Amazon SQS) queue, which then invokes the same function. This invocation causes the function to write another message to the queue, which in turn invokes the function again. Lambda can detect certain types of recursive loops shortly after they occur. When Lambda detects a recursive loop and your function's recursive loop detection configuration is set to Terminate , it stops your function being invoked and notifies you.

## Input Shape: PutFunctionRecursionConfigRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| FunctionName | Any  # complex shape | ✓ | The name or ARN of the Lambda function. Name formats Function name – my-function . Function ARN – arn:aws:lambda:us-west |
| RecursiveLoop | Any  # complex shape | ✓ | If you set your function's recursive loop detection configuration to Allow , Lambda doesn't take any action when it dete |

## Output Shape: PutFunctionRecursionConfigResponse

- **RecursiveLoop** (Any  # complex shape): The status of your function's recursive loop detection configuration. When this value is set to Allow and Lambda detects

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ResourceConflictException**: The resource already exists, or another operation is in progress.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ResourceNotFoundException**: The resource specified in the request does not exist.

## Implementation

```speclang
def put_function_recursion_config(store, request: dict) -> dict:
    """Sets your function's recursive loop detection configuration. When you configure a Lambda function to output to the same service or resource that invokes the function, it's possible to create an infini"""
    function_name = request.get("FunctionName", "").strip() if isinstance(request.get("FunctionName"), str) else request.get("FunctionName")
    if not function_name:
        raise ValidationException("FunctionName is required")
    recursive_loop = request.get("RecursiveLoop", "").strip() if isinstance(request.get("RecursiveLoop"), str) else request.get("RecursiveLoop")
    if not recursive_loop:
        raise ValidationException("RecursiveLoop is required")

    if store.function_recursion_configs(function_name):
        raise ResourceInUseException(f"Resource function_name already exists")

    record = {
        "FunctionName": function_name,
        "RecursiveLoop": recursive_loop,
    }

    store.function_recursion_configs(function_name, record)

    return {
        "RecursiveLoop": record.get("RecursiveLoop", {}),
    }
```
