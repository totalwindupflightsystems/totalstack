---
id: "@specs/aws/lambda/docs/python-context"
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
> **spec:id:** @specs/aws/lambda/docs/python-context
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Using the Lambda context object to retrieve Python function information
<a name="python-context"></a>

When Lambda runs your function, it passes a context object to the [handler](python-handler.md). This object provides methods and properties that provide information about the invocation, function, and execution environment. For more information on how the context object is passed to the function handler, see [Define Lambda function handler in Python](python-handler.md).

**Context methods**
+ `get_remaining_time_in_millis` – Returns the number of milliseconds left before the execution times out.

**Context properties**
+ `function_name` – The name of the Lambda function.
+ `function_version` – The [version](configuration-versions.md) of the function.
+ `invoked_function_arn` – The Amazon Resource Name (ARN) that's used to invoke the function. Indicates if the invoker specified a version number or alias.
+ `memory_limit_in_mb` – The amount of memory that's allocated for the function.
+ `aws_request_id` – The identifier of the invocation request.
+ `log_group_name` – The log group for the function.
+ `log_stream_name` – The log stream for the function instance.
+ `identity` – (mobile apps) Information about the Amazon Cognito identity that authorized the request.
  + `cognito_identity_id` – The authenticated Amazon Cognito identity.
  + `cognito_identity_pool_id` – The Amazon Cognito identity pool that authorized the invocation.
+ `client_context` – (mobile apps) Client context that's provided to Lambda by the client application.
  + `client.installation_id`
  + `client.app_title`
  + `client.app_version_name`
  + `client.app_version_code`
  + `client.app_package_name`
  + `custom` – A `dict` of custom values set by the mobile client application.
  + `env` – A `dict` of environment information provided by the AWS SDK.

Powertools for Lambda (Python) provides an interface definition for the Lambda context object. You can use the interface definition for type hints, or to further inspect the structure of the Lambda context object. For the interface definition, see [lambda\_context.py](https://github.com/aws-powertools/powertools-lambda-python/blob/develop/aws_lambda_powertools/utilities/typing/lambda_context.py) in the *powertools-lambda-python* repository on GitHub.

The following example shows a handler function that logs context information.

**Example handler.py**  

```
import time

def lambda_handler(event, context):   
    print("Lambda function ARN:", context.invoked_function_arn)
    print("CloudWatch log stream name:", context.log_stream_name)
    print("CloudWatch log group name:",  context.log_group_name)
    print("Lambda Request ID:", context.aws_request_id)
    print("Lambda function memory limits in MB:", context.memory_limit_in_mb)
    # We have added a 1 second delay so you can see the time remaining in get_remaining_time_in_millis.
    time.sleep(1) 
    print("Lambda time remaining in MS:", context.get_remaining_time_in_millis())
```

In addition to the options listed above, you can also use the AWS X-Ray SDK for [Instrumenting Python code in AWS Lambda](python-tracing.md) to identify critical code paths, trace their performance and capture the data for analysis. 