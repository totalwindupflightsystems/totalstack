---
id: "@specs/aws/lambda/list_functions_by_code_signing_config"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_ListFunctionsByCodeSigningConfig"
---

# ListFunctionsByCodeSigningConfig

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/list_functions_by_code_signing_config
> **spec:implements:** @kind:operation ListFunctionsByCodeSigningConfig
> **AWS Protocol:** rest-json
> **HTTP:** GET /2020-04-22/code-signing-configs/{CodeSigningConfigArn}/functions
> **@ref:** specs/aws/lambda/docs/API_ListFunctionsByCodeSigningConfig.spec.md

List the functions that use the specified code signing configuration. You can use this method prior to deleting a code signing configuration, to verify that no functions are using it.

## Input Shape: ListFunctionsByCodeSigningConfigRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CodeSigningConfigArn | Any  # complex shape | ✓ | The The Amazon Resource Name (ARN) of the code signing configuration. |
| Marker | str |  | Specify the pagination token that's returned by a previous request to retrieve the next page of results. |
| MaxItems | Any  # complex shape |  | Maximum number of items to return. |

## Output Shape: ListFunctionsByCodeSigningConfigResponse

- **FunctionArns** (list[Any  # complex shape]): The function ARNs.
- **NextMarker** (str): The pagination token that's included if more results are available.

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ServiceException**: The Lambda service encountered an internal error.
- **ResourceNotFoundException**: The resource specified in the request does not exist.

## Implementation

```speclang
def list_functions_by_code_signing_config(store, request: dict) -> dict:
    """List the functions that use the specified code signing configuration. You can use this method prior to deleting a code signing configuration, to verify that no functions are using it."""
    code_signing_config_arn = request.get("CodeSigningConfigArn", "").strip() if isinstance(request.get("CodeSigningConfigArn"), str) else request.get("CodeSigningConfigArn")
    if not code_signing_config_arn:
        raise ValidationException("CodeSigningConfigArn is required")

    items = store.list_functions_by_code_signing_configs()
    return {"FunctionArns": list(items.values())}
```
