---
id: "@specs/aws/lambda/create_function_url_config"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_CreateFunctionUrlConfig"
---

# CreateFunctionUrlConfig

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/create_function_url_config
> **spec:implements:** @kind:operation CreateFunctionUrlConfig
> **AWS Protocol:** rest-json
> **HTTP:** POST /2021-10-31/functions/{FunctionName}/url
> **@ref:** specs/aws/lambda/docs/API_CreateFunctionUrlConfig.spec.md

Creates a Lambda function URL with the specified configuration parameters. A function URL is a dedicated HTTP(S) endpoint that you can use to invoke your function.

## Input Shape: CreateFunctionUrlConfigRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AuthType | Any  # complex shape | ✓ | The type of authentication that your function URL uses. Set to AWS_IAM if you want to restrict access to authenticated u |
| Cors | Any  # complex shape |  | The cross-origin resource sharing (CORS) settings for your function URL. |
| FunctionName | Any  # complex shape | ✓ | The name or ARN of the Lambda function. Name formats Function name – my-function . Function ARN – arn:aws:lambda:us-west |
| InvokeMode | Any  # complex shape |  | Use one of the following options: BUFFERED – This is the default option. Lambda invokes your function using the Invoke A |
| Qualifier | Any  # complex shape |  | The alias name. |

## Output Shape: CreateFunctionUrlConfigResponse

- **AuthType** (Any  # complex shape): The type of authentication that your function URL uses. Set to AWS_IAM if you want to restrict access to authenticated u
- **Cors** (Any  # complex shape): The cross-origin resource sharing (CORS) settings for your function URL.
- **CreationTime** (str  # ISO8601): When the function URL was created, in ISO-8601 format (YYYY-MM-DDThh:mm:ss.sTZD).
- **FunctionArn** (Any  # complex shape): The Amazon Resource Name (ARN) of your function.
- **FunctionUrl** (Any  # complex shape): The HTTP URL endpoint for your function.
- **InvokeMode** (Any  # complex shape): Use one of the following options: BUFFERED – This is the default option. Lambda invokes your function using the Invoke A

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ResourceConflictException**: The resource already exists, or another operation is in progress.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ResourceNotFoundException**: The resource specified in the request does not exist.

## Implementation

```speclang
def create_function_url_config(store, request: dict) -> dict:
    """Creates a Lambda function URL with the specified configuration parameters. A function URL is a dedicated HTTP(S) endpoint that you can use to invoke your function."""
    auth_type = request.get("AuthType", "").strip() if isinstance(request.get("AuthType"), str) else request.get("AuthType")
    if not auth_type:
        raise ValidationException("AuthType is required")
    function_name = request.get("FunctionName", "").strip() if isinstance(request.get("FunctionName"), str) else request.get("FunctionName")
    if not function_name:
        raise ValidationException("FunctionName is required")

    if store.function_url_configs(function_name):
        raise ResourceInUseException(f"Resource function_name already exists")

    record = {
        "FunctionName": function_name,
        "Qualifier": qualifier,
        "AuthType": auth_type,
        "Cors": cors,
        "InvokeMode": invoke_mode,
    }

    store.function_url_configs(function_name, record)

    return {
        "FunctionUrl": record.get("FunctionUrl", {}),
        "FunctionArn": record.get("FunctionArn", {}),
        "AuthType": record.get("AuthType", {}),
        "Cors": record.get("Cors", {}),
        "CreationTime": record.get("CreationTime", {}),
        "InvokeMode": record.get("InvokeMode", {}),
    }
```
