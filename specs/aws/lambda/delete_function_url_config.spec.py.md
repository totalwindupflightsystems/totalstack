---
id: "@specs/aws/lambda/delete_function_url_config"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_DeleteFunctionUrlConfig"
---

# DeleteFunctionUrlConfig

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/delete_function_url_config
> **spec:implements:** @kind:operation DeleteFunctionUrlConfig
> **AWS Protocol:** rest-json
> **HTTP:** DELETE /2021-10-31/functions/{FunctionName}/url
> **@ref:** specs/aws/lambda/docs/API_DeleteFunctionUrlConfig.spec.md

Deletes a Lambda function URL. When you delete a function URL, you can't recover it. Creating a new function URL results in a different URL address.

## Input Shape: DeleteFunctionUrlConfigRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| FunctionName | Any  # complex shape | ✓ | The name or ARN of the Lambda function. Name formats Function name – my-function . Function ARN – arn:aws:lambda:us-west |
| Qualifier | Any  # complex shape |  | The alias name. |

## Errors
- **ResourceConflictException**: The resource already exists, or another operation is in progress.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ResourceNotFoundException**: The resource specified in the request does not exist.

## Implementation

```speclang
def delete_function_url_config(store, request: dict) -> dict:
    """Deletes a Lambda function URL. When you delete a function URL, you can't recover it. Creating a new function URL results in a different URL address."""
    function_name = request.get("FunctionName", "").strip() if isinstance(request.get("FunctionName"), str) else request.get("FunctionName")

    if not store.function_url_configs(function_name):
        raise ResourceNotFoundException(f"Resource function_name not found")
    store.delete_function_url_configs(function_name)
    return {}
```
