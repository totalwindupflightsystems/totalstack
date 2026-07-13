---
id: "@specs/aws/lambda/docs/runtimes-walkthrough"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Custom runtime tutorial"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Custom runtime tutorial

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/runtimes-walkthrough
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Tutorial: Building a custom runtime
<a name="runtimes-walkthrough"></a>

In this tutorial, you create a Lambda function with a custom runtime. You start by including the runtime in the function's deployment package. Then you migrate it to a layer that you manage independently from the function. Finally, you share the runtime layer with the world by updating its resource-based permissions policy.

## Prerequisites
<a name="runtimes-walkthrough-prereqs"></a>

This tutorial assumes that you have some knowledge of basic Lambda operations and the Lambda console. If you haven't already, follow the instructions in [Create a Lambda function with the console](getting-started.md#getting-started-create-function) to create your first Lambda function.

To complete the following steps, you need the [AWS CLI version 2](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html). Commands and the expected output are listed in separate blocks:

```
aws --version
```

You should see the following output:

```
aws-cli/2.13.27 Python/3.11.6 Linux/4.14.328-248.540.amzn2.x86_64 exe/x86_64.amzn.2
```

For long commands, an escape character (`\`) is used to split a command over multiple lines.

On Linux and macOS, use your preferred shell and package manager.

**Note**  
In Windows, some Bash CLI commands that you commonly use with Lambda (such as `zip`) are not supported by the operating system's built-in terminals. To get a Windows-integrated version of Ubuntu and Bash, [install the Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10). Example CLI commands in this guide use Linux formatting. Commands which include inline JSON documents must be reformatted if you are using the Windows CLI. 

You need an IAM role to create a Lambda function. The role needs permission to send logs to CloudWatch Logs and access the AWS services that your function uses. If you don't have a role for function development, create one now.

**To create an execution role**

1. Open the [roles page](https://console.aws.amazon.com/iam/home#/roles) in the IAM console.

1. Choose **Create role**.

1. Create a role with the following properties.
   + **Trusted entity** – **Lambda**.
   + **Permissions** – **AWSLambdaBasicExecutionRole**.
   + **Role name** – **lambda-role**.

   The **AWSLambdaBasicExecutionRole** policy has the permissions that the function needs to write logs to CloudWatch Logs.

## Create a function
<a name="runtimes-walkthrough-function"></a>

Create a Lambda function with a custom runtime. This example includes two files: a runtime `bootstrap` file and a function handler. Both are implemented in Bash.

1. Create a directory for the project, and then switch to that directory.

   ```
   mkdir runtime-tutorial
   cd runtime-tutorial
   ```

1. Create a new file called `bootstrap`. This is the custom runtime.  
**Example bootstrap**  

   ```
   #!/bin/sh
   
   set -euo pipefail
   
   # Initialization - load function handler
   source $LAMBDA_TASK_ROOT/"$(echo $_HANDLER | cut -d. -f1).sh"
   
   # Processing
   while true
   do
     HEADERS="$(mktemp)"
     # Get an event. The HTTP request will block until one is received
     EVENT_DATA=$(curl -sS -LD "$HEADERS" "http://${AWS_LAMBDA_RUNTIME_API}/2018-06-01/runtime/invocation/next")
   
     # Extract request ID by scraping response headers received above
     REQUEST_ID=$(grep -Fi Lambda-Runtime-Aws-Request-Id "$HEADERS" | tr -d '[:space:]' | cut -d: -f2)
   
     # Run the handler function from the script
     RESPONSE=$($(echo "$_HANDLER" | cut -d. -f2) "$EVENT_DATA")
   
     # Send the response
     curl "http://${AWS_LAMBDA_RUNTIME_API}/2018-06-01/runtime/invocation/$REQUEST_ID/response"  -d "$RESPONSE"
   done
   ```

   The runtime loads a function script from the deployment package. It uses two variables to locate the script. `LAMBDA_TASK_ROOT` tells it where the package was extracted, and `_HANDLER` includes the name of the script.

   After the runtime loads the function script, it uses the runtime API to retrieve an invocation event from Lambda, passes the event to the handler, and posts the response back to Lambda. To get the request ID, the runtime saves the headers from the API response to a temporary file, and reads the `Lambda-Runtime-Aws-Request-Id` header from the file.
**Note**  
Runtimes have additional responsibilities, including error handling, and providing context information to the handler. For details, see [Requirements](runtimes-custom.md#runtimes-custom-build).

1. Create a script for the function. The following example script defines a handler function that takes event data, logs it to `stderr`, and returns it.  
**Example function.sh**  

   ```
   function handler () {
     EVENT_DATA=$1
     echo "$EVENT_DATA" 1>&2;
     RESPONSE="Echoing request: '$EVENT_DATA'"
   
     echo $RESPONSE
   }
   ```

   The `runtime-tutorial` directory should now look like this:

   ```
   runtime-tutorial
   ├ bootstrap
   └ function.sh
   ```

1. Make the files executable and add them to a .zip file archive. This is the deployment package.

   ```
   chmod 755 function.sh bootstrap
   zip function.zip function.sh bootstrap
   ```

1. Create a function named `bash-runtime`. For `--role`, enter the ARN of your Lambda [execution role](lambda-intro-execution-role.md).

   ```
   aws lambda create-function --function-name bash-runtime \
   --zip-file fileb://function.zip --handler function.handler --runtime provided.al2023 \
   --role {{arn:aws:iam::123456789012:role/lambda-role}}
   ```

1. Invoke the function.

   ```
   aws lambda invoke --function-name bash-runtime --payload '{"text":"Hello"}' response.txt --cli-binary-format raw-in-base64-out
   ```

   The **cli-binary-format** option is required if you're using AWS CLI version 2. To make this the default setting, run `aws configure set cli-binary-format raw-in-base64-out`. For more information, see [AWS CLI supported global command line options](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-options.html#cli-configure-options-list) in the *AWS Command Line Interface User Guide for Version 2*.

   You should see a response like this:

   ```
   {
       "StatusCode": 200,
       "ExecutedVersion": "$LATEST"
   }
   ```

1. Verify the response.

   ```
   cat response.txt
   ```

   You should see a response like this:

   ```
   Echoing request: '{"text":"Hello"}'
   ```

## Create a layer
<a name="runtimes-walkthrough-layer"></a>

To separate the runtime code from the function code, create a layer that only contains the runtime. Layers let you develop your function's dependencies independently, and can reduce storage usage when you use the same layer with multiple functions. For more information, see [Managing Lambda dependencies with layers](chapter-layers.md).

1. Create a .zip file that contains the `bootstrap` file.

   ```
   zip runtime.zip bootstrap
   ```

1. Create a layer with the [publish-layer-version](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/publish-layer-version.html?highlight=nodejs16%20x) command.

   ```
   aws lambda publish-layer-version --layer-name bash-runtime --zip-file fileb://runtime.zip
   ```

   This creates the first version of the layer.

## Update the function
<a name="runtimes-walkthrough-update"></a>

To use the runtime layer in the function, configure the function to use the layer, and remove the runtime code from the function.

1. Update the function configuration to pull in the layer.

   ```
   aws lambda update-function-configuration --function-name bash-runtime \
   --layers arn:aws:lambda:us-east-1:{{123456789012}}:layer:bash-runtime:1
   ```

   This adds the runtime to the function in the `/opt` directory. To ensure that Lambda uses the runtime in the layer, you must remove the `boostrap` from the function's deployment package, as shown in the next two steps.

1. Create a .zip file that contains the function code.

   ```
   zip function-only.zip function.sh
   ```

1. Update the function code to only include the handler script.

   ```
   aws lambda update-function-code --function-name bash-runtime --zip-file fileb://function-only.zip
   ```

1. Invoke the function to confirm that it works with the runtime layer.

   ```
   aws lambda invoke --function-name bash-runtime --payload '{"text":"Hello"}' response.txt --cli-binary-format raw-in-base64-out
   ```

   The **cli-binary-format** option is required if you're using AWS CLI version 2. To make this the default setting, run `aws configure set cli-binary-format raw-in-base64-out`. For more information, see [AWS CLI supported global command line options](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-options.html#cli-configure-options-list) in the *AWS Command Line Interface User Guide for Version 2*.

   You should see a response like this:

   ```
   {
       "StatusCode": 200,
       "ExecutedVersion": "$LATEST"
   }
   ```

1. Verify the response.

   ```
   cat response.txt
   ```

   You should see a response like this:

   ```
   Echoing request: '{"text":"Hello"}'
   ```

## Update the runtime
<a name="runtimes-walkthrough-runtime"></a>

1. To log information about the execution environment, update the runtime script to output environment variables.  
**Example bootstrap**  

   ```
   #!/bin/sh
   
   set -euo pipefail
   
   # Configure runtime to output environment variables
   echo "##  Environment variables:"
   env
   
   # Load function handler
   source $LAMBDA_TASK_ROOT/"$(echo $_HANDLER | cut -d. -f1).sh"
   
   # Processing
   while true
   do
     HEADERS="$(mktemp)"
     # Get an event. The HTTP request will block until one is received
     EVENT_DATA=$(curl -sS -LD "$HEADERS" "http://${AWS_LAMBDA_RUNTIME_API}/2018-06-01/runtime/invocation/next")
   
     # Extract request ID by scraping response headers received above
     REQUEST_ID=$(grep -Fi Lambda-Runtime-Aws-Request-Id "$HEADERS" | tr -d '[:space:]' | cut -d: -f2)
   
     # Run the handler function from the script
     RESPONSE=$($(echo "$_HANDLER" | cut -d. -f2) "$EVENT_DATA")
   
     # Send the response
     curl "http://${AWS_LAMBDA_RUNTIME_API}/2018-06-01/runtime/invocation/$REQUEST_ID/response"  -d "$RESPONSE"
   done
   ```

1. Create a .zip file that contains the new version of the `bootstrap` file.

   ```
   zip runtime.zip bootstrap
   ```

1. Create a new version of the `bash-runtime` layer.

   ```
   aws lambda publish-layer-version --layer-name bash-runtime --zip-file fileb://runtime.zip
   ```

1. Configure the function to use the new version of the layer.

   ```
   aws lambda update-function-configuration --function-name bash-runtime \
   --layers arn:aws:lambda:us-east-1:{{123456789012}}:layer:bash-runtime:2
   ```

## Share the layer
<a name="runtimes-walkthrough-share"></a>

To share a layer with another AWS account, add a cross-account permissions statement to the layer's [resource-based policy](access-control-resource-based.md). Run the [add-layer-version-permission](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/add-layer-version-permission.html) command and specify the account ID as the `principal`. In each statement, you can grant permission to a single account, all accounts, or an organization in [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html).

The following example grants account 111122223333 access to version 2 of the `bash-runtime` layer.

```
aws lambda add-layer-version-permission \
  --layer-name bash-runtime \
  --version-number 2 \  
  --statement-id xaccount \
  --action lambda:GetLayerVersion \
  --principal 111122223333 \
  --output text
```

You should see output similar to the following:

```
{"Sid":"xaccount","Effect":"Allow","Principal":{"AWS":"arn:aws:iam::111122223333:root"},"Action":"lambda:GetLayerVersion","Resource":"arn:aws:lambda:us-east-1:123456789012:layer:bash-runtime:2"}
```

Permissions apply only to a single layer version. Repeat the process each time that you create a new layer version.

## Clean up
<a name="runtimes-walkthrough-cleanup"></a>

Delete each version of the layer.

```
aws lambda delete-layer-version --layer-name bash-runtime --version-number 1
aws lambda delete-layer-version --layer-name bash-runtime --version-number 2
```

Because the function holds a reference to version 2 of the layer, it still exists in Lambda. The function continues to work, but functions can no longer be configured to use the deleted version. If you modify the list of layers on the function, you must specify a new version or omit the deleted layer.

Delete the function with the [delete-function](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/delete-function.html) command.

```
aws lambda delete-function --function-name bash-runtime
```