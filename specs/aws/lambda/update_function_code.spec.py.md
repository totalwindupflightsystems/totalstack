---
id: "@specs/aws/lambda/update_function_code"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_UpdateFunctionCode"
---

# UpdateFunctionCode

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/update_function_code
> **spec:implements:** @kind:operation UpdateFunctionCode
> **AWS Protocol:** rest-json
> **HTTP:** PUT /2015-03-31/functions/{FunctionName}/code
> **@ref:** specs/aws/lambda/docs/API_UpdateFunctionCode.spec.md

Updates a Lambda function's code. If code signing is enabled for the function, the code package must be signed by a trusted publisher. For more information, see Configuring code signing for Lambda . If the function's package type is Image , then you must specify the code package in ImageUri as the URI of a container image in the Amazon ECR registry. If the function's package type is Zip , then you must specify the deployment package as a .zip file archive . Enter the Amazon S3 bucket and key of the code .zip file location. You can also provide the function code inline using the ZipFile field. The code in the deployment package must be compatible with the target instruction set architecture of the function ( x86-64 or arm64 ). The function's code is locked when you publish a version. You can't modify the code of a published version, only the unpublished version. For a function defined as a container image, Lambda resolves the image tag to an image digest. In Amazon ECR, if you update the image tag to a new image, Lambda does not automatically update the function.

## Input Shape: UpdateFunctionCodeRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Architectures | list[Any  # complex shape] |  | The instruction set architecture that the function supports. Enter a string array with one of the valid values (arm64 or |
| DryRun | bool |  | Set to true to validate the request parameters and access permissions without modifying the function code. |
| FunctionName | Any  # complex shape | ✓ | The name or ARN of the Lambda function. Name formats Function name – my-function . Function ARN – arn:aws:lambda:us-west |
| ImageUri | str |  | URI of a container image in the Amazon ECR registry. Do not use for a function defined with a .zip file archive. |
| Publish | bool |  | Set to true to publish a new version of the function after updating the code. This has the same effect as calling Publis |
| PublishTo | Any  # complex shape |  | Specifies where to publish the function version or configuration. |
| RevisionId | str |  | Update the function only if the revision ID matches the ID that's specified. Use this option to avoid modifying a functi |
| S3Bucket | Any  # complex shape |  | An Amazon S3 bucket in the same Amazon Web Services Region as your function. The bucket can be in a different Amazon Web |
| S3Key | Any  # complex shape |  | The Amazon S3 key of the deployment package. Use only with a function defined with a .zip file archive deployment packag |
| S3ObjectVersion | Any  # complex shape |  | For versioned objects, the version of the deployment package object to use. |
| SourceKMSKeyArn | Any  # complex shape |  | The ARN of the Key Management Service (KMS) customer managed key that's used to encrypt your function's .zip deployment  |
| ZipFile | bytes |  | The base64-encoded contents of the deployment package. Amazon Web Services SDK and CLI clients handle the encoding for y |

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
- **PreconditionFailedException**: The RevisionId provided does not match the latest RevisionId for the Lambda function or alias. For AddPermission and RemovePermission API operations: Call GetPolicy to retrieve the latest RevisionId f

## Implementation

```speclang
def update_function_code(store, request: dict) -> dict:
    """Updates a Lambda function's code. If code signing is enabled for the function, the code package must be signed by a trusted publisher. For more information, see Configuring code signing for Lambda . I"""
    function_name = request.get("FunctionName", "").strip() if isinstance(request.get("FunctionName"), str) else request.get("FunctionName")
    if not function_name:
        raise ValidationException("FunctionName is required")

    resource = store.function_codes(function_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource function_name not found")

    # Update mutable fields
    if "ZipFile" in request:
        resource["ZipFile"] = zip_file
    if "S3Bucket" in request:
        resource["S3Bucket"] = s3_bucket
    if "S3Key" in request:
        resource["S3Key"] = s3_key
    if "S3ObjectVersion" in request:
        resource["S3ObjectVersion"] = s3_object_version
    if "ImageUri" in request:
        resource["ImageUri"] = image_uri
    if "Publish" in request:
        resource["Publish"] = publish
    if "DryRun" in request:
        resource["DryRun"] = dry_run
    if "RevisionId" in request:
        resource["RevisionId"] = revision_id
    if "Architectures" in request:
        resource["Architectures"] = architectures
    if "SourceKMSKeyArn" in request:
        resource["SourceKMSKeyArn"] = source_kms_key_arn
    if "PublishTo" in request:
        resource["PublishTo"] = publish_to

    store.function_codes(function_name, resource)
    return resource
```
