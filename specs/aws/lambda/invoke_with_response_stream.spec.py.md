---
id: "@specs/aws/lambda/invoke_with_response_stream"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_InvokeWithResponseStream"
---

# InvokeWithResponseStream

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/invoke_with_response_stream
> **spec:implements:** @kind:operation InvokeWithResponseStream
> **AWS Protocol:** rest-json
> **HTTP:** POST /2021-11-15/functions/{FunctionName}/response-streaming-invocations
> **@ref:** specs/aws/lambda/docs/API_InvokeWithResponseStream.spec.md

Configure your Lambda functions to stream response payloads back to clients. For more information, see Configuring a Lambda function to stream responses . This operation requires permission for the lambda:InvokeFunction action. For details on how to set up permissions for cross-account invocations, see Granting function access to other accounts .

## Input Shape: InvokeWithResponseStreamRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientContext | str |  | Up to 3,583 bytes of base64-encoded data about the invoking client to pass to the function in the context object. |
| FunctionName | Any  # complex shape | ✓ | The name or ARN of the Lambda function. Name formats Function name – my-function . Function ARN – arn:aws:lambda:us-west |
| InvocationType | Any  # complex shape |  | Use one of the following options: RequestResponse (default) – Invoke the function synchronously. Keep the connection ope |
| LogType | Any  # complex shape |  | Set to Tail to include the execution log in the response. Applies to synchronously invoked functions only. |
| Payload | bytes |  | The JSON that you want to provide to your Lambda function as input. You can enter the JSON directly. For example, --payl |
| Qualifier | Any  # complex shape |  | The alias name. |
| TenantId | Any  # complex shape |  | The identifier of the tenant in a multi-tenant Lambda function. |

## Output Shape: InvokeWithResponseStreamResponse

- **EventStream** (Any  # complex shape): The stream of response payloads.
- **ExecutedVersion** (Any  # complex shape): The version of the function that executed. When you invoke a function with an alias, this indicates which version the al
- **ResponseStreamContentType** (str): The type of data the stream is returning.
- **StatusCode** (int): For a successful request, the HTTP status code is in the 200 range. For the RequestResponse invocation type, this status

## Errors
- **ResourceNotReadyException**: The function is inactive and its VPC connection is no longer available. Wait for the VPC connection to reestablish and try again.
- **InvalidSecurityGroupIDException**: The security group ID provided in the Lambda function VPC configuration is not valid.
- **SnapStartTimeoutException**: Lambda couldn't restore the snapshot within the timeout limit.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **EC2ThrottledException**: Amazon EC2 throttled Lambda during Lambda function initialization using the execution role provided for the function.
- **EFSMountConnectivityException**: The Lambda function couldn't make a network connection to the configured file system.
- **SubnetIPAddressLimitReachedException**: Lambda couldn't set up VPC access for the Lambda function because one or more configured subnets has no available IP addresses.
- **KMSAccessDeniedException**: Lambda couldn't decrypt the environment variables because KMS access was denied. Check the Lambda function's KMS permissions.
- **RequestTooLargeException**: The request payload exceeded the Invoke request body JSON input quota. For more information, see Lambda quotas .
- **KMSDisabledException**: Lambda couldn't decrypt the environment variables because the KMS key used is disabled. Check the Lambda function's KMS key settings.

## Implementation

```speclang
def invoke_with_response_stream(store, request: dict) -> dict:
    """Configure your Lambda functions to stream response payloads back to clients. For more information, see Configuring a Lambda function to stream responses . This operation requires permission for the la"""
    function_name = request.get("FunctionName", "").strip() if isinstance(request.get("FunctionName"), str) else request.get("FunctionName")
    if not function_name:
        raise ValidationException("FunctionName is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("InvokeWithResponseStream", request)
```
