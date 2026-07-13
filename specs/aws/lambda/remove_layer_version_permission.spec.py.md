---
id: "@specs/aws/lambda/remove_layer_version_permission"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_RemoveLayerVersionPermission"
---

# RemoveLayerVersionPermission

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/remove_layer_version_permission
> **spec:implements:** @kind:operation RemoveLayerVersionPermission
> **AWS Protocol:** rest-json
> **HTTP:** DELETE /2018-10-31/layers/{LayerName}/versions/{VersionNumber}/policy/{StatementId}
> **@ref:** specs/aws/lambda/docs/API_RemoveLayerVersionPermission.spec.md

Removes a statement from the permissions policy for a version of an Lambda layer . For more information, see AddLayerVersionPermission .

## Input Shape: RemoveLayerVersionPermissionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| LayerName | Any  # complex shape | ✓ | The name or Amazon Resource Name (ARN) of the layer. |
| RevisionId | str |  | Only update the policy if the revision ID matches the ID specified. Use this option to avoid modifying a policy that has |
| StatementId | Any  # complex shape | ✓ | The identifier that was specified when the statement was added. |
| VersionNumber | Any  # complex shape | ✓ | The version number. |

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ResourceNotFoundException**: The resource specified in the request does not exist.
- **PreconditionFailedException**: The RevisionId provided does not match the latest RevisionId for the Lambda function or alias. For AddPermission and RemovePermission API operations: Call GetPolicy to retrieve the latest RevisionId f

## Implementation

```speclang
def remove_layer_version_permission(store, request: dict) -> dict:
    """Removes a statement from the permissions policy for a version of an Lambda layer . For more information, see AddLayerVersionPermission ."""
    layer_name = request.get("LayerName", "").strip() if isinstance(request.get("LayerName"), str) else request.get("LayerName")
    statement_id = request.get("StatementId", "").strip() if isinstance(request.get("StatementId"), str) else request.get("StatementId")
    version_number = request.get("VersionNumber", "").strip() if isinstance(request.get("VersionNumber"), str) else request.get("VersionNumber")

    if not store.layer_version_permissions(layer_name):
        raise ResourceNotFoundException(f"Resource layer_name not found")
    store.delete_layer_version_permissions(layer_name)
    return {}
```
