---
id: "@specs/aws/lambda/get_layer_version_by_arn"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_GetLayerVersionByArn"
---

# GetLayerVersionByArn

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/get_layer_version_by_arn
> **spec:implements:** @kind:operation GetLayerVersionByArn
> **AWS Protocol:** rest-json
> **HTTP:** GET /2018-10-31/layers?find=LayerVersion
> **@ref:** specs/aws/lambda/docs/API_GetLayerVersionByArn.spec.md

Returns information about a version of an Lambda layer , with a link to download the layer archive that's valid for 10 minutes.

## Input Shape: GetLayerVersionByArnRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Arn | Any  # complex shape | ✓ | The ARN of the layer version. |

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
def get_layer_version_by_arn(store, request: dict) -> dict:
    """Returns information about a version of an Lambda layer , with a link to download the layer archive that's valid for 10 minutes."""
    arn = request.get("Arn", "").strip() if isinstance(request.get("Arn"), str) else request.get("Arn")
    if not arn:
        raise ValidationException("Arn is required")

    resource = store.layer_version_by_arns(arn)
    if not resource:
        raise ResourceNotFoundException(f"Resource arn not found")
    return {"Arn": arn, **resource}
```
