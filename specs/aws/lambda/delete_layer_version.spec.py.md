---
id: "@specs/aws/lambda/delete_layer_version"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_DeleteLayerVersion"
---

# DeleteLayerVersion

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/delete_layer_version
> **spec:implements:** @kind:operation DeleteLayerVersion
> **AWS Protocol:** rest-json
> **HTTP:** DELETE /2018-10-31/layers/{LayerName}/versions/{VersionNumber}
> **@ref:** specs/aws/lambda/docs/API_DeleteLayerVersion.spec.md

Deletes a version of an Lambda layer . Deleted versions can no longer be viewed or added to functions. To avoid breaking functions, a copy of the version remains in Lambda until no functions refer to it.

## Input Shape: DeleteLayerVersionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| LayerName | Any  # complex shape | ✓ | The name or Amazon Resource Name (ARN) of the layer. |
| VersionNumber | Any  # complex shape | ✓ | The version number. |

## Errors
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .

## Implementation

```speclang
def delete_layer_version(store, request: dict) -> dict:
    """Deletes a version of an Lambda layer . Deleted versions can no longer be viewed or added to functions. To avoid breaking functions, a copy of the version remains in Lambda until no functions refer to """
    layer_name = request.get("LayerName", "").strip() if isinstance(request.get("LayerName"), str) else request.get("LayerName")
    version_number = request.get("VersionNumber", "").strip() if isinstance(request.get("VersionNumber"), str) else request.get("VersionNumber")

    if not store.layer_versions(layer_name):
        raise ResourceNotFoundException(f"Resource layer_name not found")
    store.delete_layer_versions(layer_name)
    return {}
```
