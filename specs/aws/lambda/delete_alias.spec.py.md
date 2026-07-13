---
id: "@specs/aws/lambda/delete_alias"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_DeleteAlias"
---

# DeleteAlias

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/delete_alias
> **spec:implements:** @kind:operation DeleteAlias
> **AWS Protocol:** rest-json
> **HTTP:** DELETE /2015-03-31/functions/{FunctionName}/aliases/{Name}
> **@ref:** specs/aws/lambda/docs/API_DeleteAlias.spec.md

Deletes a Lambda function alias .

## Input Shape: DeleteAliasRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| FunctionName | Any  # complex shape | ✓ | The name or ARN of the Lambda function. Name formats Function name - MyFunction . Function ARN - arn:aws:lambda:us-west- |
| Name | Any  # complex shape | ✓ | The name of the alias. |

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ResourceConflictException**: The resource already exists, or another operation is in progress.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .

## Implementation

```speclang
def delete_alias(store, request: dict) -> dict:
    """Deletes a Lambda function alias ."""
    function_name = request.get("FunctionName", "").strip() if isinstance(request.get("FunctionName"), str) else request.get("FunctionName")
    name = request.get("Name", "").strip() if isinstance(request.get("Name"), str) else request.get("Name")

    if not store.aliass(function_name):
        raise ResourceNotFoundException(f"Resource function_name not found")
    store.delete_aliass(function_name)
    return {}
```
