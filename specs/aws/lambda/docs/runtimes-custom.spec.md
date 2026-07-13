---
id: "@specs/aws/lambda/docs/runtimes-custom"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Building a custom runtime"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Building a custom runtime

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/runtimes-custom
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Building a custom runtime for AWS Lambda
<a name="runtimes-custom"></a>

You can implement an AWS Lambda runtime in any programming language. A runtime is a program that runs a Lambda function's handler method when the function is invoked. You can include the runtime in your function's deployment package or distribute it in a [layer](chapter-layers.md). When you create the Lambda function, choose an [OS-only runtime](runtimes-provided.md) (the `provided` runtime family).

**Note**  
Creating a custom runtime is an advanced use case. If you're looking for information about compiling to a native binary or using a third-party off-the-shelf runtime, see [When to use Lambda's OS-only runtimes](runtimes-provided.md).

For a walkthrough of the custom runtime deployment process, see [Tutorial: Building a custom runtime](runtimes-walkthrough.md).

**Topics**
+ [Requirements](#runtimes-custom-build)
+ [Implementing response streaming in a custom runtime](#runtimes-custom-response-streaming)
+ [Building custom runtimes for Lambda Managed Instances](#runtimes-custom-managed-instances)

## Requirements
<a name="runtimes-custom-build"></a>

Custom runtimes must complete certain initialization and processing tasks. A runtime runs the function's setup code, reads the handler name from an environment variable, and reads invocation events from the Lambda runtime API. The runtime passes the event data to the function handler, and posts the response from the handler back to Lambda.

### Initialization tasks
<a name="runtimes-custom-initialization"></a>

The initialization tasks run once [per instance of the function](lambda-runtime-environment.md) to prepare the environment to handle invocations.
+ **Retrieve settings** – Read environment variables to get details about the function and environment.
  + `_HANDLER` – The location to the handler, from the function's configuration. The standard format is `{{file}}.{{method}}`, where `file` is the name of the file without an extension, and `method` is the name of a method or function that's defined in the file.
  + `LAMBDA_TASK_ROOT` – The directory that contains the function code.
  + `AWS_LAMBDA_RUNTIME_API` – The host and port of the runtime API.

  For a full list of available variables, see [Defined runtime environment variables](configuration-envvars.md#configuration-envvars-runtime).
+ **Initialize the function** – Load the handler file and run any global or static code that it contains. Functions should create static resources like SDK clients and database connections once, and reuse them for multiple invocations.
+ **Handle errors** – If an error occurs, call the [initialization error](runtimes-api.md#runtimes-api-initerror) API and exit immediately.

Initialization counts towards billed execution time and timeout. When an execution triggers the initialization of a new instance of your function, you can see the initialization time in the logs and [AWS X-Ray trace](services-xray.md).

**Example log**  

```
REPORT RequestId: f8ac1208... Init Duration: 48.26 ms   Duration: 237.17 ms   Billed Duration: 300 ms   Memory Size: 128 MB   Max Memory Used: 26 MB
```

### Processing tasks
<a name="runtimes-custom-processing"></a>

While it runs, a runtime uses the [Lambda runtime interface](runtimes-api.md) to manage incoming events and report errors. After completing initialization tasks, the runtime processes incoming events in a loop. In your runtime code, perform the following steps in order.
+ **Get an event** – Call the [next invocation](runtimes-api.md#runtimes-api-next) API to get the next event. The response body contains the event data. Response headers contain the request ID and other information.
+ **Propagate the tracing header** – Get the X-Ray tracing header from the `Lambda-Runtime-Trace-Id` header in the API response. Set the `_X_AMZN_TRACE_ID` environment variable locally with the same value. The X-Ray SDK uses this value to connect trace data between services.
+ **Create a context object** – Create an object with context information from environment variables and headers in the API response.
+ **Invoke the function handler** – Pass the event and context object to the handler.
+ **Handle the response** – Call the [invocation response](runtimes-api.md#runtimes-api-response) API to post the response from the handler.
+ **Handle errors** – If an error occurs, call the [invocation error](runtimes-api.md#runtimes-api-invokeerror) API.
+ **Cleanup** – Release unused resources, send data to other services, or perform additional tasks before getting the next event.

### Entrypoint
<a name="runtimes-custom-bootstrap"></a>

A custom runtime's entry point is an executable file named `bootstrap`. The bootstrap file can be the runtime, or it can invoke another file that creates the runtime. If the root of your deployment package doesn't contain a file named `bootstrap`, Lambda looks for the file in the function's layers. If the `bootstrap` file doesn't exist or isn't executable, your function returns a `Runtime.InvalidEntrypoint` error upon invocation.

Here's an example `bootstrap` file that uses a bundled version of Node.js to run a JavaScript runtime in a separate file named `runtime.js`.

**Example bootstrap**  

```
#!/bin/sh
    cd $LAMBDA_TASK_ROOT
    ./node-v11.1.0-linux-x64/bin/node runtime.js
```

## Implementing response streaming in a custom runtime
<a name="runtimes-custom-response-streaming"></a>

For [response streaming functions](configuration-response-streaming.md), the `response` and `error` endpoints have slightly modified behavior that lets the runtime stream partial responses to the client and return payloads in chunks. For more information about the specific behavior, see the following:
+ `/runtime/invocation/AwsRequestId/response` – Propagates the `Content-Type` header from the runtime to send to the client. Lambda returns the response payload in chunks via HTTP/1.1 chunked transfer encoding. To stream the response to Lambda, the runtime must:
  + Set the `Lambda-Runtime-Function-Response-Mode` HTTP header to `streaming`.
  + Set the `Transfer-Encoding` header to `chunked`.
  + Write the response conforming to the HTTP/1.1 chunked transfer encoding specification.
  + Close the underlying connection after it has successfully written the response.
+ `/runtime/invocation/AwsRequestId/error` – The runtime can use this endpoint to report function or runtime errors to Lambda, which also accepts the `Transfer-Encoding` header. This endpoint can only be called before the runtime begins sending an invocation response.
+ Report midstream errors using error trailers in `/runtime/invocation/AwsRequestId/response` – To report errors that occur after the runtime starts writing the invocation response, the runtime can optionally attach HTTP trailing headers named `Lambda-Runtime-Function-Error-Type` and `Lambda-Runtime-Function-Error-Body`. Lambda treats this as a successful response and forwards the error metadata that the runtime provides to the client. 
**Note**  
To attach trailing headers, the runtime must set the `Trailer` header value at the beginning of the HTTP request. This is a requirement of the HTTP/1.1 chunked transfer encoding specification.
  + `Lambda-Runtime-Function-Error-Type` – The error type that the runtime encountered. This header consists of a string value. Lambda accepts any string, but we recommend a format of {{<category.reason>}}. For example, `Runtime.APIKeyNotFound`.
  + `Lambda-Runtime-Function-Error-Body` – Base64-encoded information about the error.

## Building custom runtimes for Lambda Managed Instances
<a name="runtimes-custom-managed-instances"></a>

Lambda Managed Instances use the same runtime API as Lambda (default) functions. However, there are key differences in how custom runtimes must be implemented to support the concurrent execution model of Managed Instances.

### Concurrent request handling
<a name="runtimes-custom-managed-instances-concurrency"></a>

The primary difference when building custom runtimes for Managed Instances is support for concurrent invocations. Unlike Lambda (default) functions where the runtime processes one invocation at a time, Managed Instances can process multiple invocations simultaneously within a single execution environment.

Your custom runtime must:
+ **Support concurrent `/next` requests** – The runtime can make multiple simultaneous calls to the [next invocation](runtimes-api.md#runtimes-api-next) API, up to the limit specified by the `AWS_LAMBDA_MAX_CONCURRENCY` environment variable.
+ **Handle concurrent `/response` requests** – Multiple invocations can call the [invocation response](runtimes-api.md#runtimes-api-response) API simultaneously.
+ **Implement thread-safe request handling** – Ensure that concurrent invocations don't interfere with each other by properly managing shared resources and state.
+ **Use unique request IDs** – Track each invocation separately using the `Lambda-Runtime-Aws-Request-Id` header to match responses with their corresponding requests.

### Implementation pattern
<a name="runtimes-custom-managed-instances-implementation"></a>

A typical implementation pattern for Managed Instances runtimes involves creating worker threads or processes to handle concurrent invocations:

1. **Read the concurrency limit** – At initialization, read the `AWS_LAMBDA_MAX_CONCURRENCY` environment variable to determine how many concurrent invocations to support.

1. **Create worker pool** – Initialize a pool of workers (threads, processes, or async tasks) equal to the concurrency limit.

1. **Worker processing loop** – Each worker independently:
   + Calls `/runtime/invocation/next` to get an invocation event
   + Invokes the function handler with the event data
   + Posts the response to `/runtime/invocation/AwsRequestId/response`
   + Repeats the loop

### Additional considerations
<a name="runtimes-custom-managed-instances-considerations"></a>
+ **Logging format** – Managed Instances only support JSON log format. Ensure your runtime respects the `AWS_LAMBDA_LOG_FORMAT` environment variable and only uses JSON format. For more information, see [Configuring JSON and plain text log formats](monitoring-cloudwatchlogs-logformat.md).
+ **Shared resources** – Be cautious when using shared resources like the `/tmp` directory with concurrent invocations. Implement proper locking mechanisms to prevent race conditions.

For more information about Lambda Managed Instances execution environments, see [Understanding the Lambda Managed Instances execution environment](lambda-managed-instances-execution-environment.md).