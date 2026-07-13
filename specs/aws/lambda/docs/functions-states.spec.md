---
id: "@specs/aws/lambda/docs/functions-states"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Function states"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Function states

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/functions-states
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Lambda function states
<a name="functions-states"></a>

Lambda includes a [State](https://docs.aws.amazon.com/lambda/latest/api/API_GetFunctionConfiguration.html#lambda-GetFunctionConfiguration-response-State) field in the function configuration for all functions to indicate when your function is ready to invoke. `State` provides information about the current status of the function, including whether you can successfully invoke the function. Function states do not change the behavior of function invocations or how your function runs the code.

**Note**  
Function state definitions differ slightly for [SnapStart](snapstart.md) functions. For more information, see [Lambda SnapStart and function states](snapstart-activate.md#snapstart-function-states).

In many cases, a DynamoDB table is an ideal way to retain state between invocations since it provides low-latency data access and can scale with the Lambda service. You can also store data in [ Amazon EFS for Lambda](https://aws.amazon.com/blogs/compute/using-amazon-efs-for-aws-lambda-in-your-serverless-applications/) if you are using this service, and this provides low-latency access to file system storage.

Function states include:
+ `Pending` – After Lambda creates the function, it sets the state to pending. While in pending state, Lambda attempts to create or configure resources for the function, such as VPC or EFS resources. Lambda does not invoke a function during pending state. Any invocations or other API actions that operate on the function will fail.
+ `Active` – Your function transitions to active state after Lambda completes resource configuration and provisioning. Functions can only be successfully invoked while active.
+ `Failed` – Indicates that resource configuration or provisioning encountered an error. When function creation fails, Lambda sets the function state to failed, and you must delete and recreate the function.
+ `Inactive` – A function becomes inactive when it has been idle long enough for Lambda to reclaim the external resources that were configured for it. When you try to invoke a function that is inactive, the invocation fails and Lambda sets the function to pending state until the function resources are recreated. If Lambda fails to recreate the resources, the function returns to the inactive state. You might need to resolve any errors and redeploy your function to restore it to the active state.

If you are using SDK-based automation workflows or calling Lambda’s service APIs directly, ensure that you check a function's state before invocation to verify that it is active. You can do this with the Lambda API action [GetFunction](https://docs.aws.amazon.com/lambda/latest/api/API_GetFunction.html), or by configuring a waiter using the [AWS SDK for Java 2.0](https://github.com/aws/aws-sdk-java-v2).

```
aws lambda get-function --function-name my-function --query 'Configuration.[State, LastUpdateStatus]'
```

You should see the following output:

```
[
 "Active",
 "Successful" 
]
```

The following operations fail while function creation is pending:
+ [Invoke](https://docs.aws.amazon.com/lambda/latest/api/API_Invoke.html)
+ [UpdateFunctionCode](https://docs.aws.amazon.com/lambda/latest/api/API_UpdateFunctionCode.html)
+ [UpdateFunctionConfiguration](https://docs.aws.amazon.com/lambda/latest/api/API_UpdateFunctionConfiguration.html)
+ [PublishVersion](https://docs.aws.amazon.com/lambda/latest/api/API_PublishVersion.html)

## Function states during updates
<a name="functions-states-updating"></a>

Lambda has two operations for updating functions:
+ [UpdateFunctionCode](https://docs.aws.amazon.com/lambda/latest/api/API_UpdateFunctionCode.html): Updates the function's deployment package
+ [UpdateFunctionConfiguration](https://docs.aws.amazon.com/lambda/latest/api/API_UpdateFunctionConfiguration.html): Updates the function's configuration

Lambda uses the [LastUpdateStatus](https://docs.aws.amazon.com/lambda/latest/api/API_FunctionConfiguration.html#lambda-Type-FunctionConfiguration-LastUpdateStatus) attribute to track the progress of these update operations. While an update is in progress (when `"LastUpdateStatus": "InProgress"`):
+ The function's [State](https://docs.aws.amazon.com/lambda/latest/api/API_GetFunctionConfiguration.html#lambda-GetFunctionConfiguration-response-State) remains `Active`.
+ Invocations continue to use the function's previous code and configuration until the update completes.
+ The following operations fail:
  + [UpdateFunctionCode](https://docs.aws.amazon.com/lambda/latest/api/API_UpdateFunctionCode.html)
  + [UpdateFunctionConfiguration](https://docs.aws.amazon.com/lambda/latest/api/API_UpdateFunctionConfiguration.html)
  + [PublishVersion](https://docs.aws.amazon.com/lambda/latest/api/API_PublishVersion.html)
  + [TagResource](https://docs.aws.amazon.com/lambda/latest/api/API_TagResource.html)

When an update fails (when `"LastUpdateStatus": "Failed"`):
+ The function's [State](https://docs.aws.amazon.com/lambda/latest/api/API_GetFunctionConfiguration.html#lambda-GetFunctionConfiguration-response-State) remains `Active`.
+ Invocations continue to use the function's previous code and configuration.

**Example GetFunctionConfiguration response**  
The following example is the result of [GetFunctionConfiguration](https://docs.aws.amazon.com/lambda/latest/api/API_GetFunctionConfiguration.html) request on a function undergoing an update.  

```
{
    "FunctionName": "my-function",
    "FunctionArn": "arn:aws:lambda:us-east-1:123456789012:function:my-function",
    "Runtime": "nodejs24.x",
    "VpcConfig": {
        "SubnetIds": [
            "subnet-071f712345678e7c8",
            "subnet-07fd123456788a036",
            "subnet-0804f77612345cacf"
        ],
        "SecurityGroupIds": [
            "sg-085912345678492fb"
        ],
        "VpcId": "vpc-08e1234569e011e83"
    },
    "State": "Active",
    "LastUpdateStatus": "InProgress",
    ...
}
```