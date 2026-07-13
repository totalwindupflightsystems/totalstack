---
id: "@specs/aws/lambda/update_function_url_config"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_UpdateFunctionUrlConfig"
---

# UpdateFunctionUrlConfig

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/update_function_url_config
> **spec:implements:** @kind:operation UpdateFunctionUrlConfig
> **AWS Protocol:** rest-json
> **HTTP:** PUT /2021-10-31/functions/{FunctionName}/url
> **@ref:** specs/aws/lambda/docs/API_UpdateFunctionUrlConfig.spec.md

Updates the configuration for a Lambda function URL.

## Input Shape: UpdateFunctionUrlConfigRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AuthType | Any  # complex shape |  | The type of authentication that your function URL uses. Set to AWS_IAM if you want to restrict access to authenticated u |
| Cors | Any  # complex shape |  | The cross-origin resource sharing (CORS) settings for your function URL. |
| FunctionName | Any  # complex shape | ✓ | The name or ARN of the Lambda function. Name formats Function name – my-function . Function ARN – arn:aws:lambda:us-west |
| InvokeMode | Any  # complex shape |  | Use one of the following options: BUFFERED – This is the default option. Lambda invokes your function using the Invoke A |
| Qualifier | Any  # complex shape |  | The alias name. |

## Output Shape: UpdateFunctionUrlConfigResponse

- **AuthType** (Any  # complex shape): The type of authentication that your function URL uses. Set to AWS_IAM if you want to restrict access to authenticated u
- **Cors** (Any  # complex shape): The cross-origin resource sharing (CORS) settings for your function URL.
- **CreationTime** (str  # ISO8601): When the function URL was created, in ISO-8601 format (YYYY-MM-DDThh:mm:ss.sTZD).
- **FunctionArn** (Any  # complex shape): The Amazon Resource Name (ARN) of your function.
- **FunctionUrl** (Any  # complex shape): The HTTP URL endpoint for your function.
- **InvokeMode** (Any  # complex shape): Use one of the following options: BUFFERED – This is the default option. Lambda invokes your function using the Invoke A
- **LastModifiedTime** (str  # ISO8601): When the function URL configuration was last updated, in ISO-8601 format (YYYY-MM-DDThh:mm:ss.sTZD).

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ResourceConflictException**: The resource already exists, or another operation is in progress.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ResourceNotFoundException**: The resource specified in the request does not exist.

## Implementation

```speclang
def update_function_url_config(store, request: dict) -> dict:
    """Updates the configuration for a Lambda function URL."""
    function_name = request.get("FunctionName", "").strip() if isinstance(request.get("FunctionName"), str) else request.get("FunctionName")
    if not function_name:
        raise ValidationException("FunctionName is required")

    resource = store.function_url_configs(function_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource function_name not found")

    # Update mutable fields
    if "Qualifier" in request:
        resource["Qualifier"] = qualifier
    if "AuthType" in request:
        resource["AuthType"] = auth_type
    if "Cors" in request:
        resource["Cors"] = cors
    if "InvokeMode" in request:
        resource["InvokeMode"] = invoke_mode

    store.function_url_configs(function_name, resource)
    return resource
```
