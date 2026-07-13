---
id: "@specs/aws/lambda/delete_provisioned_concurrency_config"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_DeleteProvisionedConcurrencyConfig"
---

# DeleteProvisionedConcurrencyConfig

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/delete_provisioned_concurrency_config
> **spec:implements:** @kind:operation DeleteProvisionedConcurrencyConfig
> **AWS Protocol:** rest-json
> **HTTP:** DELETE /2019-09-30/functions/{FunctionName}/provisioned-concurrency
> **@ref:** specs/aws/lambda/docs/API_DeleteProvisionedConcurrencyConfig.spec.md

Deletes the provisioned concurrency configuration for a function.

## Input Shape: DeleteProvisionedConcurrencyConfigRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| FunctionName | Any  # complex shape | ✓ | The name or ARN of the Lambda function. Name formats Function name – my-function . Function ARN – arn:aws:lambda:us-west |
| Qualifier | Any  # complex shape | ✓ | The version number or alias name. |

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ResourceConflictException**: The resource already exists, or another operation is in progress.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ResourceNotFoundException**: The resource specified in the request does not exist.

## Implementation

```speclang
def delete_provisioned_concurrency_config(store, request: dict) -> dict:
    """Deletes the provisioned concurrency configuration for a function."""
    function_name = request.get("FunctionName", "").strip() if isinstance(request.get("FunctionName"), str) else request.get("FunctionName")
    qualifier = request.get("Qualifier", "").strip() if isinstance(request.get("Qualifier"), str) else request.get("Qualifier")

    if not store.provisioned_concurrency_configs(function_name):
        raise ResourceNotFoundException(f"Resource function_name not found")
    store.delete_provisioned_concurrency_configs(function_name)
    return {}
```
