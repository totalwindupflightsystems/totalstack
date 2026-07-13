---
id: "@specs/aws/lambda/docs/csharp-package-cli"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS NET Lambda Global CLI"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# NET Lambda Global CLI

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/csharp-package-cli
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Using the .NET Lambda Global CLI
<a name="csharp-package-cli"></a>

The .NET CLI and the .NET Lambda Global Tools extension (`Amazon.Lambda.Tools`) offer a cross-platform way to create .NET-based Lambda applications, package them, and deploy them to Lambda. In this section, you learn how to create new Lambda .NET projects using the .NET CLI and Amazon Lambda templates, and to package and deploy them using `Amazon.Lambda.Tools`

**Topics**
+ [Prerequisites](#csharp-package-cli-prerequisites)
+ [Creating .NET projects using the .NET CLI](#csharp-package-cli-create)
+ [Deploying .NET projects using the .NET CLI](#csharp-package-cli-deploy)
+ [Using Lambda layers with the .NET CLI](#csharp-layers)

## Prerequisites
<a name="csharp-package-cli-prerequisites"></a>

**.NET 8 SDK**  
If you haven't already done so, install the [.NET 8](https://dotnet.microsoft.com/en-us/download/dotnet/8.0) SDK and Runtime.

**AWS Amazon.Lambda.Templates .NET project templates**  
To generate your Lambda function code, use the [https://www.nuget.org/packages/Amazon.Lambda.Templates](https://www.nuget.org/packages/Amazon.Lambda.Templates) NuGet package. To install this template package, run the following command:  

```
dotnet new install Amazon.Lambda.Templates
```

**AWS Amazon.Lambda.Tools .NET Global CLI tools**  
To create your Lambda functions, you use the [https://www.nuget.org/packages/Amazon.Lambda.Tools](https://www.nuget.org/packages/Amazon.Lambda.Tools) [.NET Global Tools extension](https://aws.amazon.com/blogs/developer/net-core-global-tools-for-aws/). To install Amazon.Lambda.Tools, run the following command:  

```
dotnet tool install -g Amazon.Lambda.Tools
```
For more information about the Amazon.Lambda.Tools .NET CLI extension, see the [AWS Extensions for .NET CLI](https://github.com/aws/aws-extensions-for-dotnet-cli) repository on GitHub.

## Creating .NET projects using the .NET CLI
<a name="csharp-package-cli-create"></a>

In the .NET CLI, you use the `dotnet new` command to create .NET projects from the command line. Lambda offers additional templates using the [https://www.nuget.org/packages/Amazon.Lambda.Templates](https://www.nuget.org/packages/Amazon.Lambda.Templates) NuGet package.

After installing this package, run the following command to see a list of the available templates.

```
dotnet new list
```

To examine details about a template, use the `help` option. For example, to see details about the `lambda.EmptyFunction` template, run the following command.

```
dotnet new lambda.EmptyFunction --help
```

To create a basic template for a .NET Lambda function, use the `lambda.EmptyFunction` template. This creates a simple function that takes a string as input and converts it to upper case using the `ToUpper` method. This template supports the following options: 
+ `--name` – The name of the function.
+ `--region` – The AWS Region to create the function in.
+ `--profile` – The name of a profile in your AWS SDK for .NET credentials file. To learn more about credential profiles in .NET, see [Configure AWS credentials](https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/net-dg-config-creds.html) in the *AWS SDK for .NET Developer Guide*.

In this example, we create a new empty function named `myDotnetFunction` using the default profile and AWS Region settings:

```
dotnet new lambda.EmptyFunction --name myDotnetFunction
```

This command creates the following files and directories in your project directory.

```
└── myDotnetFunction
    ├── src
    │   └── myDotnetFunction
    │       ├── Function.cs
    │       ├── Readme.md
    │       ├── aws-lambda-tools-defaults.json
    │       └── myDotnetFunction.csproj
    └── test
        └── myDotnetFunction.Tests
            ├── FunctionTest.cs
            └── myDotnetFunction.Tests.csproj
```

Under the `src/myDotnetFunction` directory, examine the following files:
+ **aws-lambda-tools-defaults.json**: This is where you specify the command line options when deploying your Lambda function. For example:

  ```
    "profile" : "default",
    "region" : "us-east-2",
    "configuration" : "Release",
    "function-architecture": "x86_64",
    "function-runtime":"dotnet8",
    "function-memory-size" : 256,
    "function-timeout" : 30,
    "function-handler" : "myDotnetFunction::myDotnetFunction.Function::FunctionHandler"
  ```
+ **Function.cs**: Your Lambda handler function code. It's a C\# template that includes the default `Amazon.Lambda.Core` library and a default `LambdaSerializer` attribute. For more information on serialization requirements and options, see [Serialization in C\# Lambda functions](csharp-handler.md#csharp-handler-serializer). It also includes a sample function that you can edit to apply your Lambda function code.

  ```
  using Amazon.Lambda.Core;
  
  // Assembly attribute to enable the Lambda function's JSON input to be converted into a .NET class.
  [assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]
  
  namespace myDotnetFunction;
  
  public class Function
  {
  
      /// <summary>
      /// A simple function that takes a string and does a ToUpper
      /// </summary≫
      /// <param name="input"></param>
      /// <param name="context"></param>
      /// <returns></returns>
      public string FunctionHandler(string input, ILambdaContext context)
      {
          return input.ToUpper();
      }
  }
  ```
+ **myDotnetFunction.csproj**: An [MSBuild](https://msdn.microsoft.com/en-us/library/dd393574.aspx) file that lists the files and assemblies that comprise your application.

  ```
  <Project Sdk="Microsoft.NET.Sdk">
    <PropertyGroup>
      <TargetFramework>net8.0</TargetFramework>
      <ImplicitUsings>enable</ImplicitUsings>
      <Nullable>enable</Nullable>
      <GenerateRuntimeConfigurationFiles>true</GenerateRuntimeConfigurationFiles>
      <AWSProjectType>Lambda</AWSProjectType>
      <!-- This property makes the build directory similar to a publish directory and helps the AWS .NET Lambda Mock Test Tool find project dependencies. -->
      <CopyLocalLockFileAssemblies>true</CopyLocalLockFileAssemblies>
      <!-- Generate ready to run images during publishing to improve cold start time. -->
      <PublishReadyToRun>true</PublishReadyToRun>
    </PropertyGroup>
    <ItemGroup>
      <PackageReference Include="Amazon.Lambda.Core" Version="2.2.0" />
      <PackageReference Include="Amazon.Lambda.Serialization.SystemTextJson" Version="2.4.0" />
    </ItemGroup>
  </Project>
  ```
+ **Readme**: Use this file to document your Lambda function.

Under the `myfunction/test` directory, examine the following files:
+ **myDotnetFunction.Tests.csproj**: As noted previously, this is an [MSBuild](https://msdn.microsoft.com/en-us/library/dd393574.aspx) file that lists the files and assemblies that comprise your test project. Note also that it includes the `Amazon.Lambda.Core` library, so you can seamlessly integrate any Lambda templates required to test your function.

  ```
  <Project Sdk="Microsoft.NET.Sdk">
     ... 
  
      <PackageReference Include="Amazon.Lambda.Core" Version="2.2.0 " />
     ...
  ```
+ **FunctionTest.cs**: The same C\# code template file that it is included in the `src` directory. Edit this file to mirror your function's production code and test it before uploading your Lambda function to a production environment.

  ```
  using Xunit;
  using Amazon.Lambda.Core;
  using Amazon.Lambda.TestUtilities;
  
  using MyFunction;
  
  namespace MyFunction.Tests
  {
      public class FunctionTest
      {
          [Fact]
          public void TestToUpperFunction()
          {
  
              // Invoke the lambda function and confirm the string was upper cased.
              var function = new Function();
              var context = new TestLambdaContext();
              var upperCase = function.FunctionHandler("hello world", context);
  
              Assert.Equal("HELLO WORLD", upperCase);
          }
      }
  }
  ```

## Deploying .NET projects using the .NET CLI
<a name="csharp-package-cli-deploy"></a>

To build your deployment package and deploy it to Lambda, you use the `Amazon.Lambda.Tools` CLI tools. To deploy your function from the files you created in the previous steps, first navigate into the folder containing your function's `.csproj` file.

```
cd myDotnetFunction/src/myDotnetFunction
```

To deploy your code to Lambda as a .zip deployment package, run the following command. Choose your own function name.

```
dotnet lambda deploy-function {{myDotnetFunction}}
```

During the deployment, the wizard asks you to select a [Defining Lambda function permissions with an execution role](lambda-intro-execution-role.md). For this example, select the `lambda_basic_role`.

After you have deployed your function, you can test it in the cloud using the `dotnet lambda invoke-function` command. For the example code in the `lambda.EmptyFunction` template, you can test your function by passing in a string using the `--payload` option.

```
dotnet lambda invoke-function myDotnetFunction --payload "Just checking if everything is OK"
```

If your function has been successfully deployed, you should see output similar to the following.

```
dotnet lambda invoke-function myDotnetFunction --payload "Just checking if everything is OK"
Amazon Lambda Tools for .NET Core applications (5.8.0)
Project Home: https://github.com/aws/aws-extensions-for-dotnet-cli, https://github.com/aws/aws-lambda-dotnet

Payload:
"JUST CHECKING IF EVERYTHING IS OK"

Log Tail:
START RequestId: {{id}} Version: $LATEST
END RequestId: {{id}}
REPORT RequestId: {{id}}  Duration: 0.99 ms       Billed Duration: 1 ms         Memory Size: 256 MB     Max Memory Used: 12 MB
```

## Using Lambda layers with the .NET CLI
<a name="csharp-layers"></a>

**Note**  
While it's possible to use [layers](chapter-layers.md) with functions in .NET, we recommend against it. Functions in .NET that use layers manually load the shared assemblies into memory during the `Init` phase, which can increase cold start times. Instead, include all shared code at compile time to take advantage of the built-in optimizations of the .NET compiler.

The .NET CLI supports commands to help you publish layers and deploy C\# functions that consume layers. To publish a layer to a specified Amazon S3 bucket, run the following command in the same directory as your `.csproj` file:

```
dotnet lambda publish-layer {{<layer_name>}} --layer-type runtime-package-store --s3-bucket {{<s3_bucket_name>}}
```

Then, when you deploy your function using the .NET CLI, specify the layer ARN the consume in the following command:

```
dotnet lambda deploy-function {{<function_name>}} --function-layers {{arn:aws:lambda:us-east-1:123456789012:layer:layer-name:1}}
```

For a complete example of a Hello World function, see the [ blank-csharp-with-layer](https://github.com/awsdocs/aws-lambda-developer-guide/tree/main/sample-apps/blank-csharp-with-layer) sample.