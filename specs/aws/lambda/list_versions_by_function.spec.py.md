---
id: "@specs/aws/lambda/list_versions_by_function"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_ListVersionsByFunction"
---

# ListVersionsByFunction

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/list_versions_by_function
> **spec:implements:** @kind:operation ListVersionsByFunction
> **AWS Protocol:** rest-json
> **HTTP:** GET /2015-03-31/functions/{FunctionName}/versions
> **@ref:** specs/aws/lambda/docs/API_ListVersionsByFunction.spec.md

Returns a list of versions , with the version-specific configuration of each. Lambda returns up to 50 versions per call.

## Input Shape: ListVersionsByFunctionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| FunctionName | Any  # complex shape | ✓ | The name or ARN of the Lambda function. Name formats Function name - MyFunction . Function ARN - arn:aws:lambda:us-west- |
| Marker | str |  | Specify the pagination token that's returned by a previous request to retrieve the next page of results. |
| MaxItems | Any  # complex shape |  | The maximum number of versions to return. Note that ListVersionsByFunction returns a maximum of 50 items in each respons |

## Output Shape: ListVersionsByFunctionResponse

- **NextMarker** (str): The pagination token that's included if more results are available.
- **Versions** (list[Any  # complex shape]): A list of Lambda function versions.

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ResourceNotFoundException**: The resource specified in the request does not exist.

## Implementation

```speclang
def list_versions_by_function(store, request: dict) -> dict:
    """Returns a list of versions , with the version-specific configuration of each. Lambda returns up to 50 versions per call."""
    function_name = request.get("FunctionName", "").strip() if isinstance(request.get("FunctionName"), str) else request.get("FunctionName")
    if not function_name:
        raise ValidationException("FunctionName is required")

    items = store.list_versions_by_functions()
    return {"Versions": list(items.values())}
```
