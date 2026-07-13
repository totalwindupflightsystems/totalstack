---
id: "@specs/aws/lambda/docs/powershell-context"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Context"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Context

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/powershell-context
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Using the Lambda context object to retrieve PowerShell function information
<a name="powershell-context"></a>

When Lambda runs your function, it passes context information by making a `$LambdaContext` variable available to the [handler](powershell-handler.md). This variable provides methods and properties with information about the invocation, function, and execution environment.

**Context properties**
+ `FunctionName` – The name of the Lambda function.
+ `FunctionVersion` – The [version](configuration-versions.md) of the function.
+ `InvokedFunctionArn` – The Amazon Resource Name (ARN) that's used to invoke the function. Indicates if the invoker specified a version number or alias.
+ `MemoryLimitInMB` – The amount of memory that's allocated for the function.
+ `AwsRequestId` – The identifier of the invocation request.
+ `LogGroupName` – The log group for the function.
+ `LogStreamName` – The log stream for the function instance.
+ `RemainingTime` – The number of milliseconds left before the execution times out.
+ `Identity` – (mobile apps) Information about the Amazon Cognito identity that authorized the request.
+ `ClientContext` – (mobile apps) Client context that's provided to Lambda by the client application.
+ `Logger` – The [logger object](powershell-logging.md) for the function.

The following PowerShell code snippet shows a simple handler function that prints some of the context information. 

```
#Requires -Modules @{ModuleName='AWSPowerShell.NetCore';ModuleVersion='3.3.618.0'}
Write-Host 'Function name:' $LambdaContext.FunctionName
Write-Host 'Remaining milliseconds:' $LambdaContext.RemainingTime.TotalMilliseconds
Write-Host 'Log group name:' $LambdaContext.LogGroupName
Write-Host 'Log stream name:' $LambdaContext.LogStreamName
```