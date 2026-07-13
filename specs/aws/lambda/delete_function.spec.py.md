---
id: "@specs/aws/lambda/delete_function"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_DeleteFunction"
---

# DeleteFunction

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/delete_function
> **spec:implements:** @kind:operation DeleteFunction
> **AWS Protocol:** rest-json
> **HTTP:** DELETE /2015-03-31/functions/{FunctionName}
> **@ref:** specs/aws/lambda/docs/API_DeleteFunction.spec.md

Deletes a Lambda function. To delete a specific function version, use the Qualifier parameter. Otherwise, all versions and aliases are deleted. This doesn't require the user to have explicit permissions for DeleteAlias . A deleted Lambda function cannot be recovered. Ensure that you specify the correct function name and version before deleting. To delete Lambda event source mappings that invoke a function, use DeleteEventSourceMapping . For Amazon Web Services services and resources that invoke your function directly, delete the trigger in the service where you originally configured it.

## Input Shape: DeleteFunctionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| FunctionName | Any  # complex shape | ✓ | The name or ARN of the Lambda function or version. Name formats Function name – my-function (name-only), my-function:1 ( |
| Qualifier | Any  # complex shape |  | Specify a version to delete. You can't delete a version that an alias references. |

## Output Shape: DeleteFunctionResponse

- **StatusCode** (int): The HTTP status code returned by the operation.

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ResourceConflictException**: The resource already exists, or another operation is in progress.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ResourceNotFoundException**: The resource specified in the request does not exist.

## Implementation

```speclang
def delete_function(store, request: dict) -> dict:
    """Deletes a Lambda function. To delete a specific function version, use the Qualifier parameter. Otherwise, all versions and aliases are deleted. This doesn't require the user to have explicit permissio"""
    function_name = request.get("FunctionName", "").strip() if isinstance(request.get("FunctionName"), str) else request.get("FunctionName")

    if not store.functions(function_name):
        raise ResourceNotFoundException(f"Resource function_name not found")
    store.delete_functions(function_name)
    return {}
```
