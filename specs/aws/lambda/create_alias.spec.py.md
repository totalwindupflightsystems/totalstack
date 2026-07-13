---
id: "@specs/aws/lambda/create_alias"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_CreateAlias"
---

# CreateAlias

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/create_alias
> **spec:implements:** @kind:operation CreateAlias
> **AWS Protocol:** rest-json
> **HTTP:** POST /2015-03-31/functions/{FunctionName}/aliases
> **@ref:** specs/aws/lambda/docs/API_CreateAlias.spec.md

Creates an alias for a Lambda function version. Use aliases to provide clients with a function identifier that you can update to invoke a different version. You can also map an alias to split invocation requests between two versions. Use the RoutingConfig parameter to specify a second version and the percentage of invocation requests that it receives.

## Input Shape: CreateAliasRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Description | Any  # complex shape |  | A description of the alias. |
| FunctionName | Any  # complex shape | ✓ | The name or ARN of the Lambda function. Name formats Function name - MyFunction . Function ARN - arn:aws:lambda:us-west- |
| FunctionVersion | Any  # complex shape | ✓ | The function version that the alias invokes. |
| Name | Any  # complex shape | ✓ | The name of the alias. |
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

## Implementation

```speclang
def create_alias(store, request: dict) -> dict:
    """Creates an alias for a Lambda function version. Use aliases to provide clients with a function identifier that you can update to invoke a different version. You can also map an alias to split invocati"""
    function_name = request.get("FunctionName", "").strip() if isinstance(request.get("FunctionName"), str) else request.get("FunctionName")
    if not function_name:
        raise ValidationException("FunctionName is required")
    function_version = request.get("FunctionVersion", "").strip() if isinstance(request.get("FunctionVersion"), str) else request.get("FunctionVersion")
    if not function_version:
        raise ValidationException("FunctionVersion is required")
    name = request.get("Name", "").strip() if isinstance(request.get("Name"), str) else request.get("Name")
    if not name:
        raise ValidationException("Name is required")

    if store.aliass(function_name):
        raise ResourceInUseException(f"Resource function_name already exists")

    record = {
        "FunctionName": function_name,
        "Name": name,
        "FunctionVersion": function_version,
        "Description": description,
        "RoutingConfig": routing_config,
    }

    store.aliass(function_name, record)

    return {
        "AliasArn": record.get("AliasArn", {}),
        "Name": record.get("Name", {}),
        "FunctionVersion": record.get("FunctionVersion", {}),
        "Description": record.get("Description", {}),
        "RoutingConfig": record.get("RoutingConfig", {}),
        "RevisionId": record.get("RevisionId", {}),
    }
```
