---
id: "@specs/aws/lambda/docs/csharp-package-sam"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AWS SAM"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# AWS SAM

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/csharp-package-sam
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Deploy C\# Lambda functions using AWS SAM
<a name="csharp-package-sam"></a>

The AWS Serverless Application Model (AWS SAM) is a toolkit that helps streamline the process of building and running serverless applications on AWS. You define the resources for your application in a YAML or JSON template and use the AWS SAM command line interface (AWS SAM CLI) to build, package, and deploy your applications. When you build a Lambda function from an AWS SAM template, AWS SAM automatically creates a .zip deployment package or container image with your function code and any dependencies you specify. AWS SAM then deploys your function using an [CloudFormation stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacks.html). To learn more about using AWS SAM to build and deploy Lambda functions, see [Getting started with AWS SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started.html) in the *AWS Serverless Application Model Developer Guide*.

The following steps show you how to download, build, and deploy a sample .NET Hello World application using AWS SAM. This sample application uses a Lambda function and an Amazon API Gateway endpoint to implement a basic API backend. When you send an HTTP GET request to your API Gateway endpoint, API Gateway invokes your Lambda function. The function returns a "hello world" message, along with the IP address of the Lambda function instance that processes your request.

When you build and deploy your application using AWS SAM, behind the scenes the AWS SAM CLI uses the `dotnet lambda package` command to package the individual Lambda function code bundles.

## Prerequisites
<a name="csharp-package-sam-prerequisites"></a>

**.NET 8 SDK**  
Install the [.NET 8](https://dotnet.microsoft.com/en-us/download/dotnet/8.0) SDK and Runtime.

**AWS SAM CLI version 1.39 or later**  
To learn how to install the latest version of the AWS SAM CLI, see [Installing the AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html).

## Deploy a sample AWS SAM application
<a name="csharp-package-sam-deploy"></a>

1. Initialize the application using the Hello world .NET template using the following command.

   ```
   sam init --app-template hello-world --name sam-app \
   --package-type Zip --runtime dotnet8
   ```

   This command creates the following files and directories in your project directory.

   ```
   └── sam-app
       ├── README.md
       ├── events
       │   └── event.json
       ├── omnisharp.json
       ├── samconfig.toml
       ├── src
       │   └── HelloWorld
       │       ├── Function.cs
       │       ├── HelloWorld.csproj
       │       └── aws-lambda-tools-defaults.json
       ├── template.yaml
       └── test
           └── HelloWorld.Test
               ├── FunctionTest.cs
               └── HelloWorld.Tests.csproj
   ```

1. Navigate into the directory containing the `template.yaml file`. This file is a tempate that defines the AWS resources for your application, including your Lambda function and an API Gateway API.

   ```
   cd sam-app
   ```

1. To build the source of your application, run the following command.

   ```
   sam build
   ```

1. To deploy your application to AWS, run the following command.

   ```
   sam deploy --guided
   ```

   This command packages and deploys your application with the following series of prompts. To accept the default options, press Enter.
**Note**  
For **HelloWorldFunction may not have authorization defined, is this okay?**, be sure to enter `y`.
   + **Stack Name**: The name of the stack to deploy to CloudFormation. This name must be unique to your AWS account and AWS Region.
   + **AWS Region**: The AWS Region you want to deploy your app to.
   + **Confirm changes before deploy**: Select yes to manually review any change sets before AWS SAM deploys application changes. If you select no, the AWS SAM CLI automatically deploys application changes.
   + **Allow SAM CLI IAM role creation**: Many AWS SAM templates, including the Hello world one in this example, create AWS Identity and Access Management (IAM) roles to give your Lambda functions permission to access other AWS services. Select Yes to provide permission to deploy a CloudFormation stack that creates or modifies IAM roles.
   + **Disable rollback**: By default, if AWS SAM encounters an error during creation or deployment of your stack, it rolls the stack back to the previous version. Select No to accept this default.
   + **HelloWorldFunction may not have authorization defined, is this okay**: Enter `y`.
   + **Save arguments to samconfig.toml**: Select yes to save your configuration choices. In the future, you can re-run `sam deploy` without parameters to deploy changes to your application.

1. When the deployment of your application is complete, the CLI returns the Amazon Resource Name (ARN) of the Hello World Lambda function and the IAM role created for it. It also displays the endpoint of your API Gateway API. To test your application, open the endpoint in a browser. You should see a response similar to the following.

   ```
   {"message":"hello world","location":"34.244.135.203"}
   ```

1. To delete your resources, run the following command. Note that the API endpoint you created is a public endpoint accessible over the internet. We recommend that you delete this endpoint after testing.

   ```
   sam delete
   ```

## Next steps
<a name="csharp-package-sam-next"></a>

To learn more about using AWS SAM to build and deploy Lambda functions using .NET, see the following resources:
+ The [https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html)
+ [Building Serverless .NET Applications with AWS Lambda and the SAM CLI](https://aws.amazon.com/blogs/dotnet/building-serverless-net-applications-with-aws-lambda-and-the-sam-cli/)