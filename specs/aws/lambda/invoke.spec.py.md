---
id: "@specs/aws/lambda/invoke"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_Invoke"
---

# Invoke

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/invoke
> **spec:implements:** @kind:operation Invoke
> **AWS Protocol:** rest-json
> **HTTP:** POST /2015-03-31/functions/{FunctionName}/invocations
> **@ref:** specs/aws/lambda/docs/API_Invoke.spec.md

Invokes a Lambda function. You can invoke a function synchronously (and wait for the response), or asynchronously. By default, Lambda invokes your function synchronously (i.e. the InvocationType is RequestResponse ). To invoke a function asynchronously, set InvocationType to Event . Lambda passes the ClientContext object to your function for synchronous invocations only. For synchronous invocations, the maximum payload size is 6 MB. For asynchronous invocations, the maximum payload size is 1 MB. For synchronous invocation , details about the function response, including errors, are included in the response body and headers. For either invocation type, you can find more information in the execution log and trace . When an error occurs, your function may be invoked multiple times. Retry behavior varies by error type, client, event source, and invocation type. For example, if you invoke a function asynchronously and it returns an error, Lambda executes the function up to two more times. For more information, see Error handling and automatic retries in Lambda . For asynchronous invocation , Lambda adds events to a queue before sending them to your function. If your function does not have enough capacity to keep up with the queue, events may be lost. Occasionally, your function may receive the same event multiple times, even if no error occurs. To retain events that were not processed, configure your function with a dead-letter queue . The status code in the API response doesn't reflect function errors. Error codes are reserved for errors that prevent your function from executing, such as permissions errors, quota errors, or issues with your function's code and configuration. For example, Lambda returns TooManyRequestsException if running the function would cause you to exceed a concurrency limit at either the account level ( ConcurrentInvocationLimitExceeded ) or function level ( ReservedFunctionConcurrentInvocationLimitExceeded ). For functions with a long timeout, your client might disconnect during synchronous invocation while it waits for a response. Configure your HTTP client, SDK, firewall, proxy, or operating system to allow for long connections with timeout or keep-alive settings. This operation requires permission for the lambda:InvokeFunction action. For details on how to set up permissions for cross-account invocations, see Granting function access to other accounts .

## Input Shape: InvocationRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientContext | str |  | Up to 3,583 bytes of base64-encoded data about the invoking client to pass to the function in the context object. Lambda |
| DurableExecutionName | Any  # complex shape |  | Optional unique name for the durable execution. When you start your special function, you can give it a unique name to i |
| FunctionName | Any  # complex shape | ✓ | The name or ARN of the Lambda function, version, or alias. Name formats Function name – my-function (name-only), my-func |
| InvocationType | Any  # complex shape |  | Choose from the following options. RequestResponse (default) – Invoke the function synchronously. Keep the connection op |
| LogType | Any  # complex shape |  | Set to Tail to include the execution log in the response. Applies to synchronously invoked functions only. |
| Payload | bytes |  | The JSON that you want to provide to your Lambda function as input. The maximum payload size is 6 MB for synchronous inv |
| Qualifier | Any  # complex shape |  | Specify a version or alias to invoke a published version of the function. |
| TenantId | Any  # complex shape |  | The identifier of the tenant in a multi-tenant Lambda function. |

## Output Shape: InvocationResponse

- **DurableExecutionArn** (Any  # complex shape): The ARN of the durable execution that was started. This is returned when invoking a durable function and provides a uniq
- **ExecutedVersion** (Any  # complex shape): The version of the function that executed. When you invoke a function with an alias, this indicates which version the al
- **FunctionError** (str): If present, indicates that an error occurred during function execution. Details about the error are included in the resp
- **LogResult** (str): The last 4 KB of the execution log, which is base64-encoded.
- **Payload** (bytes): The response from the function, or an error object.
- **StatusCode** (int): The HTTP status code is in the 200 range for a successful request. For the RequestResponse invocation type, this status 

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
def invoke(store, request: dict) -> dict:
    """Invokes a Lambda function. You can invoke a function synchronously (and wait for the response), or asynchronously. By default, Lambda invokes your function synchronously (i.e. the InvocationType is Re"""
    function_name = request.get("FunctionName", "").strip() if isinstance(request.get("FunctionName"), str) else request.get("FunctionName")
    if not function_name:
        raise ValidationException("FunctionName is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("Invoke", request)
```
