---
id: "@specs/aws/lambda/docs/csharp-image"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Deploy container images"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Deploy container images

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/csharp-image
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Deploy .NET Lambda functions with container images
<a name="csharp-image"></a>

There are three ways to build a container image for a .NET Lambda function:
+ [Using an AWS base image for .NET](#csharp-image-instructions)

  The [AWS base images](images-create.md#runtimes-images-lp) are preloaded with a language runtime, a runtime interface client to manage the interaction between Lambda and your function code, and a runtime interface emulator for local testing.
+ [Using an AWS OS-only base image](images-create.md#runtimes-images-provided)

  [AWS OS-only base images](https://gallery.ecr.aws/lambda/provided) contain an Amazon Linux distribution and the [runtime interface emulator](https://github.com/aws/aws-lambda-runtime-interface-emulator/). These images are commonly used to create container images for compiled languages, such as [Go](go-image.md#go-image-provided) and [Rust](lambda-rust.md), and for a language or language version that Lambda doesn't provide a base image for, such as Node.js 19. You can also use OS-only base images to implement a [custom runtime](runtimes-custom.md). To make the image compatible with Lambda, you must include the [the runtime interface client for .NET](#csharp-image-clients) in the image.
+ [Using a non-AWS base image](#csharp-image-clients)

  You can use an alternative base image from another container registry, such as Alpine Linux or Debian. You can also use a custom image created by your organization. To make the image compatible with Lambda, you must include the [the runtime interface client for .NET](#csharp-image-clients) in the image.

**Tip**  
To reduce the time it takes for Lambda container functions to become active, see [Use multi-stage builds](https://docs.docker.com/build/building/multi-stage/) in the Docker documentation. To build efficient container images, follow the [Best practices for writing Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/).

This page explains how to build, test, and deploy container images for Lambda.

**Topics**
+ [AWS base images for .NET](#csharp-image-base)
+ [Using an AWS base image for .NET](#csharp-image-instructions)
+ [Using an alternative base image with the runtime interface client](#csharp-image-clients)

## AWS base images for .NET
<a name="csharp-image-base"></a>

AWS provides the following base images for .NET:


| Tags | Runtime | Operating system | Dockerfile | Deprecation | 
| --- | --- | --- | --- | --- | 
| 10 | .NET 10 | Amazon Linux 2023 | [Dockerfile for .NET 10 on GitHub](https://github.com/aws/aws-lambda-base-images/blob/dotnet10/Dockerfile.dotnet10) |  Nov 14, 2028  | 
| 9 | .NET 9 | Amazon Linux 2023 | [Dockerfile for .NET 9 on GitHub](https://github.com/aws/aws-lambda-base-images/blob/dotnet9/Dockerfile.dotnet9) |  Nov 10, 2026  | 
| 8 | .NET 8 | Amazon Linux 2023 | [Dockerfile for .NET 8 on GitHub](https://github.com/aws/aws-lambda-base-images/blob/dotnet8/Dockerfile.dotnet8) |  Nov 10, 2026  | 

Amazon ECR repository: [gallery.ecr.aws/lambda/dotnet](https://gallery.ecr.aws/lambda/dotnet)

## Using an AWS base image for .NET
<a name="csharp-image-instructions"></a>

### Prerequisites
<a name="dotnet-csharp-image-prerequisites"></a>

To complete the steps in this section, you must have the following:
+ [.NET SDK](https://dotnet.microsoft.com/download) – The following steps use the .NET 8 base image. Make sure that your .NET version matches the version of the [base image](https://gallery.ecr.aws/lambda/dotnet) that you specify in your Dockerfile.
+ [Docker](https://docs.docker.com/get-docker) (minimum version 25.0.0)
+ The Docker [buildx plugin](https://github.com/docker/buildx/blob/master/README.md).

### Creating and deploying an image using a base image
<a name="dotnet-image-create"></a>

In the following steps, you use [Amazon.Lambda.Templates](https://github.com/aws/aws-lambda-dotnet#dotnet-cli-templates) and [Amazon.Lambda.Tools](https://github.com/aws/aws-extensions-for-dotnet-cli#aws-lambda-amazonlambdatools) to create a .NET project. Then, you build a Docker image, upload the image to Amazon ECR, and deploy it to a Lambda function.

1. Install the [Amazon.Lambda.Templates](https://github.com/aws/aws-lambda-dotnet#dotnet-cli-templates) NuGet package.

   ```
   dotnet new install Amazon.Lambda.Templates
   ```

1. Create a .NET project using the `lambda.image.EmptyFunction` template.

   ```
   dotnet new lambda.image.EmptyFunction --name {{MyFunction}} --region {{us-east-1}}
   ```

   The project files are stored in the `{{MyFunction}}/src/{{MyFunction}}` directory:
   + **aws-lambda-tools-defaults.json**: Specifies the command line options for deploying your Lambda function.
   + **Function.cs**: Your Lambda handler function code. This is a C\# template that includes the default `Amazon.Lambda.Core` library and a default `LambdaSerializer` attribute. For more information about serialization requirements and options, see [Serialization in C\# Lambda functions](csharp-handler.md#csharp-handler-serializer). You can use the provided code for testing, or replace it with your own.
   + **MyFunction.csproj**: A .NET [project file](https://learn.microsoft.com/en-us/dotnet/core/project-sdk/overview#project-files), which lists the files and assemblies that comprise your application.
   + **Dockerfile**: You can use the provided Dockerfile for testing, or replace it with your own. If you use your own, make sure to:
     + Set the `FROM` property to the [URI of the base image](https://gallery.ecr.aws/lambda/dotnet). The base image and the `TargetFramework` in the `MyFunction.csproj` file must both use the same .NET version. For example, to use .NET 9:
       + Dockerfile: `FROM {{public.ecr.aws/lambda/dotnet:9}}`
       + MyFunction.csproj: `<TargetFramework>{{net9.0}}</TargetFramework>`
     + Set the `CMD` argument to the Lambda function handler. This should match the `image-command` in `aws-lambda-tools-defaults.json`.

1. Install the Amazon.Lambda.Tools [.NET Global Tool](https://aws.amazon.com/blogs/developer/net-core-global-tools-for-aws/).

   ```
   dotnet tool install -g Amazon.Lambda.Tools
   ```

   If Amazon.Lambda.Tools is already installed, make sure that you have the latest version.

   ```
   dotnet tool update -g Amazon.Lambda.Tools
   ```

1. Change the directory to `{{MyFunction}}/src/{{MyFunction}}`, if you're not there already.

   ```
   cd src/{{MyFunction}}
   ```

1. Use Amazon.Lambda.Tools to build the Docker image, push it to a new Amazon ECR repository, and deploy the Lambda function.

   For `--function-role`, specify the role name—not the Amazon Resource Name (ARN)—of the [execution role](lambda-intro-execution-role.md) for the function. For example, `lambda-role`.

   ```
   dotnet lambda deploy-function {{MyFunction}} --function-role {{lambda-role}}
   ```

   For more information about the Amazon.Lambda.Tools .NET Global Tool, see the [AWS Extensions for .NET CLI](https://github.com/aws/aws-extensions-for-dotnet-cli) repository on GitHub.

1. Invoke the function.

   ```
   dotnet lambda invoke-function {{MyFunction}} --payload "Testing the function"
   ```

   If everything is successful, you see a response similar to the following:

   ```
   Payload:
   {"Lower":"testing the function","Upper":"TESTING THE FUNCTION"}
   
   Log Tail:
   INIT_REPORT Init Duration: 9999.81 ms   Phase: init     Status: timeout
   START RequestId: 12378346-f302-419b-b1f2-deaa1e8423ed Version: $LATEST
   END RequestId: 12378346-f302-419b-b1f2-deaa1e8423ed
   REPORT RequestId: 12378346-f302-419b-b1f2-deaa1e8423ed  Duration: 3173.06 ms    Billed Duration: 3174 ms        Memory Size: 512 MB     Max Memory Used: 24 MB
   ```

1. Delete the Lambda function.

   ```
   dotnet lambda delete-function {{MyFunction}}
   ```

## Using an alternative base image with the runtime interface client
<a name="csharp-image-clients"></a>

If you use an [OS-only base image](images-create.md#runtimes-images-provided) or an alternative base image, you must include the runtime interface client in your image. The runtime interface client extends the [Runtime API](runtimes-api.md), which manages the interaction between Lambda and your function code.

The following example demonstrates how to build a container image for .NET using a non-AWS base image, and how to add the [Amazon.Lambda.RuntimeSupport package](https://github.com/aws/aws-lambda-dotnet/blob/master/Libraries/src/Amazon.Lambda.RuntimeSupport/README.md#using-amazonlambdaruntimesupport-as-a-class-library), which is the Lambda runtime interface client for .NET. The example Dockerfile uses the Microsoft .NET 8 base image.

### Prerequisites
<a name="dotnet-csharp-alt-prerequisites"></a>

To complete the steps in this section, you must have the following:
+ [.NET SDK](https://dotnet.microsoft.com/download) – The following steps use a .NET 9 base image. Make sure that your .NET version matches the version of the base image that you specify in your Dockerfile.
+ [Docker](https://docs.docker.com/get-docker) (minimum version 25.0.0)
+ The Docker [buildx plugin](https://github.com/docker/buildx/blob/master/README.md).

### Creating and deploying an image using an alternative base image
<a name="dotnet-alt-create"></a>

1. Install the [Amazon.Lambda.Templates](https://github.com/aws/aws-lambda-dotnet#dotnet-cli-templates) NuGet package.

   ```
   dotnet new install Amazon.Lambda.Templates
   ```

1. Create a .NET project using the `lambda.CustomRuntimeFunction` template. This template includes the [Amazon.Lambda.RuntimeSupport](https://github.com/aws/aws-lambda-dotnet/blob/master/Libraries/src/Amazon.Lambda.RuntimeSupport/README.md#using-amazonlambdaruntimesupport-as-a-class-library) package.

   ```
   dotnet new lambda.CustomRuntimeFunction --name {{MyFunction}} --region {{us-east-1}}
   ```

1. Navigate to the `{{MyFunction}}/src/{{MyFunction}}` directory. This is where the project files are stored. Examine the following files:
   + **aws-lambda-tools-defaults.json** – This file is where you specify the command line options when deploying your Lambda function.
   + **Function.cs** – The code contains a class with a `Main` method that initializes the `Amazon.Lambda.RuntimeSupport` library as the bootstrap. The `Main` method is the entry point for the function's process. The `Main` method wraps the function handler in a wrapper that the bootstrap can work with. For more information, see [Using Amazon.Lambda.RuntimeSupport as a class library](https://github.com/aws/aws-lambda-dotnet/blob/master/Libraries/src/Amazon.Lambda.RuntimeSupport/README.md#using-amazonlambdaruntimesupport-as-a-class-library) in the GitHub repository.
   + **MyFunction.csproj** – A .NET [project file](https://learn.microsoft.com/en-us/dotnet/core/project-sdk/overview#project-files), which lists the files and assemblies that comprise your application.
   + **Readme.md** – This file contains more information about the sample Lambda function.

1. Open the `aws-lambda-tools-defaults.json` file and Add the following lines:

   ```
     {{"package-type": "image",}}
     {{"docker-host-build-output-dir": "./bin/Release/lambda-publish"}}
   ```
   + **package-type**: Defines the deployment package as a container image.
   + **docker-host-build-output-dir**: Sets the output directory for the build process.  
**Example aws-lambda-tools-defaults.json**  

   ```
   {
     "Information": [
       "This file provides default values for the deployment wizard inside Visual Studio and the AWS Lambda commands added to the .NET Core CLI.",
       "To learn more about the Lambda commands with the .NET Core CLI execute the following command at the command line in the project root directory.",
       "dotnet lambda help",
       "All the command line options for the Lambda command can be specified in this file."
     ],
     "profile": "",
     "region": "us-east-1",
     "configuration": "Release",
     "function-runtime": "provided.al2023",
     "function-memory-size": 256,
     "function-timeout": 30,
     "function-handler": "bootstrap",
     "msbuild-parameters": "--self-contained true",
     {{"package-type": "image",}}
     {{"docker-host-build-output-dir": "./bin/Release/lambda-publish"}}
   }
   ```

1. Create a Dockerfile in the `{{MyFunction}}/src/{{MyFunction}}` directory. The following example Dockerfile uses a Microsoft .NET base image instead of an [AWS base image](#csharp-image-base).
   + Set the `FROM` property to the base image identifier. The base image and the `TargetFramework` in the `MyFunction.csproj` file must both use the same .NET version.
   + Use the `COPY` command to copy the function into the `/var/task` directory.
   + Set the `ENTRYPOINT` to the module that you want the Docker container to run when it starts. In this case, the module is the bootstrap, which initializes the `Amazon.Lambda.RuntimeSupport` library.

   Note that the example Dockerfile does not include a [USER instruction](https://docs.docker.com/reference/dockerfile/#user). When you deploy a container image to Lambda, Lambda automatically defines a default Linux user with least-privileged permissions. This is different from standard Docker behavior which defaults to the `root` user when no `USER` instruction is provided.  
**Example Dockerfile**  

   ```
   # You can also pull these images from DockerHub amazon/aws-lambda-dotnet:8
   FROM {{mcr.microsoft.com/dotnet/runtime:9.0}}
   
   # Set the image's internal work directory
   WORKDIR /var/task
     
   # Copy function code to Lambda-defined environment variable
   COPY "bin/Release/{{net9.0}}/linux-x64"  .
     
   # Set the entrypoint to the bootstrap
   ENTRYPOINT ["{{/usr/bin/dotnet", "exec", "/var/task/bootstrap.dll}}"]
   ```

1. Install the Amazon.Lambda.Tools [.NET Global Tools extension](https://aws.amazon.com/blogs/developer/net-core-global-tools-for-aws/).

   ```
   dotnet tool install -g Amazon.Lambda.Tools
   ```

   If Amazon.Lambda.Tools is already installed, make sure that you have the latest version.

   ```
   dotnet tool update -g Amazon.Lambda.Tools
   ```

1. Use Amazon.Lambda.Tools to build the Docker image, push it to a new Amazon ECR repository, and deploy the Lambda function.

   For `--function-role`, specify the role name—not the Amazon Resource Name (ARN)—of the [execution role](lambda-intro-execution-role.md) for the function. For example, `lambda-role`.

   ```
   dotnet lambda deploy-function {{MyFunction}} --function-role {{lambda-role}}
   ```

   For more information about the Amazon.Lambda.Tools .NET CLI extension, see the [AWS Extensions for .NET CLI](https://github.com/aws/aws-extensions-for-dotnet-cli) repository on GitHub.

1. Invoke the function.

   ```
   dotnet lambda invoke-function {{MyFunction}} --payload "Testing the function"
   ```

   If everything is successful, you see the following:

   ```
   Payload:
   "TESTING THE FUNCTION"
   
   Log Tail:
   START RequestId: {{id}} Version: $LATEST
   END RequestId: {{id}}
   REPORT RequestId: {{id}}  Duration: 0.99 ms       Billed Duration: 1 ms         Memory Size: 256 MB     Max Memory Used: 12 MB
   ```

1. Delete the Lambda function.

   ```
   dotnet lambda delete-function {{MyFunction}}
   ```