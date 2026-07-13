---
id: "@specs/aws/lambda/list_provisioned_concurrency_configs"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_ListProvisionedConcurrencyConfigs"
---

# ListProvisionedConcurrencyConfigs

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/list_provisioned_concurrency_configs
> **spec:implements:** @kind:operation ListProvisionedConcurrencyConfigs
> **AWS Protocol:** rest-json
> **HTTP:** GET /2019-09-30/functions/{FunctionName}/provisioned-concurrency?List=ALL
> **@ref:** specs/aws/lambda/docs/API_ListProvisionedConcurrencyConfigs.spec.md

Retrieves a list of provisioned concurrency configurations for a function.

## Input Shape: ListProvisionedConcurrencyConfigsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| FunctionName | Any  # complex shape | ✓ | The name or ARN of the Lambda function. Name formats Function name – my-function . Function ARN – arn:aws:lambda:us-west |
| Marker | str |  | Specify the pagination token that's returned by a previous request to retrieve the next page of results. |
| MaxItems | Any  # complex shape |  | Specify a number to limit the number of configurations returned. |

## Output Shape: ListProvisionedConcurrencyConfigsResponse

- **NextMarker** (str): The pagination token that's included if more results are available.
- **ProvisionedConcurrencyConfigs** (list[Any  # complex shape]): A list of provisioned concurrency configurations.

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ResourceNotFoundException**: The resource specified in the request does not exist.

## Implementation

```speclang
def list_provisioned_concurrency_configs(store, request: dict) -> dict:
    """Retrieves a list of provisioned concurrency configurations for a function."""
    function_name = request.get("FunctionName", "").strip() if isinstance(request.get("FunctionName"), str) else request.get("FunctionName")
    if not function_name:
        raise ValidationException("FunctionName is required")

    items = store.list_provisioned_concurrency_configss()
    return {"ProvisionedConcurrencyConfigs": list(items.values())}
```
