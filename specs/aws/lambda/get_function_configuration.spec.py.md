---
id: "@specs/aws/lambda/get_function_configuration"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_GetFunctionConfiguration"
---

# GetFunctionConfiguration

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/get_function_configuration
> **spec:implements:** @kind:operation GetFunctionConfiguration
> **AWS Protocol:** rest-json
> **HTTP:** GET /2015-03-31/functions/{FunctionName}/configuration
> **@ref:** specs/aws/lambda/docs/API_GetFunctionConfiguration.spec.md

Returns the version-specific settings of a Lambda function or version. The output includes only options that can vary between versions of a function. To modify these settings, use UpdateFunctionConfiguration . To get all of a function's details, including function-level settings, use GetFunction .

## Input Shape: GetFunctionConfigurationRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| FunctionName | Any  # complex shape | ✓ | The name or ARN of the Lambda function, version, or alias. Name formats Function name – my-function (name-only), my-func |
| Qualifier | Any  # complex shape |  | Specify a version or alias to get details about a published version of the function. |

## Output Shape: FunctionConfiguration

- **Architectures** (list[Any  # complex shape]): The instruction set architecture that the function supports. Architecture is a string array with one of the valid values
- **CapacityProviderConfig** (Any  # complex shape): Configuration for the capacity provider that manages compute resources for Lambda functions.
- **CodeSha256** (str): The SHA256 hash of the function's deployment package.
- **CodeSize** (int): The size of the function's deployment package, in bytes.
- **ConfigSha256** (str): The SHA256 hash of the function configuration.
- **DeadLetterConfig** (Any  # complex shape): The function's dead letter queue.
- **Description** (Any  # complex shape): The function's description.
- **DurableConfig** (Any  # complex shape): The function's durable execution configuration settings, if the function is configured for durability.
- **Environment** (Any  # complex shape): The function's environment variables . Omitted from CloudTrail logs.
- **EphemeralStorage** (Any  # complex shape): The size of the function's /tmp directory in MB. The default value is 512, but can be any whole number between 512 and 1
- **FileSystemConfigs** (list[Any  # complex shape]): Connection settings for an Amazon EFS file system .
- **FunctionArn** (Any  # complex shape): The function's Amazon Resource Name (ARN).
- **FunctionName** (Any  # complex shape): The name of the function.
- **Handler** (Any  # complex shape): The function that Lambda calls to begin running your function.
- **ImageConfigResponse** (Any  # complex shape): The function's image configuration values.
- **KMSKeyArn** (Any  # complex shape): The ARN of the Key Management Service (KMS) customer managed key that's used to encrypt the following resources: The fun
- **LastModified** (str  # ISO8601): The date and time that the function was last updated, in ISO-8601 format (YYYY-MM-DDThh:mm:ss.sTZD).
- **LastUpdateStatus** (Any  # complex shape): The status of the last update that was performed on the function. This is first set to Successful after function creatio
- **LastUpdateStatusReason** (Any  # complex shape): The reason for the last update that was performed on the function.
- **LastUpdateStatusReasonCode** (Any  # complex shape): The reason code for the last update that was performed on the function.
- **Layers** (list[Any  # complex shape]): The function's layers .
- **LoggingConfig** (Any  # complex shape): The function's Amazon CloudWatch Logs configuration settings.
- **MasterArn** (Any  # complex shape): For Lambda@Edge functions, the ARN of the main function.
- **MemorySize** (Any  # complex shape): The amount of memory available to the function at runtime.
- **PackageType** (Any  # complex shape): The type of deployment package. Set to Image for container image and set Zip for .zip file archive.
- **RevisionId** (str): The latest updated revision of the function or alias.
- **Role** (Any  # complex shape): The function's execution role.
- **Runtime** (Any  # complex shape): The identifier of the function's runtime . Runtime is required if the deployment package is a .zip file archive. Specify
- **RuntimeVersionConfig** (Any  # complex shape): The ARN of the runtime and any errors that occured.
- **SigningJobArn** (Any  # complex shape): The ARN of the signing job.
- **SigningProfileVersionArn** (Any  # complex shape): The ARN of the signing profile version.
- **SnapStart** (Any  # complex shape): Set ApplyOn to PublishedVersions to create a snapshot of the initialized execution environment when you publish a functi
- **State** (Any  # complex shape): The current state of the function. When the state is Inactive , you can reactivate the function by invoking it.
- **StateReason** (Any  # complex shape): The reason for the function's current state.
- **StateReasonCode** (Any  # complex shape): The reason code for the function's current state. When the code is Creating , you can't invoke or modify the function.
- **TenancyConfig** (Any  # complex shape): The function's tenant isolation configuration settings. Determines whether the Lambda function runs on a shared or dedic
- **Timeout** (Any  # complex shape): The amount of time in seconds that Lambda allows a function to run before stopping it.
- **TracingConfig** (Any  # complex shape): The function's X-Ray tracing configuration.
- **Version** (Any  # complex shape): The version of the Lambda function.
- **VpcConfig** (Any  # complex shape): The function's networking configuration.

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ResourceNotFoundException**: The resource specified in the request does not exist.

## Implementation

```speclang
def get_function_configuration(store, request: dict) -> dict:
    """Returns the version-specific settings of a Lambda function or version. The output includes only options that can vary between versions of a function. To modify these settings, use UpdateFunctionConfig"""
    function_name = request.get("FunctionName", "").strip() if isinstance(request.get("FunctionName"), str) else request.get("FunctionName")
    if not function_name:
        raise ValidationException("FunctionName is required")

    resource = store.function_configurations(function_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource function_name not found")
    return {"FunctionName": function_name, **resource}
```
