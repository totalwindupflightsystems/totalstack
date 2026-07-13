---
id: "@specs/aws/lambda/list_layers"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_ListLayers"
---

# ListLayers

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/list_layers
> **spec:implements:** @kind:operation ListLayers
> **AWS Protocol:** rest-json
> **HTTP:** GET /2018-10-31/layers
> **@ref:** specs/aws/lambda/docs/API_ListLayers.spec.md

Lists Lambda layers and shows information about the latest version of each. Specify a runtime identifier to list only layers that indicate that they're compatible with that runtime. Specify a compatible architecture to include only layers that are compatible with that instruction set architecture .

## Input Shape: ListLayersRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CompatibleArchitecture | Any  # complex shape |  | The compatible instruction set architecture . |
| CompatibleRuntime | Any  # complex shape |  | A runtime identifier. The following list includes deprecated runtimes. For more information, see Runtime use after depre |
| Marker | str |  | A pagination token returned by a previous call. |
| MaxItems | Any  # complex shape |  | The maximum number of layers to return. |

## Output Shape: ListLayersResponse

- **Layers** (list[Any  # complex shape]): A list of function layers.
- **NextMarker** (str): A pagination token returned when the response doesn't contain all layers.

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .

## Implementation

```speclang
def list_layers(store, request: dict) -> dict:
    """Lists Lambda layers and shows information about the latest version of each. Specify a runtime identifier to list only layers that indicate that they're compatible with that runtime. Specify a compatib"""

    items = store.list_layerss()
    return {"Layers": list(items.values())}
```
