---
id: "@specs/aws/lambda/list_layer_versions"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_ListLayerVersions"
---

# ListLayerVersions

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/list_layer_versions
> **spec:implements:** @kind:operation ListLayerVersions
> **AWS Protocol:** rest-json
> **HTTP:** GET /2018-10-31/layers/{LayerName}/versions
> **@ref:** specs/aws/lambda/docs/API_ListLayerVersions.spec.md

Lists the versions of an Lambda layer . Versions that have been deleted aren't listed. Specify a runtime identifier to list only versions that indicate that they're compatible with that runtime. Specify a compatible architecture to include only layer versions that are compatible with that architecture.

## Input Shape: ListLayerVersionsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CompatibleArchitecture | Any  # complex shape |  | The compatible instruction set architecture . |
| CompatibleRuntime | Any  # complex shape |  | A runtime identifier. The following list includes deprecated runtimes. For more information, see Runtime use after depre |
| LayerName | Any  # complex shape | ✓ | The name or Amazon Resource Name (ARN) of the layer. |
| Marker | str |  | A pagination token returned by a previous call. |
| MaxItems | Any  # complex shape |  | The maximum number of versions to return. |

## Output Shape: ListLayerVersionsResponse

- **LayerVersions** (list[Any  # complex shape]): A list of versions.
- **NextMarker** (str): A pagination token returned when the response doesn't contain all versions.

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ResourceNotFoundException**: The resource specified in the request does not exist.

## Implementation

```speclang
def list_layer_versions(store, request: dict) -> dict:
    """Lists the versions of an Lambda layer . Versions that have been deleted aren't listed. Specify a runtime identifier to list only versions that indicate that they're compatible with that runtime. Speci"""
    layer_name = request.get("LayerName", "").strip() if isinstance(request.get("LayerName"), str) else request.get("LayerName")
    if not layer_name:
        raise ValidationException("LayerName is required")

    items = store.list_layer_versionss()
    return {"LayerVersions": list(items.values())}
```
