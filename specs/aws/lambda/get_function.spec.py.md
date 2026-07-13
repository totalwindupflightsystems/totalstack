---
id: "@specs/aws/lambda/get_function"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_GetFunction"
---

# GetFunction

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/get_function
> **spec:implements:** @kind:operation GetFunction
> **AWS Protocol:** rest-json
> **HTTP:** GET /2015-03-31/functions/{FunctionName}
> **@ref:** specs/aws/lambda/docs/API_GetFunction.spec.md

Returns information about the function or function version, with a link to download the deployment package that's valid for 10 minutes. If you specify a function version, only details that are specific to that version are returned.

## Input Shape: GetFunctionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| FunctionName | Any  # complex shape | ✓ | The name or ARN of the Lambda function, version, or alias. Name formats Function name – my-function (name-only), my-func |
| Qualifier | Any  # complex shape |  | Specify a version or alias to get details about a published version of the function. |

## Output Shape: GetFunctionResponse

- **Code** (Any  # complex shape): The deployment package of the function or version.
- **Concurrency** (Any  # complex shape): The function's reserved concurrency .
- **Configuration** (Any  # complex shape): The configuration of the function or version.
- **Tags** (Any  # complex shape): The function's tags . Lambda returns tag data only if you have explicit allow permissions for lambda:ListTags .
- **TagsError** (Any  # complex shape): An object that contains details about an error related to retrieving tags.

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ResourceNotFoundException**: The resource specified in the request does not exist.

## Implementation

```speclang
def get_function(store, request: dict) -> dict:
    """Returns information about the function or function version, with a link to download the deployment package that's valid for 10 minutes. If you specify a function version, only details that are specifi"""
    function_name = request.get("FunctionName", "").strip() if isinstance(request.get("FunctionName"), str) else request.get("FunctionName")
    if not function_name:
        raise ValidationException("FunctionName is required")

    resource = store.functions(function_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource function_name not found")
    return {"FunctionName": function_name, **resource}
```
