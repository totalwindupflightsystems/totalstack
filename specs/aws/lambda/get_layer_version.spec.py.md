---
id: "@specs/aws/lambda/get_layer_version"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_GetLayerVersion"
---

# GetLayerVersion

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/get_layer_version
> **spec:implements:** @kind:operation GetLayerVersion
> **AWS Protocol:** rest-json
> **HTTP:** GET /2018-10-31/layers/{LayerName}/versions/{VersionNumber}
> **@ref:** specs/aws/lambda/docs/API_GetLayerVersion.spec.md

Returns information about a version of an Lambda layer , with a link to download the layer archive that's valid for 10 minutes.

## Input Shape: GetLayerVersionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| LayerName | Any  # complex shape | ✓ | The name or Amazon Resource Name (ARN) of the layer. |
| VersionNumber | Any  # complex shape | ✓ | The version number. |

## Output Shape: GetLayerVersionResponse

- **CompatibleArchitectures** (Any  # complex shape): A list of compatible instruction set architectures .
- **CompatibleRuntimes** (Any  # complex shape): The layer's compatible runtimes. The following list includes deprecated runtimes. For more information, see Runtime use 
- **Content** (Any  # complex shape): Details about the layer version.
- **CreatedDate** (str  # ISO8601): The date that the layer version was created, in ISO-8601 format (YYYY-MM-DDThh:mm:ss.sTZD).
- **Description** (Any  # complex shape): The description of the version.
- **LayerArn** (Any  # complex shape): The ARN of the layer.
- **LayerVersionArn** (Any  # complex shape): The ARN of the layer version.
- **LicenseInfo** (Any  # complex shape): The layer's software license.
- **Version** (Any  # complex shape): The version number.

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ResourceNotFoundException**: The resource specified in the request does not exist.

## Implementation

```speclang
def get_layer_version(store, request: dict) -> dict:
    """Returns information about a version of an Lambda layer , with a link to download the layer archive that's valid for 10 minutes."""
    layer_name = request.get("LayerName", "").strip() if isinstance(request.get("LayerName"), str) else request.get("LayerName")
    if not layer_name:
        raise ValidationException("LayerName is required")
    version_number = request.get("VersionNumber", "").strip() if isinstance(request.get("VersionNumber"), str) else request.get("VersionNumber")
    if not version_number:
        raise ValidationException("VersionNumber is required")

    resource = store.layer_versions(layer_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource layer_name not found")
    return {"LayerName": layer_name, **resource}
```
