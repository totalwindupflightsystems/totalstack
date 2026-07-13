---
id: "@specs/aws/lambda/get_alias"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_GetAlias"
---

# GetAlias

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/get_alias
> **spec:implements:** @kind:operation GetAlias
> **AWS Protocol:** rest-json
> **HTTP:** GET /2015-03-31/functions/{FunctionName}/aliases/{Name}
> **@ref:** specs/aws/lambda/docs/API_GetAlias.spec.md

Returns details about a Lambda function alias .

## Input Shape: GetAliasRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| FunctionName | Any  # complex shape | ✓ | The name or ARN of the Lambda function. Name formats Function name - MyFunction . Function ARN - arn:aws:lambda:us-west- |
| Name | Any  # complex shape | ✓ | The name of the alias. |

## Output Shape: AliasConfiguration

- **AliasArn** (Any  # complex shape): The Amazon Resource Name (ARN) of the alias.
- **Description** (Any  # complex shape): A description of the alias.
- **FunctionVersion** (Any  # complex shape): The function version that the alias invokes.
- **Name** (Any  # complex shape): The name of the alias.
- **RevisionId** (str): A unique identifier that changes when you update the alias.
- **RoutingConfig** (Any  # complex shape): The routing configuration of the alias.

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ResourceNotFoundException**: The resource specified in the request does not exist.

## Implementation

```speclang
def get_alias(store, request: dict) -> dict:
    """Returns details about a Lambda function alias ."""
    function_name = request.get("FunctionName", "").strip() if isinstance(request.get("FunctionName"), str) else request.get("FunctionName")
    if not function_name:
        raise ValidationException("FunctionName is required")
    name = request.get("Name", "").strip() if isinstance(request.get("Name"), str) else request.get("Name")
    if not name:
        raise ValidationException("Name is required")

    resource = store.aliass(function_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource function_name not found")
    return {"FunctionName": function_name, **resource}
```
