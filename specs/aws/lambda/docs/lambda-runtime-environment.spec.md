---
id: "@specs/aws/lambda/docs/lambda-runtime-environment"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Execution environment"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Execution environment

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/lambda-runtime-environment
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Understanding the Lambda execution environment lifecycle
<a name="lambda-runtime-environment"></a>

Lambda execution environments support both standard functions (up to 15 minutes) and Durable Functions (up to one year). While both share the same basic lifecycle, Durable Functions add state management capabilities for long-running workflows.

 Lambda invokes your function in an execution environment, which provides a secure and isolated runtime environment. The execution environment manages the resources required to run your function. The execution environment also provides lifecycle support for the function's runtime and any [external extensions](lambda-extensions.md) associated with your function. 

**For Durable Functions, the execution environment includes additional components for:**
+ State persistence between steps
+ Checkpointing management
+ Wait state coordination
+ Progress tracking

**Lambda Managed Instances execution environment**  
If you are using [Lambda Managed Instances](lambda-managed-instances-execution-environment.md), the execution environment has important differences compared to Lambda (default) functions. Managed Instances support concurrent invocations, use a different lifecycle model, and run on customer-owned infrastructure. For detailed information about the Managed Instances execution environment, see [Understanding the Lambda Managed Instances execution environment](lambda-managed-instances-execution-environment.md).

The function's runtime communicates with Lambda using the [Runtime API](runtimes-api.md). Extensions communicate with Lambda using the [Extensions API](runtimes-extensions-api.md). Extensions can also receive log messages and other telemetry from the function by using the [Telemetry API](telemetry-api.md). 



![Architecture diagram of the execution environment.](http://docs.aws.amazon.com/lambda/latest/dg/images/telemetry-api-concept-diagram.png)


When you create your Lambda function, you specify configuration information, such as the amount of memory available and the maximum execution time allowed for your function. Lambda uses this information to set up the execution environment.

The function's runtime and each external extension are processes that run within the execution environment. Permissions, resources, credentials, and environment variables are shared between the function and the extensions.

**Topics**
+ [Lambda execution environment lifecycle](#runtimes-lifecycle)
+ [Cold starts and latency](#cold-start-latency)
+ [Reducing cold starts with Provisioned Concurrency](#cold-starts-pc)
+ [Optimizing static initialization](#static-initialization)

## Lambda execution environment lifecycle
<a name="runtimes-lifecycle"></a>

![Lambda lifecycle phases: Init, Invoke, Shutdown](http://docs.aws.amazon.com/lambda/latest/dg/images/Overview-Successful-Invokes.png)


Each phase starts with an event that Lambda sends to the runtime and to all registered extensions. The runtime and each extension indicate completion by sending a `Next` API request. Lambda freezes the execution environment when the runtime and each extension have completed and there are no pending events.

**The lifecycle phases for Durable Functions include:**
+ **Init:** Standard initialization plus durable state setup
+ **Invoke:** Can include multiple step executions with automatic checkpointing
+ **Wait:** Function can pause execution without consuming resources
+ **Resume:** Function restarts from last checkpoint
+ **Shutdown:** Cleanup of durable state and resources

**Topics**
+ [Init phase](#runtimes-lifecycle-ib)
+ [Failures during the Init phase](#runtimes-lifecycle-init-errors)
+ [Restore phase (Lambda SnapStart only)](#runtimes-lifecycle-restore)
+ [Invoke phase](#runtimes-lifecycle-invoke)
+ [Failures during the invoke phase](#runtimes-lifecycle-invoke-with-errors)
+ [Shutdown phase](#runtimes-lifecycle-shutdown)

### Init phase
<a name="runtimes-lifecycle-ib"></a>

In the `Init` phase, Lambda performs three tasks:
+ Start all extensions (`Extension init`)
+ Bootstrap the runtime (`Runtime init`)
+ Run the function's static code (`Function init`)
+ Run any before-checkpoint [runtime hooks](snapstart-runtime-hooks.md) (Lambda SnapStart only)

The `Init` phase ends when the runtime and all extensions signal that they are ready by sending a `Next` API request. The `Init` phase is limited to 10 seconds. If all three tasks do not complete within 10 seconds, Lambda retries the `Init` phase at the time of the first function invocation with the configured function timeout.

When [SnapStart](snapstart.md) is activated, the `Init` phase happens when you publish a function version. Lambda saves a snapshot of the memory and disk state of the initialized execution environment, persists the encrypted snapshot, and caches it for low-latency access. If you have a before-checkpoint [runtime hook](snapstart-runtime-hooks.md), then the code runs at the end of `Init` phase.

**Note**  
The 10-second timeout doesn't apply to functions that are using provisioned concurrency, SnapStart, or Lambda Managed Instances. For provisioned concurrency, SnapStart, and Managed Instances functions, your initialization code can run for up to 15 minutes. The time limit is 130 seconds or the configured function timeout (maximum 900 seconds), whichever is higher.

When you use [provisioned concurrency](https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html), Lambda initializes the execution environment when you configure the PC settings for a function. Lambda also ensures that initialized execution environments are always available in advance of invocations. You may see gaps between your function's invocation and initialization phases. Depending on your function's runtime and memory configuration, you may also see variable latency on the first invocation on an initialized execution environment.

For functions using on-demand concurrency, Lambda may occasionally initialize execution environments ahead of invocation requests. When this happens, you may also observe a time gap between your function's initialization and invocation phases. We recommend you to not take a dependency on this behavior.

### Failures during the Init phase
<a name="runtimes-lifecycle-init-errors"></a>

If a function crashes or times out during the `Init` phase, Lambda emits error information in the `INIT_REPORT` log.

**Example — INIT\_REPORT log for timeout**  

```
INIT_REPORT Init Duration: 1236.04 ms Phase: init Status: timeout
```

**Example — INIT\_REPORT log for extension failure**  

```
INIT_REPORT Init Duration: 1236.04 ms Phase: init Status: error Error Type: Extension.Crash
```

If the `Init` phase is successful, Lambda doesn't emit the `INIT_REPORT` log unless [SnapStart](snapstart.md) or [provisioned concurrency](provisioned-concurrency.md) is enabled. SnapStart and provisioned concurrency functions always emit `INIT_REPORT`. For more information, see [Monitoring for Lambda SnapStart](snapstart-monitoring.md).

### Restore phase (Lambda SnapStart only)
<a name="runtimes-lifecycle-restore"></a>

When you first invoke a [SnapStart](snapstart.md) function and as the function scales up, Lambda resumes new execution environments from the persisted snapshot instead of initializing the function from scratch. If you have an after-restore [runtime hook](snapstart-runtime-hooks.md), the code runs at the end of the `Restore` phase. You are charged for the duration of after-restore runtime hooks. The runtime must load and after-restore runtime hooks must complete within the timeout limit (10 seconds). Otherwise, you'll get a SnapStartTimeoutException. When the `Restore` phase completes, Lambda invokes the function handler (the [Invoke phase](#runtimes-lifecycle-invoke)).

#### Failures during the Restore phase
<a name="runtimes-lifecycle-restore-errors"></a>

If the `Restore` phase fails, Lambda emits error information in the `RESTORE_REPORT` log.

**Example — RESTORE\_REPORT log for timeout**  

```
RESTORE_REPORT Restore Duration: 1236.04 ms Status: timeout
```

**Example — RESTORE\_REPORT log for runtime hook failure**  

```
RESTORE_REPORT Restore Duration: 1236.04 ms Status: error Error Type: Runtime.ExitError
```

For more information about the `RESTORE_REPORT` log, see [Monitoring for Lambda SnapStart](snapstart-monitoring.md).

### Invoke phase
<a name="runtimes-lifecycle-invoke"></a>

When a Lambda function is invoked in response to a `Next` API request, Lambda sends an `Invoke` event to the runtime and to each extension.

The function's timeout setting limits the duration of the entire `Invoke` phase. For example, if you set the function timeout as 360 seconds, the function and all extensions need to complete within 360 seconds. Note that there is no independent post-invoke phase. The duration is the sum of all invocation time (runtime \+ extensions) and is not calculated until the function and all extensions have finished executing.

The invoke phase ends after the runtime and all extensions signal that they are done by sending a `Next` API request.

### Failures during the invoke phase
<a name="runtimes-lifecycle-invoke-with-errors"></a>

If the Lambda function crashes or times out during the `Invoke` phase, Lambda resets the execution environment. The following diagram illustrates Lambda execution environment behavior when there's an invoke failure:

![Execution environment example: Init, Invoke, Invoke with Error, Invoke, Shutdown](http://docs.aws.amazon.com/lambda/latest/dg/images/Overview-Invoke-with-Error.png)


In the previous diagram:
+ The first phase is the **INIT** phase, which runs without errors.
+ The second phase is the **INVOKE** phase, which runs without errors.
+ At some point, suppose your function runs into an invoke failure (common causes include function timeouts, runtime errors, memory exhaustion, VPC connectivity issues, permission errors, concurrency limits, and various configuration problems). For a complete list of possible invocation failures, see [Troubleshoot invocation issues in Lambda](troubleshooting-invocation.md). The third phase, labeled **INVOKE WITH ERROR **, illustrates this scenario. When this happens, the Lambda service performs a reset. The reset behaves like a `Shutdown` event. First, Lambda shuts down the runtime, then sends a `Shutdown` event to each registered external extension. The event includes the reason for the shutdown. If this environment is used for a new invocation, Lambda re-initializes the extension and runtime together with the next invocation.

  Note that the Lambda reset does not clear the `/tmp` directory content prior to the next init phase. This behavior is consistent with the regular shutdown phase.
**Note**  
AWS is currently implementing changes to the Lambda service. Due to these changes, you may see minor differences between the structure and content of system log messages and trace segments emitted by different Lambda functions in your AWS account.  
If your function's system log configuration is set to plain text, this change affects the log messages captured in CloudWatch Logs when your function experiences an invoke failure. The following examples show log outputs in both old and new formats.  
These changes will be implemented during the coming weeks, and all functions in all AWS Regions except the China and GovCloud regions will transition to use the new-format log messages and trace segments.

    
**Example CloudWatch Logs log output (runtime or extension crash) - old style**  

  ```
  START RequestId: c3252230-c73d-49f6-8844-968c01d1e2e1 Version: $LATEST
  RequestId: c3252230-c73d-49f6-8844-968c01d1e2e1 Error: Runtime exited without providing a reason
  Runtime.ExitError
  END RequestId: c3252230-c73d-49f6-8844-968c01d1e2e1
  REPORT RequestId: c3252230-c73d-49f6-8844-968c01d1e2e1 Duration: 933.59 ms Billed Duration: 934 ms Memory Size: 128 MB Max Memory Used: 9 MB
  ```  
**Example CloudWatch Logs log output (function timeout) - old style**  

  ```
  START RequestId: b70435cc-261c-4438-b9b6-efe4c8f04b21 Version: $LATEST
  2024-03-04T17:22:38.033Z b70435cc-261c-4438-b9b6-efe4c8f04b21 Task timed out after 3.00 seconds
  END RequestId: b70435cc-261c-4438-b9b6-efe4c8f04b21
  REPORT RequestId: b70435cc-261c-4438-b9b6-efe4c8f04b21 Duration: 3004.92 ms Billed Duration: 3117 ms Memory Size: 128 MB Max Memory Used: 33 MB Init Duration: 111.23 ms
  ```

  The new format for CloudWatch logs includes an additional `status`field in the `REPORT` line. In the case of a runtime or extension crash, the `REPORT` line also includes a field `ErrorType`.

    
**Example CloudWatch Logs log output (runtime or extension crash) - new style**  

  ```
  START RequestId: 5b866fb1-7154-4af6-8078-6ef6ca4c2ddd Version: $LATEST
  END RequestId: 5b866fb1-7154-4af6-8078-6ef6ca4c2ddd
  REPORT RequestId: 5b866fb1-7154-4af6-8078-6ef6ca4c2ddd Duration: 133.61 ms Billed Duration: 214 ms Memory Size: 128 MB Max Memory Used: 31 MB Init Duration: 80.00 ms Status: error Error Type: Runtime.ExitError
  ```  
**Example CloudWatch Logs log output (function timeout) - new style**  

  ```
  START RequestId: 527cb862-4f5e-49a9-9ae4-a7edc90f0fda Version: $LATEST
  END RequestId: 527cb862-4f5e-49a9-9ae4-a7edc90f0fda
  REPORT RequestId: 527cb862-4f5e-49a9-9ae4-a7edc90f0fda Duration: 3016.78 ms Billed Duration: 3101 ms Memory Size: 128 MB Max Memory Used: 31 MB Init Duration: 84.00 ms Status: timeout
  ```
+ The fourth phase represents the **INVOKE** phase immediately following an invoke failure. Here, Lambda initializes the environment again by re-running the **INIT** phase. This is called a *suppressed init*. When suppressed inits occur, Lambda doesn't explicitly report an additional **INIT** phase in CloudWatch Logs. Instead, you may notice that the duration in the REPORT line includes an additional **INIT** duration \+ the **INVOKE** duration. For example, suppose you see the following logs in CloudWatch:

  ```
  2022-12-20T01:00:00.000-08:00 START RequestId: XXX Version: $LATEST 
  2022-12-20T01:00:02.500-08:00 END RequestId: XXX 
  2022-12-20T01:00:02.500-08:00 REPORT RequestId: XXX Duration: 3022.91 ms 
  Billed Duration: 3000 ms Memory Size: 512 MB Max Memory Used: 157 MB
  ```

  In this example, the difference between the REPORT and START timestamps is 2.5 seconds. This doesn't match the reported duration of 3022.91 millseconds, because it doesn't take into account the extra **INIT** (suppressed init) that Lambda performed. In this example, you can infer that the actual **INVOKE** phase took 2.5 seconds.

  For more insight into this behavior, you can use the [Accessing real-time telemetry data for extensions using the Telemetry API](telemetry-api.md). The Telemetry API emits `INIT_START`, `INIT_RUNTIME_DONE`, and `INIT_REPORT` events with `phase=invoke` whenever suppressed inits occur in between invoke phases.
+ The fifth phase represents the **SHUTDOWN** phase, which runs without errors.

### Shutdown phase
<a name="runtimes-lifecycle-shutdown"></a>

When Lambda is about to shut down the runtime, it sends a `Shutdown` event to each registered external extension. Extensions can use this time for final cleanup tasks. The `Shutdown` event is a response to a `Next` API request.

**Duration limit**: The maximum duration of the `Shutdown` phase depends on the configuration of registered extensions:
+ 0 ms – A function with no registered extensions
+ 500 ms – A function with a registered internal extension
+ 2,000 ms – A function with one or more registered external extensions

If the runtime or an extension does not respond to the `Shutdown` event within the limit, Lambda ends the process using a `SIGKILL` signal.

After the function and all extensions have completed, Lambda maintains the execution environment for some time in anticipation of another function invocation. However, Lambda terminates execution environments every few hours to allow for runtime updates and maintenance—even for functions that are invoked continuously. You should not assume that the execution environment will persist indefinitely. For more information, see [Implement statelessness in functions](concepts-application-design.md#statelessness-functions).

When the function is invoked again, Lambda thaws the environment for reuse. Reusing the execution environment has the following implications: 
+ Objects declared outside of the function's handler method remain initialized, providing additional optimization when the function is invoked again. For example, if your Lambda function establishes a database connection, instead of reestablishing the connection, the original connection is used in subsequent invocations. We recommend adding logic in your code to check if a connection exists before creating a new one.
+ Each execution environment provides between 512 MB and 10,240 MB, in 1-MB increments, of disk space in the `/tmp` directory. The directory content remains when the execution environment is frozen, providing a transient cache that can be used for multiple invocations. You can add extra code to check if the cache has the data that you stored. For more information on deployment size limits, see [Lambda quotasLambda quotas](gettingstarted-limits.md).
+ Background processes or callbacks that were initiated by your Lambda function and did not complete when the function ended resume if Lambda reuses the execution environment. Make sure that any background processes or callbacks in your code are complete before the code exits.

## Cold starts and latency
<a name="cold-start-latency"></a>

When Lambda receives a request to run a function via the Lambda API, the service first prepares an execution environment. During this initialization phase, the service downloads your code, starts the environment, and runs any initialization code outside of the main handler. Finally, Lambda runs the handler code.

![perf optimize figure 1](http://docs.aws.amazon.com/lambda/latest/dg/images/perf-optimize-figure-1.png)


In this diagram, the first two steps of downloading the code and setting up the environment are frequently referred to as a “cold start”. You are [charged for this time](https://aws.amazon.com/blogs/compute/aws-lambda-standardizes-billing-for-init-phase/), and it adds latency to your overall invocation duration.

After the invocation completes, the execution environment is frozen. To improve resource management and performance, Lambda retains the execution environment for a period of time. During this time, if another request arrives for the same function, Lambda can reuse the environment. This second request typically finishes more quickly, since the execution environment is already fully set up. This is called a “warm start”.

Cold starts typically occur in under 1% of invocations. The duration of a cold start varies from under 100 ms to over 1 second. In general, cold starts are typically more common in development and test functions than production workloads. This is because development and test functions are usually invoked less frequently.

## Reducing cold starts with Provisioned Concurrency
<a name="cold-starts-pc"></a>

If you need predictable function start times for your workload, [provisioned concurrency](provisioned-concurrency.md) is the recommended solution to ensure the lowest possible latency. This feature pre-initializes execution environments, reducing cold starts.

For example, a function with a provisioned concurrency of 6 has 6 execution environments pre-warmed.

![perf optimize figure 4](http://docs.aws.amazon.com/lambda/latest/dg/images/perf-optimize-figure-4.png)


## Optimizing static initialization
<a name="static-initialization"></a>

Static initialization happens before the handler code starts running in a function. This is the initialization code that you provide, that is outside of the main handler. This code is often used to import libraries and dependencies, set up configurations, and initialize connections to other services.

The following Python example shows importing, and configuring modules, and creating the Amazon S3 client during the initialization phase, before the `lambda_handler` function runs during invoke.

```
import os
import json
import cv2
import logging
import boto3

s3 = boto3.client('s3')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):

  # Handler logic...
```

The largest contributor of latency before function execution comes from initialization code. This code runs when a new execution environment is created for the first time. The initialization code is not run again if an invocation uses a warm execution environment. Factors that affect initialization code latency include:
+ The size of the function package, in terms of imported libraries and dependencies, and Lambda layers.
+ The amount of code and initialization work.
+ The performance of libraries and other services in setting up connections and other resources.

There are a number of steps that developers can take to optimize static initialization latency. If a function has many objects and connections, you may be able to rearchitect a single function into multiple, specialized functions. These are individually smaller and each have less initialization code.

It’s important that functions only import the libraries and dependencies that they need. For example, if you only use Amazon DynamoDB in the AWS SDK, you can require an individual service instead of the entire SDK. Compare the following three examples:

```
// Instead of const AWS = require('aws-sdk'), use:
const DynamoDB = require('aws-sdk/clients/dynamodb')

// Instead of const AWSXRay = require('aws-xray-sdk'), use:
const AWSXRay = require('aws-xray-sdk-core')

// Instead of const AWS = AWSXRay.captureAWS(require('aws-sdk')), use:
const dynamodb = new DynamoDB.DocumentClient()
AWSXRay.captureAWSClient(dynamodb.service)
```

Static initialization is also often the best place to open database connections to allow a function to reuse connections over multiple invocations to the same execution environment. However, you may have large numbers of objects that are only used in certain execution paths in your function. In this case, you can lazily load variables in the global scope to reduce the static initialization duration.

Avoid global variables for context-specific information. If your function has a global variable that is used only for the lifetime of a single invocation and is reset for the next invocation, use a variable scope that is local to the handler. Not only does this prevent global variable leaks across invocations, it also improves the static initialization performance.