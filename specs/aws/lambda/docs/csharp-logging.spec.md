---
id: "@specs/aws/lambda/docs/csharp-logging"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Logging"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Logging

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/csharp-logging
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Log and monitor C\# Lambda functions
<a name="csharp-logging"></a>

AWS Lambda automatically monitors Lambda functions and sends log entries to Amazon CloudWatch. Your Lambda function comes with a CloudWatch Logs log group and a log stream for each instance of your function. The Lambda runtime environment sends details about each invocation and other output from your function's code to the log stream. For more information about CloudWatch Logs, see [Sending Lambda function logs to CloudWatch Logs](monitoring-cloudwatchlogs.md).

**Topics**
+ [Creating a function that returns logs](#csharp-logging-output)
+ [Using Lambda advanced logging controls with .NET](#csharp-logging-advanced)
+ [Additional logging tools and libraries](#csharp-tools-libraries)
+ [Using Powertools for AWS Lambda (.NET) and AWS SAM for structured logging](#dotnet-logging-sam)
+ [Viewing logs in the Lambda console](#csharp-logging-console)
+ [Viewing logs in the CloudWatch console](#csharp-logging-cwconsole)
+ [Viewing logs using the AWS Command Line Interface (AWS CLI)](#csharp-logging-cli)
+ [Deleting logs](#csharp-logging-delete)

## Creating a function that returns logs
<a name="csharp-logging-output"></a>

To output logs from your function code, you can use the [ILambdaLogger](https://github.com/aws/aws-lambda-dotnet/blob/master/Libraries/src/Amazon.Lambda.Core/ILambdaLogger.cs) on the context object, the methods on the [Console class](https://docs.microsoft.com/en-us/dotnet/api/system.console), or any logging library that writes to `stdout` or `stderr`.

The .NET runtime logs the `START`, `END`, and `REPORT` lines for each invocation. The report line provides the following details.

**REPORT line data fields**
+ **RequestId** – The unique request ID for the invocation.
+ **Duration** – The amount of time that your function's handler method spent processing the event.
+ **Billed Duration** – The amount of time billed for the invocation.
+ **Memory Size** – The amount of memory allocated to the function.
+ **Max Memory Used** – The amount of memory used by the function. When invocations share an execution environment, Lambda reports the maximum memory used across all invocations. This behavior might result in a higher than expected reported value.
+ **Init Duration** – For the first request served, the amount of time it took the runtime to load the function and run code outside of the handler method.
+ **XRAY TraceId** – For traced requests, the [AWS X-Ray trace ID](services-xray.md).
+ **SegmentId** – For traced requests, the X-Ray segment ID.
+ **Sampled** – For traced requests, the sampling result.

## Using Lambda advanced logging controls with .NET
<a name="csharp-logging-advanced"></a>

To give you more control over how your functions’ logs are captured, processed, and consumed, you can configure the following logging options for supported .NET runtimes:
+ **Log format** - select between plain text and structured JSON format for your function’s logs
+ **Log level** - for logs in JSON format, choose the detail level of the logs Lambda sends to CloudWatch, such as ERROR, DEBUG, or INFO
+ **Log group** - choose the CloudWatch log group your function sends logs to

For more information about these logging options, and instructions on how to configure your function to use them, see [Configuring advanced logging controls for Lambda functions](monitoring-logs.md#monitoring-cloudwatchlogs-advanced).

To use the log format and log level options with your .NET Lambda functions, see the guidance in the following sections.

### Using structured JSON log format with .NET
<a name="csharp-logging-advanced-JSON"></a>

If you select JSON for your function's log format, Lambda will send logs output using [ILambdaLogger](https://github.com/aws/aws-lambda-dotnet/blob/master/Libraries/src/Amazon.Lambda.Core/ILambdaLogger.cs) as structured JSON. Each JSON log object contains at least five key value pairs with the following keys:
+ `"timestamp"` - the time the log message was generated
+ `"level"` - the log level assigned to the message
+ `"requestId"` - the unique request ID for the function invocation
+ `"traceId"` - the `_X_AMZN_TRACE_ID` environment variable
+ `"message"` - the contents of the log message

The `ILambdaLogger` instance can add additional key value pairs, for example when logging exceptions. You can also supply your own additional parameters as described in the section [Customer-provided log parameters](#csharp-logging-advanced-JSON-user-supplied).

**Note**  
If your code already uses another logging library to produce JSON-formatted logs, ensure that your function's log format is set to plain text. Setting the log format to JSON will result in your log outputs being double-encoded.

The following example logging command shows how to write a log message with the level `INFO`.

**Example .NET logging code**  

```
context.Logger.LogInformation("Fetching cart from database");
```

You can also use a generic log method that takes the log level as an argument as shown in the following example.

```
context.Logger.Log(LogLevel.Information, "Fetching cart from database");
```

The log output by these example code snippets would be captured in CloudWatch Logs as follows:

**Example JSON log record**  

```
{
    "timestamp": "2025-09-07T01:30:06.977Z",
    "level": "Information",
    "requestId": "8f711428-7e55-46f9-ae88-2a65d4f85fc5",
    "traceId": "1-6408af34-50f56f5b5677a7d763973804",
    "message": "Fetching cart from database"
}
```

**Note**  
If you configure your function's log format to to use plain text rather than JSON, then the log level captured in the message follows the Microsoft convention of using a four-character label. For example, a log level of `Debug` is represented in the message as `dbug`.  
When you configure your function to use JSON formatted logs, the log level captured in the log uses the full label as shown in the example JSON log record.

If you don't assign a level to your log output, Lambda will automatically assign it the level INFO.

#### Logging exceptions in JSON
<a name="csharp-logging-advanced-JSON-exceptions"></a>

When using structured JSON logging with `ILambdaLogger`, you can log exceptions in your code as shown in the following example.

**Example usage of exception logging**  

```
try
{
    connection.ExecuteQuery(query);
}
catch(Exception e)
{
    context.Logger.LogWarning(e, "Error executing query");
}
```

The log format output by this code is shown in the following example JSON. Note that the `message` property in the JSON is populated using the message argument provided in the `LogWarning` call, while the `errorMessage` property comes from the `Message` property of the exception itself.

**Example JSON log record**  

```
{
    "timestamp": "2025-09-07T01:30:06.977Z",
    "level": "Warning",
    "requestId": "8f711428-7e55-46f9-ae88-2a65d4f85fc5",
    "traceId": "1-6408af34-50f56f5b5677a7d763973804",
    "message": "Error executing query",
    "errorType": "System.Data.SqlClient.SqlException",
    "errorMessage": "Connection closed",
    "stackTrace": ["<call exception.StackTrace>"]
}
```

If your function's logging format is set to JSON, Lambda also outputs JSON-formatted log messages when your code throws an uncaught exception. The following example code snippet and log message show how uncaught exceptions are logged.

**Example exception code**  

```
throw new ApplicationException("Invalid data");
```

**Example JSON log record**  

```
{
    "timestamp": "2025-09-07T01:30:06.977Z",
    "level": "Error",
    "requestId": "8f711428-7e55-46f9-ae88-2a65d4f85fc5",
    "traceId": "1-6408af34-50f56f5b5677a7d763973804",
    "message": "Invalid data",
    "errorType": "System.ApplicationException",
    "errorMessage": "Invalid data",
    "stackTrace": ["<call exception.StackTrace>"]
}
```

#### Customer-provided log parameters
<a name="csharp-logging-advanced-JSON-user-supplied"></a>

With JSON-formatted log messages, you can supply additional log parameters and include these in the log `message`. The following code snippet example shows a command to add two user-supplied parameters labeled `retryAttempt` and `uri`. In the example, the value of these parameters come from the `retryAttempt` and `uriDestination` arguments passed into the logging command.

**Example JSON logging command with additional parameters**  

```
context.Logger.LogInformation("Starting retry {retryAttempt} to make GET request to {uri}", retryAttempt, uriDestination);
```

The log message output by this command is shown in the following example JSON.

**Example JSON log record**  

```
{
    "timestamp": "2025-09-07T01:30:06.977Z",
    "level": "Information",
    "requestId": "8f711428-7e55-46f9-ae88-2a65d4f85fc5",
    "traceId": "1-6408af34-50f56f5b5677a7d763973804",
    "message": "Starting retry 1 to make GET request to http://example.com/",
    "retryAttempt": 1,
    "uri": "http://example.com/"
}
```

**Tip**  
You can also use positional properties instead of names when specifying additional parameters. For example, the logging command in the previous example could also be written as follows:  

```
context.Logger.LogInformation("Starting retry {0} to make GET request to {1}", retryAttempt, uriDestination);
```

Note that when you supply additional logging parameters, Lambda captures them as top-level properties in the JSON log record. This approach differs from some popular .NET logging libraries such as `Serilog`, which captures additional parameters in a separate child object.

If the argument you supply for an additional parameter is a complex object, by default Lambda uses the `ToString()` method to supply the value. To indicate that an argument should be JSON serialized, use the `@` prefix as shown in the following code snippet. In this example, `User` is an object with `FirstName` and `LastName` properties.

**Example JSON logging command with JSON serialized object**  

```
context.Logger.LogInformation("User {@user} logged in", User);
```

The log message output by this command is shown in the following example JSON.

**Example JSON log record**  

```
{
    "timestamp": "2025-09-07T01:30:06.977Z",
    "level": "Information",
    "requestId": "8f711428-7e55-46f9-ae88-2a65d4f85fc5",
    "traceId": "1-6408af34-50f56f5b5677a7d763973804",
    "message": "User {@user} logged in",
    "user": 
    {
        "FirstName": "John",
        "LastName": "Doe"
    }
}
```

If the argument for an additional parameter is an array or implements `IList` or `IDictionary`, then Lambda adds the argument to the JSON log message as an array as shown in the following example JSON log record. In this example, `{users}` takes an `IList` argument containing instances of the `User` property with the same format as the previous example. Lambda converts this `IList` into an array, with each value being created using the `ToString` method.

**Example JSON log record with an `IList` argument**  

```
{
    "timestamp": "2025-09-07T01:30:06.977Z",
    "level": "Information",
    "requestId": "8f711428-7e55-46f9-ae88-2a65d4f85fc5",
    "traceId": "1-6408af34-50f56f5b5677a7d763973804",
    "message": "{users} have joined the group",
    "users": 
    [
        "Rosalez, Alejandro",
        "Stiles, John"       
    ] 
}
```

You can also JSON serialize the list by using the `@` prefix in your logging command. In the following example JSON log record, the `users` property is JSON serialized.

**Example JSON log record with a JSON serialized `IList` argument**  

```
{
    "timestamp": "2025-09-07T01:30:06.977Z",
    "level": "Information",
    "requestId": "8f711428-7e55-46f9-ae88-2a65d4f85fc5",
    "traceId": "1-6408af34-50f56f5b5677a7d763973804",
    "message": "{@users} have joined the group",
    "users": 
    [
        {
            "FirstName": "Alejandro",
            "LastName": "Rosalez"
        },
        {
            "FirstName": "John",
            "LastName": "Stiles"
        }        
    ] 
}
```

### Using log-level filtering with .NET
<a name="csharp-logging-advanced-levels"></a>

By configuring log-level filtering, you can choose to send only logs of a certain detail level or lower to CloudWatch Logs. To learn how to configure log-level filtering for your function, see [Log-level filtering](monitoring-cloudwatchlogs-log-level.md).

For AWS Lambda to filter your log messages by log level, you can either use JSON formatted logs or use the .NET `Console` methods to output log messages. To create JSON formatted logs, [configure your function's log type to JSON](monitoring-cloudwatchlogs-logformat.md#monitoring-cloudwatchlogs-set-format) and use the `ILambdaLogger` instance.

With JSON-formatted logs, Lambda filters your log outputs using the “level” key value pair in the JSON object described in [Using structured JSON log format with .NET](#csharp-logging-advanced-JSON).

If you use the .NET `Console` methods to write messages to CloudWatch Logs, Lambda applies log levels to your messages as follows:
+ **Console.WriteLine method** - Lambda applies a log-level of `INFO`
+ **Console.Error method** - Lambda applies a log-level of `ERROR`

When you configure your function to use log-level filtering, you must select from the following options for the level of logs you want Lambda to send to CloudWatch Logs. Note the mapping of the log levels used by Lambda with the standard Microsoft levels used by the .NET `ILambdaLogger`.


| Lambda log level | Equivalent Microsoft level | Standard usage | 
| --- | --- | --- | 
| TRACE (most detail) | Trace | The most fine-grained information used to trace the path of your code's execution | 
| DEBUG | Debug | Detailed information for system debugging | 
| INFO | Information | Messages that record the normal operation of your function | 
| WARN | Warning | Messages about potential errors that may lead to unexpected behavior if unaddressed | 
| ERROR | Error | Messages about problems that prevent the code from performing as expected | 
| FATAL (least detail) | Critical | Messages about serious errors that cause the application to stop functioning | 

Lambda sends logs of the selected detail level and lower to CloudWatch. For example, if you configure a log level of WARN, Lambda will send logs corresponding to the WARN, ERROR, and FATAL levels.

## Additional logging tools and libraries
<a name="csharp-tools-libraries"></a>

[Powertools for AWS Lambda (.NET)](https://docs.aws.amazon.com/powertools/dotnet/) is a developer toolkit to implement Serverless best practices and increase developer velocity. The [Logging utility](https://docs.aws.amazon.com/powertools/dotnet/core/logging/) provides a Lambda optimized logger which includes additional information about function context across all your functions with output structured as JSON. Use this utility to do the following:
+ Capture key fields from the Lambda context, cold start and structures logging output as JSON
+ Log Lambda invocation events when instructed (disabled by default)
+ Print all the logs only for a percentage of invocations via log sampling (disabled by default)
+ Append additional keys to structured log at any point in time
+ Use a custom log formatter (Bring Your Own Formatter) to output logs in a structure compatible with your organization’s Logging RFC

## Using Powertools for AWS Lambda (.NET) and AWS SAM for structured logging
<a name="dotnet-logging-sam"></a>

Follow the steps below to download, build, and deploy a sample Hello World C\# application with integrated [Powertools for AWS Lambda (.NET)](https://docs.powertools.aws.dev/lambda-dotnet) modules using the AWS SAM. This application implements a basic API backend and uses Powertools for emitting logs, metrics, and traces. It consists of an Amazon API Gateway endpoint and a Lambda function. When you send a GET request to the API Gateway endpoint, the Lambda function invokes, sends logs and metrics using Embedded Metric Format to CloudWatch, and sends traces to AWS X-Ray. The function returns a `hello world` message.

**Prerequisites**

To complete the steps in this section, you must have the following:
+ .NET 8
+ [AWS CLI version 2](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
+ [AWS SAM CLI version 1.75 or later](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html). If you have an older version of the AWS SAM CLI, see [Upgrading the AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/manage-sam-cli-versions.html#manage-sam-cli-versions-upgrade).

**Deploy a sample AWS SAM application**

1. Initialize the application using the Hello World TypeScript template.

   ```
   sam init --app-template hello-world-powertools-dotnet --name sam-app --package-type Zip --runtime dotnet6 --no-tracing
   ```

1. Build the app.

   ```
   cd sam-app && sam build
   ```

1. Deploy the app.

   ```
   sam deploy --guided
   ```

1. Follow the on-screen prompts. To accept the default options provided in the interactive experience, press `Enter`.
**Note**  
For **HelloWorldFunction may not have authorization defined, Is this okay?**, make sure to enter `y`.

1. Get the URL of the deployed application:

   ```
   aws cloudformation describe-stacks --stack-name sam-app --query 'Stacks[0].Outputs[?OutputKey==`HelloWorldApi`].OutputValue' --output text
   ```

1. Invoke the API endpoint:

   ```
   curl -X GET {{<URL_FROM_PREVIOUS_STEP>}}
   ```

   If successful, you'll see this response:

   ```
   {"message":"hello world"}
   ```

1. To get the logs for the function, run [sam logs](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-logs.html). For more information, see [Working with logs](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-logging.html) in the *AWS Serverless Application Model Developer Guide*.

   ```
   sam logs --stack-name sam-app
   ```

   The log output looks like this:

   ```
   2025/02/20/[$LATEST]4eaf8445ba7a4a93b999cb17fbfbecd8 2025-09-20T14:15:27.988000 INIT_START Runtime Version: dotnet:6.v13        Runtime Version ARN: arn:aws:lambda:ap-southeast-2::runtime:699f346a05dae24c58c45790bc4089f252bf17dae3997e79b17d939a288aa1ec
   2025/02/20/[$LATEST]4eaf8445ba7a4a93b999cb17fbfbecd8 2025-09-20T14:15:28.229000 START RequestId: bed25b38-d012-42e7-ba28-f272535fb80e Version: $LATEST
   2025/02/20/[$LATEST]4eaf8445ba7a4a93b999cb17fbfbecd8 2025-09-20T14:15:29.259000 2025-09-20T14:15:29.201Z        bed25b38-d012-42e7-ba28-f272535fb80e    info   {"_aws":{"Timestamp":1676902528962,"CloudWatchMetrics":[{"Namespace":"sam-app-logging","Metrics":[{"Name":"ColdStart","Unit":"Count"}],"Dimensions":[["FunctionName"],["Service"]]}]},"FunctionName":"sam-app-HelloWorldFunction-haKIoVeose2p","Service":"PowertoolsHelloWorld","ColdStart":1}
   2025/02/20/[$LATEST]4eaf8445ba7a4a93b999cb17fbfbecd8 2025-09-20T14:15:30.479000 2025-09-20T14:15:30.479Z        bed25b38-d012-42e7-ba28-f272535fb80e    info   {"ColdStart":true,"XrayTraceId":"1-63f3807f-5dbcb9910c96f50742707542","CorrelationId":"d3d4de7f-4ccc-411a-a549-4d67b2fdc015","FunctionName":"sam-app-HelloWorldFunction-haKIoVeose2p","FunctionVersion":"$LATEST","FunctionMemorySize":256,"FunctionArn":"arn:aws:lambda:ap-southeast-2:123456789012:function:sam-app-HelloWorldFunction-haKIoVeose2p","FunctionRequestId":"bed25b38-d012-42e7-ba28-f272535fb80e","Timestamp":"2025-09-20T14:15:30.4602970Z","Level":"Information","Service":"PowertoolsHelloWorld","Name":"AWS.Lambda.Powertools.Logging.Logger","Message":"Hello world API - HTTP 200"}
   2025/02/20/[$LATEST]4eaf8445ba7a4a93b999cb17fbfbecd8 2025-09-20T14:15:30.599000 2025-09-20T14:15:30.599Z        bed25b38-d012-42e7-ba28-f272535fb80e    info   {"_aws":{"Timestamp":1676902528922,"CloudWatchMetrics":[{"Namespace":"sam-app-logging","Metrics":[{"Name":"ApiRequestCount","Unit":"Count"}],"Dimensions":[["Service"]]}]},"Service":"PowertoolsHelloWorld","ApiRequestCount":1}
   2025/02/20/[$LATEST]4eaf8445ba7a4a93b999cb17fbfbecd8 2025-09-20T14:15:30.680000 END RequestId: bed25b38-d012-42e7-ba28-f272535fb80e
   2025/02/20/[$LATEST]4eaf8445ba7a4a93b999cb17fbfbecd8 2025-09-20T14:15:30.680000 REPORT RequestId: bed25b38-d012-42e7-ba28-f272535fb80e  Duration: 2450.99 ms   Billed Duration: 2692 ms Memory Size: 256 MB     Max Memory Used: 74 MB  Init Duration: 240.05 ms
   XRAY TraceId: 1-63f3807f-5dbcb9910c96f50742707542       SegmentId: 16b362cd5f52cba0
   ```

1. This is a public API endpoint that is accessible over the internet. We recommend that you delete the endpoint after testing.

   ```
   sam delete
   ```

### Managing log retention
<a name="csharp-log-retention"></a>

Log groups aren't deleted automatically when you delete a function. To avoid storing logs indefinitely, delete the log group, or configure a retention period after which CloudWatch automatically deletes the logs. To set up log retention, add the following to your AWS SAM template:

```
Resources:
  HelloWorldFunction:
    Type: AWS::Serverless::Function
    Properties:
      # Omitting other properties

  LogGroup:
    Type: AWS::Logs::LogGroup
    Properties:
      LogGroupName: !Sub "/aws/lambda/${HelloWorldFunction}"
      RetentionInDays: 7
```

## Viewing logs in the Lambda console
<a name="csharp-logging-console"></a>

You can use the Lambda console to view log output after you invoke a Lambda function.

If your code can be tested from the embedded **Code** editor, you will find logs in the **execution results**. When you use the console test feature to invoke a function, you'll find **Log output** in the **Details** section.

## Viewing logs in the CloudWatch console
<a name="csharp-logging-cwconsole"></a>

You can use the Amazon CloudWatch console to view logs for all Lambda function invocations.

**To view logs on the CloudWatch console**

1. Open the [Log groups page](https://console.aws.amazon.com/cloudwatch/home?#logs:) on the CloudWatch console.

1. Choose the log group for your function (**/aws/lambda/{{your-function-name}}**).

1. Choose a log stream.

Each log stream corresponds to an [instance of your function](lambda-runtime-environment.md). A log stream appears when you update your Lambda function, and when additional instances are created to handle concurrent invocations. To find logs for a specific invocation, we recommend instrumenting your function with AWS X-Ray. X-Ray records details about the request and the log stream in the trace.

## Viewing logs using the AWS Command Line Interface (AWS CLI)
<a name="csharp-logging-cli"></a>

The AWS CLI is an open-source tool that enables you to interact with AWS services using commands in your command line shell. To complete the steps in this section, you must have the [AWS CLI version 2](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

You can use the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) to retrieve logs for an invocation using the `--log-type` command option. The response contains a `LogResult` field that contains up to 4 KB of base64-encoded logs from the invocation.

**Example retrieve a log ID**  
The following example shows how to retrieve a *log ID* from the `LogResult` field for a function named `my-function`.  

```
aws lambda invoke --function-name my-function out --log-type Tail
```
You should see the following output:  

```
{
    "StatusCode": 200,
    "LogResult": "U1RBUlQgUmVxdWVzdElkOiA4N2QwNDRiOC1mMTU0LTExZTgtOGNkYS0yOTc0YzVlNGZiMjEgVmVyc2lvb...",
    "ExecutedVersion": "$LATEST"
}
```

**Example decode the logs**  
In the same command prompt, use the `base64` utility to decode the logs. The following example shows how to retrieve base64-encoded logs for `my-function`.  

```
aws lambda invoke --function-name my-function out --log-type Tail \
--query 'LogResult' --output text --cli-binary-format raw-in-base64-out | base64 --decode
```
The **cli-binary-format** option is required if you're using AWS CLI version 2. To make this the default setting, run `aws configure set cli-binary-format raw-in-base64-out`. For more information, see [AWS CLI supported global command line options](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-options.html#cli-configure-options-list) in the *AWS Command Line Interface User Guide for Version 2*.  
You should see the following output:  

```
START RequestId: 57f231fb-1730-4395-85cb-4f71bd2b87b8 Version: $LATEST
"AWS_SESSION_TOKEN": "AgoJb3JpZ2luX2VjELj...", "_X_AMZN_TRACE_ID": "Root=1-5d02e5ca-f5792818b6fe8368e5b51d50;Parent=191db58857df8395;Sampled=0"",ask/lib:/opt/lib",
END RequestId: 57f231fb-1730-4395-85cb-4f71bd2b87b8
REPORT RequestId: 57f231fb-1730-4395-85cb-4f71bd2b87b8  Duration: 79.67 ms      Billed Duration: 80 ms         Memory Size: 128 MB     Max Memory Used: 73 MB
```
The `base64` utility is available on Linux, macOS, and [Ubuntu on Windows](https://docs.microsoft.com/en-us/windows/wsl/install-win10). macOS users may need to use `base64 -D`.

**Example get-logs.sh script**  
In the same command prompt, use the following script to download the last five log events. The script uses `sed` to remove quotes from the output file, and sleeps for 15 seconds to allow time for the logs to become available. The output includes the response from Lambda and the output from the `get-log-events` command.   
Copy the contents of the following code sample and save in your Lambda project directory as `get-logs.sh`.  
The **cli-binary-format** option is required if you're using AWS CLI version 2. To make this the default setting, run `aws configure set cli-binary-format raw-in-base64-out`. For more information, see [AWS CLI supported global command line options](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-options.html#cli-configure-options-list) in the *AWS Command Line Interface User Guide for Version 2*.  

```
#!/bin/bash
aws lambda invoke --function-name my-function --cli-binary-format raw-in-base64-out --payload '{"key": "value"}' out
sed -i'' -e 's/"//g' out
sleep 15
aws logs get-log-events --log-group-name /aws/lambda/{{my-function}} --log-stream-name {{stream1}} --limit 5
```

**Example macOS and Linux (only)**  
In the same command prompt, macOS and Linux users may need to run the following command to ensure the script is executable.  

```
chmod -R 755 get-logs.sh
```

**Example retrieve the last five log events**  
In the same command prompt, run the following script to get the last five log events.  

```
./get-logs.sh
```
You should see the following output:  

```
{
    "StatusCode": 200,
    "ExecutedVersion": "$LATEST"
}
{
    "events": [
        {
            "timestamp": 1559763003171,
            "message": "START RequestId: 4ce9340a-b765-490f-ad8a-02ab3415e2bf Version: $LATEST\n",
            "ingestionTime": 1559763003309
        },
        {
            "timestamp": 1559763003173,
            "message": "2019-06-05T19:30:03.173Z\t4ce9340a-b765-490f-ad8a-02ab3415e2bf\tINFO\tENVIRONMENT VARIABLES\r{\r  \"AWS_LAMBDA_FUNCTION_VERSION\": \"$LATEST\",\r ...",
            "ingestionTime": 1559763018353
        },
        {
            "timestamp": 1559763003173,
            "message": "2019-06-05T19:30:03.173Z\t4ce9340a-b765-490f-ad8a-02ab3415e2bf\tINFO\tEVENT\r{\r  \"key\": \"value\"\r}\n",
            "ingestionTime": 1559763018353
        },
        {
            "timestamp": 1559763003218,
            "message": "END RequestId: 4ce9340a-b765-490f-ad8a-02ab3415e2bf\n",
            "ingestionTime": 1559763018353
        },
        {
            "timestamp": 1559763003218,
            "message": "REPORT RequestId: 4ce9340a-b765-490f-ad8a-02ab3415e2bf\tDuration: 26.73 ms\tBilled Duration: 27 ms \tMemory Size: 128 MB\tMax Memory Used: 75 MB\t\n",
            "ingestionTime": 1559763018353
        }
    ],
    "nextForwardToken": "f/34783877304859518393868359594929986069206639495374241795",
    "nextBackwardToken": "b/34783877303811383369537420289090800615709599058929582080"
}
```

## Deleting logs
<a name="csharp-logging-delete"></a>

Log groups aren't deleted automatically when you delete a function. To avoid storing logs indefinitely, delete the log group, or [configure a retention period](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html#SettingLogRetention) after which logs are deleted automatically.