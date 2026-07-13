---
id: "@specs/aws/lambda/list_aliases"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_ListAliases"
---

# ListAliases

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/list_aliases
> **spec:implements:** @kind:operation ListAliases
> **AWS Protocol:** rest-json
> **HTTP:** GET /2015-03-31/functions/{FunctionName}/aliases
> **@ref:** specs/aws/lambda/docs/API_ListAliases.spec.md

Returns a list of aliases for a Lambda function.

## Input Shape: ListAliasesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| FunctionName | Any  # complex shape | ✓ | The name or ARN of the Lambda function. Name formats Function name - MyFunction . Function ARN - arn:aws:lambda:us-west- |
| FunctionVersion | Any  # complex shape |  | Specify a function version to only list aliases that invoke that version. |
| Marker | str |  | Specify the pagination token that's returned by a previous request to retrieve the next page of results. |
| MaxItems | Any  # complex shape |  | Limit the number of aliases returned. |

## Output Shape: ListAliasesResponse

- **Aliases** (list[Any  # complex shape]): A list of aliases.
- **NextMarker** (str): The pagination token that's included if more results are available.

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ResourceNotFoundException**: The resource specified in the request does not exist.

## Implementation

```speclang
def list_aliases(store, request: dict) -> dict:
    """Returns a list of aliases for a Lambda function."""
    function_name = request.get("FunctionName", "").strip() if isinstance(request.get("FunctionName"), str) else request.get("FunctionName")
    if not function_name:
        raise ValidationException("FunctionName is required")

    items = store.list_aliasess()
    return {"Aliases": list(items.values())}
```
