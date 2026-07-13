---
id: "@specs/aws/lambda/docs/golang-context"
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
> **spec:id:** @specs/aws/lambda/docs/golang-context
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Using the Lambda context object to retrieve Go function information
<a name="golang-context"></a>

In Lambda, the context object provides methods and properties with information about the invocation, function, and execution environment. When Lambda runs your function, it passes a context object to the [handler](golang-handler.md). To use the context object in your handler, you can optionally declare it as an input parameter to your handler. The context object is necessary if you want to do the following in your handler:
+ You need access to any of the [global variables, methods, or properties](#golang-context-library) offered by the context object. These methods and properties are useful for tasks like determining the entity that invoked your function or measuring the invocation time of your function, as illustrated in [Accessing invoke context information](#golang-context-access).
+ You need to use the AWS SDK for Go to make calls to other services. The context object is an important input parameter to most of these calls. For more information, see [Using the context in AWS SDK client initializations and calls](#golang-context-sdk).

**Topics**
+ [Supported variables, methods, and properties in the context object](#golang-context-library)
+ [Accessing invoke context information](#golang-context-access)
+ [Using the context in AWS SDK client initializations and calls](#golang-context-sdk)

## Supported variables, methods, and properties in the context object
<a name="golang-context-library"></a>

The Lambda context library provides the following global variables, methods, and properties.

**Global variables**
+ `FunctionName` – The name of the Lambda function.
+ `FunctionVersion` – The [version](configuration-versions.md) of the function.
+ `MemoryLimitInMB` – The amount of memory that's allocated for the function.
+ `LogGroupName` – The log group for the function.
+ `LogStreamName` – The log stream for the function instance.

**Context methods**
+ `Deadline` – Returns the date that the execution times out, in Unix time milliseconds.

**Context properties**
+ `InvokedFunctionArn` – The Amazon Resource Name (ARN) that's used to invoke the function. Indicates if the invoker specified a version number or alias.
+ `AwsRequestID` – The identifier of the invocation request.
+ `Identity` – (mobile apps) Information about the Amazon Cognito identity that authorized the request.
+ `ClientContext` – (mobile apps) Client context that's provided to Lambda by the client application.

## Accessing invoke context information
<a name="golang-context-access"></a>

Lambda functions have access to metadata about their environment and the invocation request. This can be accessed at [Package context](https://golang.org/pkg/context/). Should your handler include `context.Context` as a parameter, Lambda will insert information about your function into the context's `Value` property. Note that you need to import the `lambdacontext` library to access the contents of the `context.Context` object.

```
package main
 
import (
        "context"
        "log"
        "github.com/aws/aws-lambda-go/lambda"
        "github.com/aws/aws-lambda-go/lambdacontext"
)
 
func CognitoHandler(ctx context.Context) {
        lc, _ := lambdacontext.FromContext(ctx)
        log.Print(lc.Identity.CognitoIdentityPoolID)
}
 
func main() {
        lambda.Start(CognitoHandler)
}
```

In the example above, `lc` is the variable used to consume the information that the context object captured and `log.Print(lc.Identity.CognitoIdentityPoolID)` prints that information, in this case, the CognitoIdentityPoolID.

The following example introduces how to use the context object to monitor how long your Lambda function takes to complete. This allows you to analyze performance expectations and adjust your function code accordingly, if needed. 

```
package main

import (
        "context"
        "log"
        "time"
        "github.com/aws/aws-lambda-go/lambda"
)

func LongRunningHandler(ctx context.Context) (string, error) {

        deadline, _ := ctx.Deadline()
        deadline = deadline.Add(-100 * time.Millisecond)
        timeoutChannel := time.After(time.Until(deadline))

        for {

                select {

                case <- timeoutChannel:
                        return "Finished before timing out.", nil

                default:
                        log.Print("hello!")
                        time.Sleep(50 * time.Millisecond)
                }
        }
}

func main() {
        lambda.Start(LongRunningHandler)
}
```

## Using the context in AWS SDK client initializations and calls
<a name="golang-context-sdk"></a>

If your handler needs to use the AWS SDK for Go to make calls to other services, include the context object as an input to your handler. In AWS, it's a best practice to pass in the context object in most AWS SDK calls. For example, the Amazon S3 `PutObject` call accepts the context object (`ctx`) as its first argument:

```
// Upload an object to S3
    _, err = s3Client.PutObject(ctx, &s3.PutObjectInput{
        ...
    })
```

To initialize your SDK clients properly, you can also use the context object to load the correct configuration before passing that configuration object to the client:

```
// Load AWS SDK configuration using the default credential provider chain
    cfg, err := config.LoadDefaultConfig(ctx)
    ...
    s3Client = s3.NewFromConfig(cfg)
```

If you want to initialize your SDK clients outside of your main handler (i.e. during the initialization phase), you can pass in a placeholder context object:

```
func init() {
	// Initialize the S3 client outside of the handler, during the init phase
	cfg, err := config.LoadDefaultConfig(context.TODO())
	...
	s3Client = s3.NewFromConfig(cfg)
}
```

If you initialize your clients this way, ensure that you pass in the correct context object in SDK calls from your main handler.