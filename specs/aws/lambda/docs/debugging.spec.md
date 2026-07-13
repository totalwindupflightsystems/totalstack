---
id: "@specs/aws/lambda/docs/debugging"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Debug with VS Code"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Debug with VS Code

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/debugging
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Remotely debug Lambda functions with Visual Studio Code
<a name="debugging"></a>

With the remote debugging feature in the [AWS Toolkit for Visual Studio Code](https://aws.amazon.com/visualstudiocode/), you can debug your Lambda functions running directly in the AWS cloud. This is useful when investigating issues that are difficult to replicate locally or diagnose only with logs.

With remote debugging, you can:
+ Set breakpoints in your Lambda function code.
+ Step through code execution in real-time.
+ Inspect variables and state during runtime.
+ Debug Lambda functions deployed to AWS, including those in VPCs or with specific IAM permissions.

## Supported runtimes
<a name="debugging-runtimes"></a>

Remote debugging is supported for the following runtimes:
+ Python (AL2023)
+ Java
+ JavaScript/Node.js (AL2023)

**Note**  
Remote debugging is supported for both x86\_64 and arm64 architectures.

## Security and remote debugging
<a name="debugging-security"></a>

Remote debugging operates within existing Lambda security boundaries. Users can attach layers to a function using the `UpdateFunctionConfiguration` permission, which already has the ability to access function environment variables and configuration. Remote debugging doesn't extend beyond these existing permissions. Instead, it adds extra security controls through secure tunneling and automatic session management. Additionally, remote debugging is entirely a customer-controlled feature that requires explicit permissions and actions:
+ **IoT Secure Tunnel Creation**: The AWS Toolkit must create an IoT secure tunnel, which only occurs with the user's explicit permission using `iot:OpenTunnel`.
+ **Debug Layer Attachment and Token Management**: The debugging process maintains security through these controls:
  + The debugging layer must be attached to the Lambda function and this process requires the following permissions: `lambda:UpdateFunctionConfiguration` and `lambda:GetLayerVersion`.
  + A security token (generated via `iot:OpenTunnel`) must be updated in the function environment variable before each debug session, which also requires `lambda:UpdateFunctionConfiguration`.
  + For security, this token is automatically rotated and the debug layer is automatically removed at the end of each debug session and cannot be reused.

**Note**  
Remote debugging is supported for both x86\_64 and arm64 architectures.

## Prerequisites
<a name="debugging-prerequisites"></a>

Before you begin remote debugging, ensure you have the following:

1. A Lambda function deployed to your AWS account.

1. AWS Toolkit for Visual Studio Code. See [Setting up the AWS Toolkit for Visual Studio Code](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/setup-toolkit.html) for installation instructions.

1. The version of the AWS Toolkit you have installed is **3.69.0** or later.

1. AWS credentials configured in AWS Toolkit for Visual Studio Code. For more information, see [Authentication and access control](foundation-iac-local-development.md#lambda-functions-vscode-authentication-and-access-control).

## Remotely debug Lambda functions
<a name="debugging-procedure"></a>

Follow these steps to start a remote debugging session:

1. Open the AWS Explorer in VS Code by selecting the AWS icon in the left sidebar.

1. Expand the Lambda section to see your functions.

1. Right-click on the function you want to debug.

1. From the context menu, select **Remotely invoke**.

1. In the invoke window that opens, check the box for **Enable debugging**.

1. Click **Invoke** to start the remote debugging session.

**Note**  
Lambda functions have a 250MB combined limit for function code and all attached layers. The remote debugging layer adds approximately 40MB to your function's size.

A remote debugging session ends when you:
+ Choose **Remove Debug Setup** from the Remote invoke configuration screen.
+ Select the disconnect icon in the VS Code debugging controls.
+ Select the handler file in the VS Code editor.

**Note**  
The debug layer is automatically removed after 60 seconds of inactivity following your last invoke.

## Disable remote debugging
<a name="debugging-disable"></a>

There are three ways to disable this feature:
+ **Deny Function Updates**: Set `lambda:UpdateFunctionConfiguration` to `deny`.
+ **Restrict IoT Permissions**: Deny IoT-related permissions
+ **Block Debug Layers**: Deny `lambda:GetLayerVersion` for the following ARNs:
  + `arn:aws:lambda:*:*:layer:LDKLayerX86:*`
  + `arn:aws:lambda:*:*:layer:LDKLayerArm64:*`
**Note**  
Disabling this feature prevents the debugging layer from being added during function configuration updates.

## Additional information
<a name="debugging-related-info"></a>

For more information on using Lambda in VS Code, refer to [Developing Lambda functions locally with VS Code](foundation-iac-local-development.md).

For detailed instructions on troubleshooting, advanced use cases, and region availability, see [Remote debugging Lambda functions](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/lambda-remote-debug.html) in the AWS Toolkit for Visual Studio Code User Guide.