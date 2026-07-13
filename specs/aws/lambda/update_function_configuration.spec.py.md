---
id: "@specs/aws/lambda/update_function_configuration"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_UpdateFunctionConfiguration"
---

# UpdateFunctionConfiguration

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/update_function_configuration
> **spec:implements:** @kind:operation UpdateFunctionConfiguration
> **AWS Protocol:** rest-json
> **HTTP:** PUT /2015-03-31/functions/{FunctionName}/configuration
> **@ref:** specs/aws/lambda/docs/API_UpdateFunctionConfiguration.spec.md

Modify the version-specific settings of a Lambda function. When you update a function, Lambda provisions an instance of the function and its supporting resources. If your function connects to a VPC, this process can take a minute. During this time, you can't modify the function, but you can still invoke it. The LastUpdateStatus , LastUpdateStatusReason , and LastUpdateStatusReasonCode fields in the response from GetFunctionConfiguration indicate when the update is complete and the function is processing events with the new configuration. For more information, see Lambda function states . These settings can vary between versions of a function and are locked when you publish a version. You can't modify the configuration of a published version, only the unpublished version. To configure function concurrency, use PutFunctionConcurrency . To grant invoke permissions to an Amazon Web Services account or Amazon Web Services service, use AddPermission .

## Input Shape: UpdateFunctionConfigurationRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CapacityProviderConfig | Any  # complex shape |  | Configuration for the capacity provider that manages compute resources for Lambda functions. |
| DeadLetterConfig | Any  # complex shape |  | A dead-letter queue configuration that specifies the queue or topic where Lambda sends asynchronous events when they fai |
| Description | Any  # complex shape |  | A description of the function. |
| DurableConfig | Any  # complex shape |  | Configuration settings for durable functions. Allows updating execution timeout and retention period for functions with  |
| Environment | Any  # complex shape |  | Environment variables that are accessible from function code during execution. |
| EphemeralStorage | Any  # complex shape |  | The size of the function's /tmp directory in MB. The default value is 512, but can be any whole number between 512 and 1 |
| FileSystemConfigs | list[Any  # complex shape] |  | Connection settings for an Amazon EFS file system. |
| FunctionName | Any  # complex shape | ✓ | The name or ARN of the Lambda function. Name formats Function name – my-function . Function ARN – arn:aws:lambda:us-west |
| Handler | Any  # complex shape |  | The name of the method within your code that Lambda calls to run your function. Handler is required if the deployment pa |
| ImageConfig | Any  # complex shape |  | Container image configuration values that override the values in the container image Docker file. |
| KMSKeyArn | Any  # complex shape |  | The ARN of the Key Management Service (KMS) customer managed key that's used to encrypt the following resources: The fun |
| Layers | list[Any  # complex shape] |  | A list of function layers to add to the function's execution environment. Specify each layer by its ARN, including the v |
| LoggingConfig | Any  # complex shape |  | The function's Amazon CloudWatch Logs configuration settings. |
| MemorySize | Any  # complex shape |  | The amount of memory available to the function at runtime. Increasing the function memory also increases its CPU allocat |
| RevisionId | str |  | Update the function only if the revision ID matches the ID that's specified. Use this option to avoid modifying a functi |
| Role | Any  # complex shape |  | The Amazon Resource Name (ARN) of the function's execution role. |
| Runtime | Any  # complex shape |  | The identifier of the function's runtime . Runtime is required if the deployment package is a .zip file archive. Specify |
| SnapStart | Any  # complex shape |  | The function's SnapStart setting. |
| Timeout | Any  # complex shape |  | The amount of time (in seconds) that Lambda allows a function to run before stopping it. The default is 3 seconds. The m |
| TracingConfig | Any  # complex shape |  | Set Mode to Active to sample and trace a subset of incoming requests with X-Ray . |
| VpcConfig | Any  # complex shape |  | For network connectivity to Amazon Web Services resources in a VPC, specify a list of security groups and subnets in the |

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
- **ResourceConflictException**: The resource already exists, or another operation is in progress.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **InvalidCodeSignatureException**: The code signature failed the integrity check. If the integrity check fails, then Lambda blocks deployment, even if the code signing policy is set to WARN.
- **ResourceNotFoundException**: The resource specified in the request does not exist.
- **CodeVerificationFailedException**: The code signature failed one or more of the validation checks for signature mismatch or expiry, and the code signing policy is set to ENFORCE. Lambda blocks the deployment.
- **CodeSigningConfigNotFoundException**: The specified code signing configuration does not exist.
- **PreconditionFailedException**: The RevisionId provided does not match the latest RevisionId for the Lambda function or alias. For AddPermission and RemovePermission API operations: Call GetPolicy to retrieve the latest RevisionId f

## Implementation

```speclang
def update_function_configuration(store, request: dict) -> dict:
    """Modify the version-specific settings of a Lambda function. When you update a function, Lambda provisions an instance of the function and its supporting resources. If your function connects to a VPC, t"""
    function_name = request.get("FunctionName", "").strip() if isinstance(request.get("FunctionName"), str) else request.get("FunctionName")
    if not function_name:
        raise ValidationException("FunctionName is required")

    resource = store.function_configurations(function_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource function_name not found")

    # Update mutable fields
    if "Role" in request:
        resource["Role"] = role
    if "Handler" in request:
        resource["Handler"] = handler
    if "Description" in request:
        resource["Description"] = description
    if "Timeout" in request:
        resource["Timeout"] = timeout
    if "MemorySize" in request:
        resource["MemorySize"] = memory_size
    if "VpcConfig" in request:
        resource["VpcConfig"] = vpc_config
    if "Environment" in request:
        resource["Environment"] = environment
    if "Runtime" in request:
        resource["Runtime"] = runtime
    if "DeadLetterConfig" in request:
        resource["DeadLetterConfig"] = dead_letter_config
    if "KMSKeyArn" in request:
        resource["KMSKeyArn"] = kms_key_arn
    if "TracingConfig" in request:
        resource["TracingConfig"] = tracing_config
    if "RevisionId" in request:
        resource["RevisionId"] = revision_id
    if "Layers" in request:
        resource["Layers"] = layers
    if "FileSystemConfigs" in request:
        resource["FileSystemConfigs"] = file_system_configs
    if "ImageConfig" in request:
        resource["ImageConfig"] = image_config
    if "EphemeralStorage" in request:
        resource["EphemeralStorage"] = ephemeral_storage
    if "SnapStart" in request:
        resource["SnapStart"] = snap_start
    if "LoggingConfig" in request:
        resource["LoggingConfig"] = logging_config
    if "CapacityProviderConfig" in request:
        resource["CapacityProviderConfig"] = capacity_provider_config
    if "DurableConfig" in request:
        resource["DurableConfig"] = durable_config

    store.function_configurations(function_name, resource)
    return resource
```
