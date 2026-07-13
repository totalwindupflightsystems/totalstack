---
id: "@specs/aws/lambda/docs/java-context"
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
> **spec:id:** @specs/aws/lambda/docs/java-context
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Using the Lambda context object to retrieve Java function information
<a name="java-context"></a>

When Lambda runs your function, it passes a context object to the [handler](java-handler.md). This object provides methods and properties that provide information about the invocation, function, and execution environment.

**Context methods**
+ `getRemainingTimeInMillis()` – Returns the number of milliseconds left before the execution times out.
+ `getFunctionName()` – Returns the name of the Lambda function.
+ `getFunctionVersion()` – Returns the [version](configuration-versions.md) of the function.
+ `getInvokedFunctionArn()` – Returns the Amazon Resource Name (ARN) that's used to invoke the function. Indicates if the invoker specified a version number or alias.
+ `getMemoryLimitInMB()` – Returns the amount of memory that's allocated for the function.
+ `getAwsRequestId()` – Returns the identifier of the invocation request.
+ `getLogGroupName()` – Returns the log group for the function.
+ `getLogStreamName()` – Returns the log stream for the function instance.
+ `getIdentity()` – (mobile apps) Returns information about the Amazon Cognito identity that authorized the request.
+ `getClientContext()` – (mobile apps) Returns the client context that's provided to Lambda by the client application.
+ `getLogger()` – Returns the [logger object](java-logging.md) for the function.

The following example shows a function that uses the context object to access the Lambda logger.

**Example [Handler.java](https://github.com/awsdocs/aws-lambda-developer-guide/tree/main/sample-apps/java-basic/src/main/java/example/Handler.java)**  

```
package example;

import [com.amazonaws.services.lambda.runtime.Context](https://github.com/aws/aws-lambda-java-libs/blob/master/aws-lambda-java-core/src/main/java/com/amazonaws/services/lambda/runtime/Context.java);
import [com.amazonaws.services.lambda.runtime.LambdaLogger](https://github.com/aws/aws-lambda-java-libs/blob/master/aws-lambda-java-core/src/main/java/com/amazonaws/services/lambda/runtime/LambdaLogger.java);
import [com.amazonaws.services.lambda.runtime.RequestHandler](https://github.com/aws/aws-lambda-java-libs/blob/master/aws-lambda-java-core/src/main/java/com/amazonaws/services/lambda/runtime/RequestHandler.java);

import java.util.Map;

// Handler value: example.Handler
public class Handler implements RequestHandler<Map<String,String>, Void>{

  @Override
  public Void handleRequest(Map<String,String> event, Context context)
  {
    LambdaLogger logger = context.getLogger();
    logger.log("EVENT TYPE: " + event.getClass());
    return null;
  }
}
```

The function logs the class type of the incoming event before returning `null`.

**Example log output**  

```
EVENT TYPE: class java.util.LinkedHashMap
```

The interface for the context object is available in the [aws-lambda-java-core](https://github.com/aws/aws-lambda-java-libs/tree/master/aws-lambda-java-core) library. You can implement this interface to create a context class for testing. The following example shows a context class that returns dummy values for most properties and a working test logger.

**Example [src/test/java/example/TestContext.java](https://github.com/awsdocs/aws-lambda-developer-guide/tree/main/sample-apps/java-basic/src/test/java/example/TestContext.java)**  

```
package example;

import [com.amazonaws.services.lambda.runtime.Context](https://github.com/aws/aws-lambda-java-libs/blob/master/aws-lambda-java-core/src/main/java/com/amazonaws/services/lambda/runtime/Context.java);
import [com.amazonaws.services.lambda.runtime.CognitoIdentity](https://github.com/aws/aws-lambda-java-libs/blob/master/aws-lambda-java-core/src/main/java/com/amazonaws/services/lambda/runtime/CognitoIdentity.java);
import [com.amazonaws.services.lambda.runtime.ClientContext](https://github.com/aws/aws-lambda-java-libs/blob/master/aws-lambda-java-core/src/main/java/com/amazonaws/services/lambda/runtime/ClientContext.java);
import [com.amazonaws.services.lambda.runtime.LambdaLogger](https://github.com/aws/aws-lambda-java-libs/blob/master/aws-lambda-java-core/src/main/java/com/amazonaws/services/lambda/runtime/LambdaLogger.java);

public class TestContext implements Context{

  public TestContext() {}
  public String getAwsRequestId(){
    return new String("495b12a8-xmpl-4eca-8168-160484189f99");
  }
  public String getLogGroupName(){
    return new String("/aws/lambda/my-function");
  }
  public String getLogStreamName(){
    return new String("2020/02/26/[$LATEST]704f8dxmpla04097b9134246b8438f1a");
  }
  public String getFunctionName(){
    return new String("my-function");
  }
  public String getFunctionVersion(){
    return new String("$LATEST");
  }
  public String getInvokedFunctionArn(){
    return new String("arn:aws:lambda:us-east-2:123456789012:function:my-function");
  }
  public CognitoIdentity getIdentity(){
    return null;
  }
  public ClientContext getClientContext(){
    return null;
  }
  public int getRemainingTimeInMillis(){
    return 300000;
  }
  public int getMemoryLimitInMB(){
    return 512;
  }
  public LambdaLogger getLogger(){
    return new TestLogger();
  }

}
```

For more information on logging, see [Log and monitor Java Lambda functions](java-logging.md).

## Context in sample applications
<a name="java-context-samples"></a>

The GitHub repository for this guide includes sample applications that demonstrate the use of the context object. Each sample application includes scripts for easy deployment and cleanup, an AWS Serverless Application Model (AWS SAM) template, and supporting resources.

**Sample Lambda applications in Java**
+ [example-java](https://github.com/awsdocs/aws-lambda-developer-guide/tree/main/sample-apps/example-java) – A Java function that demonstrates how you can use Lambda to process orders. This function illustrates how to define and deserialize a custom input event object, use the AWS SDK, and output logging.
+ [java-basic](https://github.com/awsdocs/aws-lambda-developer-guide/tree/main/sample-apps/java-basic) – A collection of minimal Java functions with unit tests and variable logging configuration.
+ [java-events](https://github.com/awsdocs/aws-lambda-developer-guide/tree/main/sample-apps/java-events) – A collection of Java functions that contain skeleton code for how to handle events from various services such as Amazon API Gateway, Amazon SQS, and Amazon Kinesis. These functions use the latest version of the [aws-lambda-java-events](java-package.md) library (3.0.0 and newer). These examples do not require the AWS SDK as a dependency.
+ [s3-java](https://github.com/awsdocs/aws-lambda-developer-guide/tree/main/sample-apps/s3-java) – A Java function that processes notification events from Amazon S3 and uses the Java Class Library (JCL) to create thumbnails from uploaded image files.
+ [layer-java](https://github.com/awsdocs/aws-lambda-developer-guide/tree/main/sample-apps/layer-java) – A Java function that illustrates how to use a Lambda layer to package dependencies separate from your core function code.