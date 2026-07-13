---
id: "@specs/aws/lambda/docs/golang-handler"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Handler"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Handler

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/golang-handler
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Define Lambda function handlers in Go
<a name="golang-handler"></a>

The Lambda function *handler* is the method in your function code that processes events. When your function is invoked, Lambda runs the handler method. Your function runs until the handler returns a response, exits, or times out.

This page describes how to work with Lambda function handlers in Go, including project setup, naming conventions, and best practices. This page also includes an example of a Go Lambda function that takes in information about an order, produces a text file receipt, and puts this file in an Amazon Simple Storage Service (Amazon S3) bucket. For information about how to deploy your function after writing it, see [Deploy Go Lambda functions with .zip file archives](golang-package.md) or [Deploy Go Lambda functions with container images](go-image.md).

**Topics**
+ [Setting up your Go handler project](#golang-handler-setup)
+ [Example Go Lambda function code](#golang-example-code)
+ [Handler naming conventions](#golang-handler-naming)
+ [Defining and accessing the input event object](#golang-example-input)
+ [Accessing and using the Lambda context object](#golang-example-context)
+ [Valid handler signatures for Go handlers](#golang-handler-signatures)
+ [Using the AWS SDK for Go v2 in your handler](#golang-example-sdk-usage)
+ [Accessing environment variables](#golang-example-envvars)
+ [Using global state](#golang-handler-state)
+ [Code best practices for Go Lambda functions](#go-best-practices)

## Setting up your Go handler project
<a name="golang-handler-setup"></a>

A Lambda function written in [Go](https://golang.org/) is authored as a Go executable. You can initialize a Go Lambda function project the same way you initialize any other Go project using the following `go mod init` command:

```
go mod init {{example-go}}
```

Here, `example-go` is the module name. You can replace this with anything. This command initializes your project and generates the `go.mod` file that lists your project's dependencies.

Use the `go get` command to add any external dependencies to your project. For example, for all Lambda functions in Go, you must include the [ github.com/aws/aws-lambda-go/lambda](https://github.com/aws/aws-lambda-go/tree/master/lambda) package, which implements the Lambda programming model for Go. Include this package with the following `go get` command:

```
go get github.com/aws/aws-lambda-go
```

Your function code should live in a Go file. In the following example, we name this file `main.go`. In this file, you implement your core function logic in a handler method, as well as a `main()` function that calls this handler.

## Example Go Lambda function code
<a name="golang-example-code"></a>

The following example Go Lambda function code takes in information about an order, produces a text file receipt, and puts this file in an Amazon S3 bucket.

**Example `main.go` Lambda function**  

```
package main

import (
	"context"
	"encoding/json"
	"fmt"
	"log"
	"os"
	"strings"

	"github.com/aws/aws-lambda-go/lambda"
	"github.com/aws/aws-sdk-go-v2/config"
	"github.com/aws/aws-sdk-go-v2/service/s3"
)

type Order struct {
	OrderID string  `json:"order_id"`
	Amount  float64 `json:"amount"`
	Item    string  `json:"item"`
}

var (
	s3Client *s3.Client
)

func init() {
	// Initialize the S3 client outside of the handler, during the init phase
	cfg, err := config.LoadDefaultConfig(context.TODO())
	if err != nil {
		log.Fatalf("unable to load SDK config, %v", err)
	}

	s3Client = s3.NewFromConfig(cfg)
}

func uploadReceiptToS3(ctx context.Context, bucketName, key, receiptContent string) error {
	_, err := s3Client.PutObject(ctx, &s3.PutObjectInput{
		Bucket: &bucketName,
		Key:    &key,
		Body:   strings.NewReader(receiptContent),
	})
	if err != nil {
		log.Printf("Failed to upload receipt to S3: %v", err)
		return err
	}
	return nil
}

func handleRequest(ctx context.Context, event json.RawMessage) error {
	// Parse the input event
	var order Order
	if err := json.Unmarshal(event, &order); err != nil {
		log.Printf("Failed to unmarshal event: %v", err)
		return err
	}

	// Access environment variables
	bucketName := os.Getenv("RECEIPT_BUCKET")
	if bucketName == "" {
		log.Printf("RECEIPT_BUCKET environment variable is not set")
		return fmt.Errorf("missing required environment variable RECEIPT_BUCKET")
	}

	// Create the receipt content and key destination
	receiptContent := fmt.Sprintf("OrderID: %s\nAmount: $%.2f\nItem: %s",
		order.OrderID, order.Amount, order.Item)
	key := "receipts/" + order.OrderID + ".txt"

	// Upload the receipt to S3 using the helper method
	if err := uploadReceiptToS3(ctx, bucketName, key, receiptContent); err != nil {
		return err
	}

	log.Printf("Successfully processed order %s and stored receipt in S3 bucket %s", order.OrderID, bucketName)
	return nil
}

func main() {
	lambda.Start(handleRequest)
}
```

This `main.go` file contains the following sections of code:
+ `package main`: In Go, the package containing your `func main()` function must always be named `main`.
+ `import` block: Use this block to include libraries that your Lambda function requires.
+ `type Order struct {}` block: Define the shape of the expected input event in this Go struct.
+ `var ()` block: Use this block to define any global variables that you'll use in your Lambda function.
+ `func init() {}`: Include any code you want Lambda to run during the during the [initialization phase](lambda-runtime-environment.md#runtimes-lifecycle-ib) in this `init()` method.
+ `func uploadReceiptToS3(...) {}`: This is a helper method that's referenced by the main `handleRequest` handler method.
+ `func handleRequest(ctx context.Context, event json.RawMessage) error {}`: This is the **main handler method**, which contains your main application logic.
+ `func main() {}`: This is a required entry point for your Lambda handler. The argument to the `lambda.Start()` method is your main handler method.

For this function to work properly, its [execution role](lambda-intro-execution-role.md) must allow the `s3:PutObject` action. Also, ensure that you define the `RECEIPT_BUCKET` environment variable. After a successful invocation, the Amazon S3 bucket should contain a receipt file.

## Handler naming conventions
<a name="golang-handler-naming"></a>

For Lambda functions in Go, you can use any name for the handler. In this example, the handler method name is `handleRequest`. To reference the handler value in your code, you can use the `_HANDLER` environment variable.

For Go functions deployed using a [.zip deployment package](golang-package.md), the executable file that contains your function code must be named `bootstrap`. In addition, the `bootstrap` file must be at the root of the .zip file. For Go functions deployed using a [container image](go-image.md#go-image-provided), you can use any name for the executable file.

## Defining and accessing the input event object
<a name="golang-example-input"></a>

JSON is the most common and standard input format for Lambda functions. In this example, the function expects an input similar to the following:

```
{
    "order_id": "12345",
    "amount": 199.99,
    "item": "Wireless Headphones"
}
```

When working with Lambda functions in Go, you can define the shape of the expected input event as a Go struct. In this example, we define a struct to represent an `Order`:

```
type Order struct {
    OrderID string  `json:"order_id"`
    Amount  float64 `json:"amount"`
    Item    string  `json:"item"`
}
```

This struct matches the expected input shape. After you define your struct, you can write a handler signature that takes in a generic JSON type compatible with the [encoding/json standard library](https://pkg.go.dev/encoding/json). You can then deserialize it into your struct using the [func Unmarshal](https://golang.org/pkg/encoding/json/#Unmarshal) function. This is illustrated in the first few lines of the handler:

```
func handleRequest(ctx context.Context, event json.RawMessage) error {
    // Parse the input event
    var order Order
    if err := json.Unmarshal(event, &order); err != nil {
        log.Printf("Failed to unmarshal event: %v", err)
        return err
    ...
}
```

After this deserialization, you can access the fields of the `order` variable. For example, `order.OrderID` retrieves the value of `"order_id"` from the original input.

**Note**  
The `encoding/json` package can access only exported fields. To be exported, field names in the event struct must be capitalized.

## Accessing and using the Lambda context object
<a name="golang-example-context"></a>

The Lambda [context object](golang-context.md) contains information about the invocation, function, and execution environment. In this example, we declared this variable as `ctx` in the handler signature:

```
func handleRequest(ctx context.Context, event json.RawMessage) error {
    ...
}
```

The `ctx context.Context` input is an optional argument in your function handler. For more information about accepted handler signatures, see [Valid handler signatures for Go handlers](#golang-handler-signatures).

If you make calls to other services using the AWS SDK, the context object is required in a few key areas. For example, to properly initialize your SDK clients, you can load the correct AWS SDK configuration using the context object as follows:

```
// Load AWS SDK configuration using the default credential provider chain
    cfg, err := config.LoadDefaultConfig(ctx)
```

SDK calls themselves may require the context object as an input. For example, the `s3Client.PutObject` call accepts the context object as its first argument:

```
// Upload the receipt to S3
    _, err = s3Client.PutObject(ctx, &s3.PutObjectInput{
        ...
    })
```

Outside of AWS SDK requests, you can also use the context object for function monitoring. For more information about the context object, see [Using the Lambda context object to retrieve Go function information](golang-context.md).

## Valid handler signatures for Go handlers
<a name="golang-handler-signatures"></a>

You have several options when building a Lambda function handler in Go, but you must adhere to the following rules:
+ The handler must be a function.
+ The handler may take between 0 and 2 arguments. If there are two arguments, the first argument must implement `context.Context`.
+ The handler may return between 0 and 2 arguments. If there is a single return value, it must implement `error`. If there are two return values, the second value must implement `error`.

The following lists valid handler signatures. `TIn` and `TOut` represent types compatible with the *encoding/json* standard library. For more information, see [func Unmarshal](https://golang.org/pkg/encoding/json/#Unmarshal) to learn how these types are deserialized.
+ 

  ```
  func ()
  ```
+ 

  ```
  func () error
  ```
+ 

  ```
  func () (TOut, error)
  ```
+ 

  ```
  func (TIn) error
  ```
+ 

  ```
  func (TIn) (TOut, error)
  ```
+ 

  ```
  func (context.Context) error
  ```
+ 

  ```
  func (context.Context) (TOut, error)
  ```
+ 

  ```
  func (context.Context, TIn) error
  ```
+ 

  ```
  func (context.Context, TIn) (TOut, error)
  ```

## Using the AWS SDK for Go v2 in your handler
<a name="golang-example-sdk-usage"></a>

Often, you'll use Lambda functions to interact with or make updates to other AWS resources. The simplest way to interface with these resources is to use the [AWS SDK for Go v2](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2).

**Note**  
The AWS SDK for Go (v1) is in maintenance mode, and will reach end-of-support on July 31, 2025. We recommend that you use only the AWS SDK for Go v2 going forward.

To add SDK dependencies to your function, use the `go get` command for the specific SDK clients that you need. In the example code earlier, we used the `config` library and the `s3` library. Add these dependencies by running the following commands in the directory that contains your `go.mod` and `main.go `files:

```
go get github.com/aws/aws-sdk-go-v2/config
go get github.com/aws/aws-sdk-go-v2/service/s3
```

Then, import the dependencies accordingly in your function's import block:

```
import (
    ...
    "github.com/aws/aws-sdk-go-v2/config"
    "github.com/aws/aws-sdk-go-v2/service/s3"
)
```

When using the SDK in your handler, configure your clients with the right settings. The simplest way to do this is to use the [default credential provider chain](https://docs.aws.amazon.com/sdkref/latest/guide/standardized-credentials.html#credentialProviderChain). This example illustrates one way to load this configuration:

```
// Load AWS SDK configuration using the default credential provider chain
    cfg, err := config.LoadDefaultConfig(ctx)
    if err != nil {
        log.Printf("Failed to load AWS SDK config: %v", err)
        return err
    }
```

After loading this configuration into the `cfg` variable, you can pass this variable into client instantiations. The example code instantiates an Amazon S3 client as follows:

```
// Create an S3 client
    s3Client := s3.NewFromConfig(cfg)
```

In this example, we initialized our Amazon S3 client in the `init()` function to avoid having to initialize it every time we invoke our function. The problem is that in the `init()` function, Lambda doesn't have access to the context object. As a workaround, you can pass in a placeholder like `context.TODO()` during the initialization phase. Later, when you make a call using the client, pass in the full context object. This workaround is also described in [Using the context in AWS SDK client initializations and calls](golang-context.md#golang-context-sdk).

After you configure and initialize your SDK client, you can then use it to interact with other AWS services. The example code calls the Amazon S3 `PutObject` API as follows:

```
_, err = s3Client.PutObject(ctx, &s3.PutObjectInput{
    Bucket: &bucketName,
    Key:    &key,
    Body:   strings.NewReader(receiptContent),
})
```

## Accessing environment variables
<a name="golang-example-envvars"></a>

In your handler code, you can reference any [environment variables](configuration-envvars.md) by using the `os.Getenv()` method. In this example, we reference the defined `RECEIPT_BUCKET` environment variable using the following line of code:

```
// Access environment variables
    bucketName := os.Getenv("RECEIPT_BUCKET")
    if bucketName == "" {
        log.Printf("RECEIPT_BUCKET environment variable is not set")
        return fmt.Errorf("missing required environment variable RECEIPT_BUCKET")
    }
```

## Using global state
<a name="golang-handler-state"></a>

To avoid creating new resources every time you invoke your function, you can declare and modify global variables outside of your Lambda function's handler code. You define these global variables in a `var` block or statement. In addition, your handler may declare an `init()` function that is executed during the [initialization phase](lambda-runtime-environment.md#runtimes-lifecycle-ib). The `init` method behaves the same in AWS Lambda as it does in standard Go programs.

## Code best practices for Go Lambda functions
<a name="go-best-practices"></a>

Adhere to the guidelines in the following list to use best coding practices when building your Lambda functions:
+ **Separate the Lambda handler from your core logic.** This allows you to make a more unit-testable function.
+ **Minimize the complexity of your dependencies.** Prefer simpler frameworks that load quickly on [execution environment](lambda-runtime-environment.md) startup.
+ **Minimize your deployment package size to its runtime necessities.** This will reduce the amount of time that it takes for your deployment package to be downloaded and unpacked ahead of invocation.

**Take advantage of execution environment reuse to improve the performance of your function.** Initialize SDK clients and database connections outside of the function handler, and cache static assets locally in the `/tmp` directory. Subsequent invocations processed by the same instance of your function can reuse these resources. This saves cost by reducing function run time.

To avoid potential data leaks across invocations, don’t use the execution environment to store user data, events, or other information with security implications. If your function relies on a mutable state that can’t be stored in memory within the handler, consider creating a separate function or separate versions of a function for each user.

**Use a keep-alive directive to maintain persistent connections.** Lambda purges idle connections over time. Attempting to reuse an idle connection when invoking a function will result in a connection error. To maintain your persistent connection, use the keep-alive directive associated with your runtime. For an example, see [Reusing Connections with Keep-Alive in Node.js](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/node-reusing-connections.html).

**Use [environment variables](configuration-envvars.md) to pass operational parameters to your function.** For example, if you are writing to an Amazon S3 bucket, instead of hard-coding the bucket name you are writing to, configure the bucket name as an environment variable.

**Avoid using recursive invocations** in your Lambda function, where the function invokes itself or initiates a process that may invoke the function again. This could lead to unintended volume of function invocations and escalated costs. If you see an unintended volume of invocations, set the function reserved concurrency to `0` immediately to throttle all invocations to the function, while you update the code.

**Do not use non-documented, non-public APIs** in your Lambda function code. For AWS Lambda managed runtimes, Lambda periodically applies security and functional updates to Lambda's internal APIs. These internal API updates may be backwards-incompatible, leading to unintended consequences such as invocation failures if your function has a dependency on these non-public APIs. See [the API reference](https://docs.aws.amazon.com/lambda/latest/api/welcome.html) for a list of publicly available APIs.

**Write idempotent code.** Writing idempotent code for your functions ensures that duplicate events are handled the same way. Your code should properly validate events and gracefully handle duplicate events. For more information, see [How do I make my Lambda function idempotent?](https://aws.amazon.com/premiumsupport/knowledge-center/lambda-function-idempotent/).