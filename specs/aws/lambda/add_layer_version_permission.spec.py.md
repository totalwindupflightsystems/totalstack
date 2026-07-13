---
id: "@specs/aws/lambda/add_layer_version_permission"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_AddLayerVersionPermission"
---

# AddLayerVersionPermission

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/add_layer_version_permission
> **spec:implements:** @kind:operation AddLayerVersionPermission
> **AWS Protocol:** rest-json
> **HTTP:** POST /2018-10-31/layers/{LayerName}/versions/{VersionNumber}/policy
> **@ref:** specs/aws/lambda/docs/API_AddLayerVersionPermission.spec.md

Adds permissions to the resource-based policy of a version of an Lambda layer . Use this action to grant layer usage permission to other accounts. You can grant permission to a single account, all accounts in an organization, or all Amazon Web Services accounts. To revoke permission, call RemoveLayerVersionPermission with the statement ID that you specified when you added it.

## Input Shape: AddLayerVersionPermissionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Action | Any  # complex shape | ✓ | The API action that grants access to the layer. For example, lambda:GetLayerVersion . |
| LayerName | Any  # complex shape | ✓ | The name or Amazon Resource Name (ARN) of the layer. |
| OrganizationId | Any  # complex shape |  | With the principal set to * , grant permission to all accounts in the specified organization. |
| Principal | Any  # complex shape | ✓ | An account ID, or * to grant layer usage permission to all accounts in an organization, or all Amazon Web Services accou |
| RevisionId | str |  | Only update the policy if the revision ID matches the ID specified. Use this option to avoid modifying a policy that has |
| StatementId | Any  # complex shape | ✓ | An identifier that distinguishes the policy from others on the same layer version. |
| VersionNumber | Any  # complex shape | ✓ | The version number. |

## Output Shape: AddLayerVersionPermissionResponse

- **RevisionId** (str): A unique identifier for the current revision of the policy.
- **Statement** (str): The permission statement.

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ResourceConflictException**: The resource already exists, or another operation is in progress.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **PolicyLengthExceededException**: The permissions policy for the resource is too large. For more information, see Lambda quotas .
- **ResourceNotFoundException**: The resource specified in the request does not exist.
- **PreconditionFailedException**: The RevisionId provided does not match the latest RevisionId for the Lambda function or alias. For AddPermission and RemovePermission API operations: Call GetPolicy to retrieve the latest RevisionId f

## Implementation

```speclang
def add_layer_version_permission(store, request: dict) -> dict:
    """Adds permissions to the resource-based policy of a version of an Lambda layer . Use this action to grant layer usage permission to other accounts. You can grant permission to a single account, all acc"""
    action = request.get("Action", "").strip() if isinstance(request.get("Action"), str) else request.get("Action")
    if not action:
        raise ValidationException("Action is required")
    layer_name = request.get("LayerName", "").strip() if isinstance(request.get("LayerName"), str) else request.get("LayerName")
    if not layer_name:
        raise ValidationException("LayerName is required")
    principal = request.get("Principal", "").strip() if isinstance(request.get("Principal"), str) else request.get("Principal")
    if not principal:
        raise ValidationException("Principal is required")
    statement_id = request.get("StatementId", "").strip() if isinstance(request.get("StatementId"), str) else request.get("StatementId")
    if not statement_id:
        raise ValidationException("StatementId is required")
    version_number = request.get("VersionNumber", "").strip() if isinstance(request.get("VersionNumber"), str) else request.get("VersionNumber")
    if not version_number:
        raise ValidationException("VersionNumber is required")

    if store.layer_version_permissions(statement_id):
        raise ResourceInUseException(f"Resource statement_id already exists")

    record = {
        "LayerName": layer_name,
        "VersionNumber": version_number,
        "StatementId": statement_id,
        "Action": action,
        "Principal": principal,
        "OrganizationId": organization_id,
        "RevisionId": revision_id,
    }

    store.layer_version_permissions(statement_id, record)

    return {
        "Statement": record.get("Statement", {}),
        "RevisionId": record.get("RevisionId", {}),
    }
```
