---
id: "@specs/aws/lambda/list_code_signing_configs"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_ListCodeSigningConfigs"
---

# ListCodeSigningConfigs

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/list_code_signing_configs
> **spec:implements:** @kind:operation ListCodeSigningConfigs
> **AWS Protocol:** rest-json
> **HTTP:** GET /2020-04-22/code-signing-configs
> **@ref:** specs/aws/lambda/docs/API_ListCodeSigningConfigs.spec.md

Returns a list of code signing configurations . A request returns up to 10,000 configurations per call. You can use the MaxItems parameter to return fewer configurations per call.

## Input Shape: ListCodeSigningConfigsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Marker | str |  | Specify the pagination token that's returned by a previous request to retrieve the next page of results. |
| MaxItems | Any  # complex shape |  | Maximum number of items to return. |

## Output Shape: ListCodeSigningConfigsResponse

- **CodeSigningConfigs** (list[Any  # complex shape]): The code signing configurations
- **NextMarker** (str): The pagination token that's included if more results are available.

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ServiceException**: The Lambda service encountered an internal error.

## Implementation

```speclang
def list_code_signing_configs(store, request: dict) -> dict:
    """Returns a list of code signing configurations . A request returns up to 10,000 configurations per call. You can use the MaxItems parameter to return fewer configurations per call."""

    items = store.list_code_signing_configss()
    return {"CodeSigningConfigs": list(items.values())}
```
