---
id: "@specs/aws/lambda/publish_layer_version"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_PublishLayerVersion"
---

# PublishLayerVersion

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/publish_layer_version
> **spec:implements:** @kind:operation PublishLayerVersion
> **AWS Protocol:** rest-json
> **HTTP:** POST /2018-10-31/layers/{LayerName}/versions
> **@ref:** specs/aws/lambda/docs/API_PublishLayerVersion.spec.md

Creates an Lambda layer from a ZIP archive. Each time you call PublishLayerVersion with the same layer name, a new version is created. Add layers to your function with CreateFunction or UpdateFunctionConfiguration .

## Input Shape: PublishLayerVersionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CompatibleArchitectures | Any  # complex shape |  | A list of compatible instruction set architectures . |
| CompatibleRuntimes | Any  # complex shape |  | A list of compatible function runtimes . Used for filtering with ListLayers and ListLayerVersions . The following list i |
| Content | Any  # complex shape | ✓ | The function layer archive. |
| Description | Any  # complex shape |  | The description of the version. |
| LayerName | Any  # complex shape | ✓ | The name or Amazon Resource Name (ARN) of the layer. |
| LicenseInfo | Any  # complex shape |  | The layer's software license. It can be any of the following: An SPDX license identifier . For example, MIT . The URL of |

## Output Shape: PublishLayerVersionResponse

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
- **CodeStorageExceededException**: Your Amazon Web Services account has exceeded its maximum total code size. For more information, see Lambda quotas .

## Implementation

```speclang
def publish_layer_version(store, request: dict) -> dict:
    """Creates an Lambda layer from a ZIP archive. Each time you call PublishLayerVersion with the same layer name, a new version is created. Add layers to your function with CreateFunction or UpdateFunction"""
    content = request.get("Content", "").strip() if isinstance(request.get("Content"), str) else request.get("Content")
    if not content:
        raise ValidationException("Content is required")
    layer_name = request.get("LayerName", "").strip() if isinstance(request.get("LayerName"), str) else request.get("LayerName")
    if not layer_name:
        raise ValidationException("LayerName is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("PublishLayerVersion", request)
```
