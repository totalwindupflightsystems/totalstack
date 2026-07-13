---
id: "@specs/aws/lambda/docs/typescript-context"
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
> **spec:id:** @specs/aws/lambda/docs/typescript-context
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Using the Lambda context object to retrieve TypeScript function information
<a name="typescript-context"></a>

When Lambda runs your function, it passes a context object to the [handler](typescript-handler.md). This object provides methods and properties that provide information about the invocation, function, and execution environment.

To enable type checking for the context object, you must add the [@types/aws-lambda](https://www.npmjs.com/package/@types/aws-lambda) package as a development dependency and import the `Context` type. For more information, see [Type definitions for Lambda](lambda-typescript.md#typescript-type-definitions).

**Context methods**
+ `getRemainingTimeInMillis()` – Returns the number of milliseconds left before the execution times out.

**Context properties**
+ `functionName` – The name of the Lambda function.
+ `functionVersion` – The [version](configuration-versions.md) of the function.
+ `invokedFunctionArn` – The Amazon Resource Name (ARN) that's used to invoke the function. Indicates if the invoker specified a version number or alias.
+ `memoryLimitInMB` – The amount of memory that's allocated for the function.
+ `awsRequestId` – The identifier of the invocation request.
+ `logGroupName` – The log group for the function.
+ `logStreamName` – The log stream for the function instance.
+ `identity` – (mobile apps) Information about the Amazon Cognito identity that authorized the request.
  + `cognitoIdentityId` – The authenticated Amazon Cognito identity.
  + `cognitoIdentityPoolId` – The Amazon Cognito identity pool that authorized the invocation.
+ `clientContext` – (mobile apps) Client context that's provided to Lambda by the client application.
  + `client.installation_id`
  + `client.app_title`
  + `client.app_version_name`
  + `client.app_version_code`
  + `client.app_package_name`
  + `env.platform_version`
  + `env.platform`
  + `env.make`
  + `env.model`
  + `env.locale`
  + `Custom` – Custom values that are set by the client application. 
+ `callbackWaitsForEmptyEventLoop` – By default (`true`), when using a callback-based function handler, Lambda waits for the event loop to be empty after the callback runs before ending the function invoke. Set to `false` to send the response and end the invoke immediately after the callback runs instead of waiting for the event loop to be empty. Outstanding events continue to run during the next invocation. Note that Lambda supports callback-based function handlers for Node.js 22 and earlier runtimes only.

**Example index.ts file**  
The following example function logs context information and returns the location of the logs.  
Before using this code in a Lambda function, you must add the [@types/aws-lambda](https://www.npmjs.com/package/@types/aws-lambda) package as a development dependency. This package contains the type definitions for Lambda. For more information, see [Type definitions for Lambda](lambda-typescript.md#typescript-type-definitions).

```
import { Context } from 'aws-lambda';
export const lambdaHandler = async (event: string, context: Context): Promise<string> => {
  console.log('Remaining time: ', context.getRemainingTimeInMillis());
  console.log('Function name: ', context.functionName);
  return context.logStreamName;
};
```