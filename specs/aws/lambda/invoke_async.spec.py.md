---
id: "@specs/aws/lambda/invoke_async"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_InvokeAsync"
---

# InvokeAsync

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/invoke_async
> **spec:implements:** @kind:operation InvokeAsync
> **AWS Protocol:** rest-json
> **HTTP:** POST /2014-11-13/functions/{FunctionName}/invoke-async
> **@ref:** specs/aws/lambda/docs/API_InvokeAsync.spec.md

For asynchronous function invocation, use Invoke . Invokes a function asynchronously. The payload limit is 256KB. For larger payloads, for up to 1MB, use Invoke . If you do use the InvokeAsync action, note that it doesn't support the use of X-Ray active tracing. Trace ID is not propagated to the function, even if X-Ray active tracing is turned on.

## Input Shape: InvokeAsyncRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| FunctionName | Any  # complex shape | ✓ | The name or ARN of the Lambda function. Name formats Function name – my-function . Function ARN – arn:aws:lambda:us-west |
| InvokeArgs | Any  # complex shape | ✓ | The JSON that you want to provide to your Lambda function as input. |

## Output Shape: InvokeAsyncResponse

- **Status** (Any  # complex shape): The status code.

## Errors
- **InvalidRuntimeException**: The runtime or runtime version specified is not supported.
- **ResourceConflictException**: The resource already exists, or another operation is in progress.
- **ServiceException**: The Lambda service encountered an internal error.
- **ResourceNotFoundException**: The resource specified in the request does not exist.
- **InvalidRequestContentException**: The request body could not be parsed as JSON, or a request header is invalid. For example, the 'x-amzn-RequestId' header is not a valid UUID string.

## Implementation

```speclang
def invoke_async(store, request: dict) -> dict:
    """For asynchronous function invocation, use Invoke . Invokes a function asynchronously. The payload limit is 256KB. For larger payloads, for up to 1MB, use Invoke . If you do use the InvokeAsync action,"""
    function_name = request.get("FunctionName", "").strip() if isinstance(request.get("FunctionName"), str) else request.get("FunctionName")
    if not function_name:
        raise ValidationException("FunctionName is required")
    invoke_args = request.get("InvokeArgs", "").strip() if isinstance(request.get("InvokeArgs"), str) else request.get("InvokeArgs")
    if not invoke_args:
        raise ValidationException("InvokeArgs is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("InvokeAsync", request)
```
