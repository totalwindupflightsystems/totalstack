---
id: "@specs/aws/lambda/put_provisioned_concurrency_config"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_PutProvisionedConcurrencyConfig"
---

# PutProvisionedConcurrencyConfig

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/put_provisioned_concurrency_config
> **spec:implements:** @kind:operation PutProvisionedConcurrencyConfig
> **AWS Protocol:** rest-json
> **HTTP:** PUT /2019-09-30/functions/{FunctionName}/provisioned-concurrency
> **@ref:** specs/aws/lambda/docs/API_PutProvisionedConcurrencyConfig.spec.md

Adds a provisioned concurrency configuration to a function's alias or version.

## Input Shape: PutProvisionedConcurrencyConfigRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| FunctionName | Any  # complex shape | ✓ | The name or ARN of the Lambda function. Name formats Function name – my-function . Function ARN – arn:aws:lambda:us-west |
| ProvisionedConcurrentExecutions | Any  # complex shape | ✓ | The amount of provisioned concurrency to allocate for the version or alias. |
| Qualifier | Any  # complex shape | ✓ | The version number or alias name. |

## Output Shape: PutProvisionedConcurrencyConfigResponse

- **AllocatedProvisionedConcurrentExecutions** (Any  # complex shape): The amount of provisioned concurrency allocated. When a weighted alias is used during linear and canary deployments, thi
- **AvailableProvisionedConcurrentExecutions** (Any  # complex shape): The amount of provisioned concurrency available.
- **LastModified** (str  # ISO8601): The date and time that a user last updated the configuration, in ISO 8601 format .
- **RequestedProvisionedConcurrentExecutions** (Any  # complex shape): The amount of provisioned concurrency requested.
- **Status** (Any  # complex shape): The status of the allocation process.
- **StatusReason** (str): For failed allocations, the reason that provisioned concurrency could not be allocated.

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ResourceConflictException**: The resource already exists, or another operation is in progress.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ResourceNotFoundException**: The resource specified in the request does not exist.

## Implementation

```speclang
def put_provisioned_concurrency_config(store, request: dict) -> dict:
    """Adds a provisioned concurrency configuration to a function's alias or version."""
    function_name = request.get("FunctionName", "").strip() if isinstance(request.get("FunctionName"), str) else request.get("FunctionName")
    if not function_name:
        raise ValidationException("FunctionName is required")
    provisioned_concurrent_executions = request.get("ProvisionedConcurrentExecutions", "").strip() if isinstance(request.get("ProvisionedConcurrentExecutions"), str) else request.get("ProvisionedConcurrentExecutions")
    if not provisioned_concurrent_executions:
        raise ValidationException("ProvisionedConcurrentExecutions is required")
    qualifier = request.get("Qualifier", "").strip() if isinstance(request.get("Qualifier"), str) else request.get("Qualifier")
    if not qualifier:
        raise ValidationException("Qualifier is required")

    if store.provisioned_concurrency_configs(function_name):
        raise ResourceInUseException(f"Resource function_name already exists")

    record = {
        "FunctionName": function_name,
        "Qualifier": qualifier,
        "ProvisionedConcurrentExecutions": provisioned_concurrent_executions,
    }

    store.provisioned_concurrency_configs(function_name, record)

    return {
        "RequestedProvisionedConcurrentExecutions": record.get("RequestedProvisionedConcurrentExecutions", {}),
        "AvailableProvisionedConcurrentExecutions": record.get("AvailableProvisionedConcurrentExecutions", {}),
        "AllocatedProvisionedConcurrentExecutions": record.get("AllocatedProvisionedConcurrentExecutions", {}),
        "Status": record.get("Status", {}),
        "StatusReason": record.get("StatusReason", {}),
        "LastModified": record.get("LastModified", {}),
    }
```
