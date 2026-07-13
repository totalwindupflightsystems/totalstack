---
id: "@specs/aws/lambda/list_function_url_configs"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_ListFunctionUrlConfigs"
---

# ListFunctionUrlConfigs

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/list_function_url_configs
> **spec:implements:** @kind:operation ListFunctionUrlConfigs
> **AWS Protocol:** rest-json
> **HTTP:** GET /2021-10-31/functions/{FunctionName}/urls
> **@ref:** specs/aws/lambda/docs/API_ListFunctionUrlConfigs.spec.md

Returns a list of Lambda function URLs for the specified function.

## Input Shape: ListFunctionUrlConfigsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| FunctionName | Any  # complex shape | ✓ | The name or ARN of the Lambda function. Name formats Function name – my-function . Function ARN – arn:aws:lambda:us-west |
| Marker | str |  | Specify the pagination token that's returned by a previous request to retrieve the next page of results. |
| MaxItems | Any  # complex shape |  | The maximum number of function URLs to return in the response. Note that ListFunctionUrlConfigs returns a maximum of 50  |

## Output Shape: ListFunctionUrlConfigsResponse

- **FunctionUrlConfigs** (list[Any  # complex shape]): A list of function URL configurations.
- **NextMarker** (str): The pagination token that's included if more results are available.

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ResourceNotFoundException**: The resource specified in the request does not exist.

## Implementation

```speclang
def list_function_url_configs(store, request: dict) -> dict:
    """Returns a list of Lambda function URLs for the specified function."""
    function_name = request.get("FunctionName", "").strip() if isinstance(request.get("FunctionName"), str) else request.get("FunctionName")
    if not function_name:
        raise ValidationException("FunctionName is required")

    items = store.list_function_url_configss()
    return {"FunctionUrlConfigs": list(items.values())}
```
