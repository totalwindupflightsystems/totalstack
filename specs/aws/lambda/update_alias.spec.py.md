---
id: "@specs/aws/lambda/update_alias"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_UpdateAlias"
---

# UpdateAlias

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/update_alias
> **spec:implements:** @kind:operation UpdateAlias
> **AWS Protocol:** rest-json
> **HTTP:** PUT /2015-03-31/functions/{FunctionName}/aliases/{Name}
> **@ref:** specs/aws/lambda/docs/API_UpdateAlias.spec.md

Updates the configuration of a Lambda function alias .

## Input Shape: UpdateAliasRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Description | Any  # complex shape |  | A description of the alias. |
| FunctionName | Any  # complex shape | ✓ | The name or ARN of the Lambda function. Name formats Function name - MyFunction . Function ARN - arn:aws:lambda:us-west- |
| FunctionVersion | Any  # complex shape |  | The function version that the alias invokes. |
| Name | Any  # complex shape | ✓ | The name of the alias. |
| RevisionId | str |  | Only update the alias if the revision ID matches the ID that's specified. Use this option to avoid modifying an alias th |
| RoutingConfig | Any  # complex shape |  | The routing configuration of the alias. |

## Output Shape: AliasConfiguration

- **AliasArn** (Any  # complex shape): The Amazon Resource Name (ARN) of the alias.
- **Description** (Any  # complex shape): A description of the alias.
- **FunctionVersion** (Any  # complex shape): The function version that the alias invokes.
- **Name** (Any  # complex shape): The name of the alias.
- **RevisionId** (str): A unique identifier that changes when you update the alias.
- **RoutingConfig** (Any  # complex shape): The routing configuration of the alias.

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ResourceConflictException**: The resource already exists, or another operation is in progress.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ResourceNotFoundException**: The resource specified in the request does not exist.
- **PreconditionFailedException**: The RevisionId provided does not match the latest RevisionId for the Lambda function or alias. For AddPermission and RemovePermission API operations: Call GetPolicy to retrieve the latest RevisionId f

## Implementation

```speclang
def update_alias(store, request: dict) -> dict:
    """Updates the configuration of a Lambda function alias ."""
    function_name = request.get("FunctionName", "").strip() if isinstance(request.get("FunctionName"), str) else request.get("FunctionName")
    if not function_name:
        raise ValidationException("FunctionName is required")
    name = request.get("Name", "").strip() if isinstance(request.get("Name"), str) else request.get("Name")
    if not name:
        raise ValidationException("Name is required")

    resource = store.aliass(function_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource function_name not found")

    # Update mutable fields
    if "FunctionVersion" in request:
        resource["FunctionVersion"] = function_version
    if "Description" in request:
        resource["Description"] = description
    if "RoutingConfig" in request:
        resource["RoutingConfig"] = routing_config
    if "RevisionId" in request:
        resource["RevisionId"] = revision_id

    store.aliass(function_name, resource)
    return resource
```
