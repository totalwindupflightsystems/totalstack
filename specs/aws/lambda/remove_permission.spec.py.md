---
id: "@specs/aws/lambda/remove_permission"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_RemovePermission"
---

# RemovePermission

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/remove_permission
> **spec:implements:** @kind:operation RemovePermission
> **AWS Protocol:** rest-json
> **HTTP:** DELETE /2015-03-31/functions/{FunctionName}/policy/{StatementId}
> **@ref:** specs/aws/lambda/docs/API_RemovePermission.spec.md

Revokes function-use permission from an Amazon Web Services service or another Amazon Web Services account. You can get the ID of the statement from the output of GetPolicy .

## Input Shape: RemovePermissionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| FunctionName | Any  # complex shape | ✓ | The name or ARN of the Lambda function, version, or alias. Name formats Function name – my-function (name-only), my-func |
| Qualifier | Any  # complex shape |  | Specify a version or alias to remove permissions from a published version of the function. |
| RevisionId | str |  | Update the policy only if the revision ID matches the ID that's specified. Use this option to avoid modifying a policy t |
| StatementId | Any  # complex shape | ✓ | Statement ID of the permission to remove. |

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ResourceNotFoundException**: The resource specified in the request does not exist.
- **PreconditionFailedException**: The RevisionId provided does not match the latest RevisionId for the Lambda function or alias. For AddPermission and RemovePermission API operations: Call GetPolicy to retrieve the latest RevisionId f

## Implementation

```speclang
def remove_permission(store, request: dict) -> dict:
    """Revokes function-use permission from an Amazon Web Services service or another Amazon Web Services account. You can get the ID of the statement from the output of GetPolicy ."""
    function_name = request.get("FunctionName", "").strip() if isinstance(request.get("FunctionName"), str) else request.get("FunctionName")
    statement_id = request.get("StatementId", "").strip() if isinstance(request.get("StatementId"), str) else request.get("StatementId")

    if not store.permissions(function_name):
        raise ResourceNotFoundException(f"Resource function_name not found")
    store.delete_permissions(function_name)
    return {}
```
