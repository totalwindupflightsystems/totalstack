---
id: "@specs/aws/lambda/create_function"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_CreateFunction"
---

# CreateFunction

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/create_function
> **spec:implements:** @kind:operation CreateFunction
> **AWS Protocol:** rest-json
> **HTTP:** POST /2015-03-31/functions
> **@ref:** specs/aws/lambda/docs/API_CreateFunction.spec.md

Creates a Lambda function. To create a function, you need a deployment package and an execution role . The deployment package is a .zip file archive or container image that contains your function code. The execution role grants the function permission to use Amazon Web Services services, such as Amazon CloudWatch Logs for log streaming and X-Ray for request tracing. If the deployment package is a container image , then you set the package type to Image . For a container image, the code property must include the URI of a container image in the Amazon ECR registry. You do not need to specify the handler and runtime properties. If the deployment package is a .zip file archive , then you set the package type to Zip . For a .zip file archive, the code property specifies the location of the .zip file. You must also specify the handler and runtime properties. The code in the deployment package must be compatible with the target instruction set architecture of the function ( x86-64 or arm64 ). If you do not specify the architecture, then the default value is x86-64 . When you create a function, Lambda provisions an instance of the function and its supporting resources. If your function connects to a VPC, this process can take a minute or so. During this time, you can't invoke or modify the function. The State , StateReason , and StateReasonCode fields in the response from GetFunctionConfiguration indicate when the function is ready to invoke. For more information, see Lambda function states . A function has an unpublished version, and can have published versions and aliases. The unpublished version changes when you update your function's code and configuration. A published version is a snapshot of your function code and configuration that can't be changed. An alias is a named resource that maps to a version, and can be changed to map to a different version. Use the Publish parameter to create version 1 of your function from its initial configuration. The other parameters let you configure version-specific and function-level settings. You can modify version-specific settings later with UpdateFunctionConfiguration . Function-level settings apply to both the unpublished and published versions of the function, and include tags ( TagResource ) and per-function concurrency limits ( PutFunctionConcurrency ). You can use code signing if your deployment package is a .zip file archive. To enable code signing for this function, specify the ARN of a code-signing configuration. When a user attempts to deploy a code package with UpdateFunctionCode , Lambda checks that the code package has a valid signature from a trusted publisher. The code-signing configuration includes set of signing profiles, which define the trusted publishers for this function. If another Amazon Web Services account or an Amazon Web Services service invokes your function, use AddPermission to grant permission by creating a resource-based Identity and Access Management (IAM) policy. You can grant permissions at the function level, on a version, or on an alias. To invoke your function directly, use Invoke . To invoke your function in response to events in other Amazon Web Services services, create an event source mapping ( CreateEventSourceMapping ), or configure a function trigger in the other service. For more information, see Invoking Lambda functions .

## Input Shape: CreateFunctionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Architectures | list[Any  # complex shape] |  | The instruction set architecture that the function supports. Enter a string array with one of the valid values (arm64 or |
| CapacityProviderConfig | Any  # complex shape |  | Configuration for the capacity provider that manages compute resources for Lambda functions. |
| Code | Any  # complex shape | ✓ | The code for the function. |
| CodeSigningConfigArn | Any  # complex shape |  | To enable code signing for this function, specify the ARN of a code-signing configuration. A code-signing configuration  |
| DeadLetterConfig | Any  # complex shape |  | A dead-letter queue configuration that specifies the queue or topic where Lambda sends asynchronous events when they fai |
| Description | Any  # complex shape |  | A description of the function. |
| DurableConfig | Any  # complex shape |  | Configuration settings for durable functions. Enables creating functions with durability that can remember their state a |
| Environment | Any  # complex shape |  | Environment variables that are accessible from function code during execution. |
| EphemeralStorage | Any  # complex shape |  | The size of the function's /tmp directory in MB. The default value is 512, but can be any whole number between 512 and 1 |
| FileSystemConfigs | list[Any  # complex shape] |  | Connection settings for an Amazon EFS file system. |
| FunctionName | Any  # complex shape | ✓ | The name or ARN of the Lambda function. Name formats Function name – my-function . Function ARN – arn:aws:lambda:us-west |
| Handler | Any  # complex shape |  | The name of the method within your code that Lambda calls to run your function. Handler is required if the deployment pa |
| ImageConfig | Any  # complex shape |  | Container image configuration values that override the values in the container image Dockerfile. |
| KMSKeyArn | Any  # complex shape |  | The ARN of the Key Management Service (KMS) customer managed key that's used to encrypt the following resources: The fun |
| Layers | list[Any  # complex shape] |  | A list of function layers to add to the function's execution environment. Specify each layer by its ARN, including the v |
| LoggingConfig | Any  # complex shape |  | The function's Amazon CloudWatch Logs configuration settings. |
| MemorySize | Any  # complex shape |  | The amount of memory available to the function at runtime. Increasing the function memory also increases its CPU allocat |
| PackageType | Any  # complex shape |  | The type of deployment package. Set to Image for container image and set to Zip for .zip file archive. |
| Publish | bool |  | Set to true to publish the first version of the function during creation. |
| PublishTo | Any  # complex shape |  | Specifies where to publish the function version or configuration. |
| Role | Any  # complex shape | ✓ | The Amazon Resource Name (ARN) of the function's execution role. |
| Runtime | Any  # complex shape |  | The identifier of the function's runtime . Runtime is required if the deployment package is a .zip file archive. Specify |
| SnapStart | Any  # complex shape |  | The function's SnapStart setting. |
| Tags | Any  # complex shape |  | A list of tags to apply to the function. |
| TenancyConfig | Any  # complex shape |  | Configuration for multi-tenant applications that use Lambda functions. Defines tenant isolation settings and resource al |
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
- **CodeStorageExceededException**: Your Amazon Web Services account has exceeded its maximum total code size. For more information, see Lambda quotas .
- **FunctionVersionsPerCapacityProviderLimitExceededException**: The maximum number of function versions that can be associated with a single capacity provider has been exceeded. For more information, see Lambda quotas .

## Implementation

```speclang
def create_function(store, request: dict) -> dict:
    """Creates a Lambda function. To create a function, you need a deployment package and an execution role . The deployment package is a .zip file archive or container image that contains your function code"""
    code = request.get("Code", "").strip() if isinstance(request.get("Code"), str) else request.get("Code")
    if not code:
        raise ValidationException("Code is required")
    function_name = request.get("FunctionName", "").strip() if isinstance(request.get("FunctionName"), str) else request.get("FunctionName")
    if not function_name:
        raise ValidationException("FunctionName is required")
    role = request.get("Role", "").strip() if isinstance(request.get("Role"), str) else request.get("Role")
    if not role:
        raise ValidationException("Role is required")

    if store.functions(function_name):
        raise ResourceInUseException(f"Resource function_name already exists")

    record = {
        "FunctionName": function_name,
        "Runtime": runtime,
        "Role": role,
        "Handler": handler,
        "Code": code,
        "Description": description,
        "Timeout": timeout,
        "MemorySize": memory_size,
        "Publish": publish,
        "VpcConfig": vpc_config,
        "PackageType": package_type,
        "DeadLetterConfig": dead_letter_config,
        "Environment": environment,
        "KMSKeyArn": kms_key_arn,
        "TracingConfig": tracing_config,
        "Tags": tags,
        "Layers": layers,
        "FileSystemConfigs": file_system_configs,
        "ImageConfig": image_config,
        "CodeSigningConfigArn": code_signing_config_arn,
        "Architectures": architectures,
        "EphemeralStorage": ephemeral_storage,
        "SnapStart": snap_start,
        "LoggingConfig": logging_config,
        "CapacityProviderConfig": capacity_provider_config,
        "PublishTo": publish_to,
        "DurableConfig": durable_config,
        "TenancyConfig": tenancy_config,
    }

    store.functions(function_name, record)

    return {
        "FunctionName": function_name,
        "FunctionArn": record.get("FunctionArn", {}),
        "Runtime": record.get("Runtime", {}),
        "Role": record.get("Role", {}),
        "Handler": record.get("Handler", {}),
        "CodeSize": record.get("CodeSize", {}),
        "Description": record.get("Description", {}),
        "Timeout": record.get("Timeout", {}),
        "MemorySize": record.get("MemorySize", {}),
        "LastModified": record.get("LastModified", {}),
        "CodeSha256": record.get("CodeSha256", {}),
        "Version": record.get("Version", {}),
        "VpcConfig": record.get("VpcConfig", {}),
        "DeadLetterConfig": record.get("DeadLetterConfig", {}),
        "Environment": record.get("Environment", {}),
        "KMSKeyArn": record.get("KMSKeyArn", {}),
        "TracingConfig": record.get("TracingConfig", {}),
        "MasterArn": record.get("MasterArn", {}),
        "RevisionId": record.get("RevisionId", {}),
        "Layers": record.get("Layers", {}),
        "State": record.get("State", {}),
        "StateReason": record.get("StateReason", {}),
        "StateReasonCode": record.get("StateReasonCode", {}),
        "LastUpdateStatus": record.get("LastUpdateStatus", {}),
        "LastUpdateStatusReason": record.get("LastUpdateStatusReason", {}),
        "LastUpdateStatusReasonCode": record.get("LastUpdateStatusReasonCode", {}),
        "FileSystemConfigs": record.get("FileSystemConfigs", {}),
        "PackageType": record.get("PackageType", {}),
        "ImageConfigResponse": record.get("ImageConfigResponse", {}),
        "SigningProfileVersionArn": record.get("SigningProfileVersionArn", {}),
        "SigningJobArn": record.get("SigningJobArn", {}),
        "Architectures": record.get("Architectures", {}),
        "EphemeralStorage": record.get("EphemeralStorage", {}),
        "SnapStart": record.get("SnapStart", {}),
        "RuntimeVersionConfig": record.get("RuntimeVersionConfig", {}),
        "LoggingConfig": record.get("LoggingConfig", {}),
        "CapacityProviderConfig": record.get("CapacityProviderConfig", {}),
        "ConfigSha256": record.get("ConfigSha256", {}),
        "DurableConfig": record.get("DurableConfig", {}),
        "TenancyConfig": record.get("TenancyConfig", {}),
    }
```
