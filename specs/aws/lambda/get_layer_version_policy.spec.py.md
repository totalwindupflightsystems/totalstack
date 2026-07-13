---
id: "@specs/aws/lambda/get_layer_version_policy"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_GetLayerVersionPolicy"
---

# GetLayerVersionPolicy

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/get_layer_version_policy
> **spec:implements:** @kind:operation GetLayerVersionPolicy
> **AWS Protocol:** rest-json
> **HTTP:** GET /2018-10-31/layers/{LayerName}/versions/{VersionNumber}/policy
> **@ref:** specs/aws/lambda/docs/API_GetLayerVersionPolicy.spec.md

Returns the permission policy for a version of an Lambda layer . For more information, see AddLayerVersionPermission .

## Input Shape: GetLayerVersionPolicyRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| LayerName | Any  # complex shape | ✓ | The name or Amazon Resource Name (ARN) of the layer. |
| VersionNumber | Any  # complex shape | ✓ | The version number. |

## Output Shape: GetLayerVersionPolicyResponse

- **Policy** (str): The policy document.
- **RevisionId** (str): A unique identifier for the current revision of the policy.

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ResourceNotFoundException**: The resource specified in the request does not exist.

## Implementation

```speclang
def get_layer_version_policy(store, request: dict) -> dict:
    """Returns the permission policy for a version of an Lambda layer . For more information, see AddLayerVersionPermission ."""
    layer_name = request.get("LayerName", "").strip() if isinstance(request.get("LayerName"), str) else request.get("LayerName")
    if not layer_name:
        raise ValidationException("LayerName is required")
    version_number = request.get("VersionNumber", "").strip() if isinstance(request.get("VersionNumber"), str) else request.get("VersionNumber")
    if not version_number:
        raise ValidationException("VersionNumber is required")

    resource = store.layer_version_policys(layer_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource layer_name not found")
    return {"LayerName": layer_name, **resource}
```
