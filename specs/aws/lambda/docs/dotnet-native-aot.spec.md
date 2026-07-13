---
id: "@specs/aws/lambda/docs/dotnet-native-aot"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Native AOT compilation"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Native AOT compilation

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/dotnet-native-aot
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Compile .NET Lambda function code to a native runtime format
<a name="dotnet-native-aot"></a>

.NET 8 supports native ahead-of-time (AOT) compilation. With native AOT, you can compile your Lambda function code to a native runtime format, which removes the need to compile .NET code at runtime. Native AOT compilation can reduce the cold start time for Lambda functions that you write in .NET. For more information, see [Introducing the .NET 8 runtime for AWS Lambda](https://aws.amazon.com/blogs/compute/introducing-the-net-8-runtime-for-aws-lambda/) on the AWS Compute Blog.

**Topics**
+ [Lambda runtime](#dotnet-native-aot-runtime)
+ [Prerequisites](#dotnet-native-aot-prerequisites)
+ [Getting started](#dotnet-native-aot-getting-started)
+ [Serialization](#dotnet-native-aot-serialization)
+ [Trimming](#dotnet-native-aot-trimming)
+ [Troubleshooting](#dotnet-native-aot-troubleshooting)

## Lambda runtime
<a name="dotnet-native-aot-runtime"></a>

To deploy a Lambda function build with native AOT compilation, use the managed .NET 8 Lambda runtime. This runtime supports the use of both x86\_64 and arm64 architectures.

When you deploy a .NET Lambda function without using AOT, your application is first compiled into Intermediate Language (IL) code. At runtime, the just-in-time (JIT) compiler in the Lambda runtime takes the IL code and compiles it into machine code as needed. With a Lambda function that is compiled ahead of time with native AOT, you compile your code into machine code when you deploy your function, so you're not dependent on the .NET runtime or SDK in the Lambda runtime to compile your code before it runs.

One limitation of AOT is that your application code must be compiled in an environment with the same Amazon Linux 2023 (AL2023) operating system that the .NET 8 runtime uses. The .NET Lambda CLI provides functionality to compile your application in a Docker container using an AL2023 image.

To avoid potential issues with cross-architecture compatibility, we strongly recommend that you compile your code in an environment with the same processor architecture that you configure for your function. To learn more about the limitations of cross-architecture compilation, see [Cross-compilation](https://learn.microsoft.com/en-us/dotnet/core/deploying/native-aot/cross-compile) in the Microsoft .NET documentation.

## Prerequisites
<a name="dotnet-native-aot-prerequisites"></a>

**Docker**  
To use native AOT, your function code must be compiled in an environment with the same AL2023 operating system as the .NET 8 runtime. The .NET CLI commands in the following sections use Docker to develop and build Lambda functions in an AL2023 environment.

**.NET 8 SDK**  
Native AOT compilation is a feature of .NET 8. You must install the [.NET 8 SDK](https://dotnet.microsoft.com/en-us/download/dotnet/8.0) on your build machine, not only the runtime.

**Amazon.Lambda.Tools**  
To create your Lambda functions, you use the [https://www.nuget.org/packages/Amazon.Lambda.Tools](https://www.nuget.org/packages/Amazon.Lambda.Tools) [.NET Global Tools extension](https://aws.amazon.com/blogs/developer/net-core-global-tools-for-aws/). To install Amazon.Lambda.Tools, run the following command:  

```
dotnet tool install -g Amazon.Lambda.Tools
```
For more information about the Amazon.Lambda.Tools .NET CLI extension, see the [AWS Extensions for .NET CLI](https://github.com/aws/aws-extensions-for-dotnet-cli) repository on GitHub.

**Amazon.Lambda.Templates**  
To generate your Lambda function code, use the [https://www.nuget.org/packages/Amazon.Lambda.Templates](https://www.nuget.org/packages/Amazon.Lambda.Templates) NuGet package. To install this template package, run the following command:  

```
dotnet new install Amazon.Lambda.Templates
```

## Getting started
<a name="dotnet-native-aot-getting-started"></a>

Both the .NET Global CLI and the AWS Serverless Application Model (AWS SAM) provide getting started templates for building applications using native AOT. To build your first native AOT Lambda function, carry out the steps in the following instructions.

**To initialize and deploy a native AOT compiled Lambda function**

1. Initialize a new project using the native AOT template and then navigate into the directory containing the created `.cs` and `.csproj` files. In this example, we name our function `NativeAotSample`.

   ```
   dotnet new lambda.NativeAOT -n NativeAotSample
   cd ./NativeAotSample/src/NativeAotSample
   ```

   The `Function.cs` file created by the native AOT template contains the following function code.

   ```
   using Amazon.Lambda.Core;
   using Amazon.Lambda.RuntimeSupport;
   using Amazon.Lambda.Serialization.SystemTextJson;
   using System.Text.Json.Serialization;
   
   namespace NativeAotSample;
   
   public class Function
   {
       /// <summary>
       /// The main entry point for the Lambda function. The main function is called once during the Lambda init phase. It
       /// initializes the .NET Lambda runtime client passing in the function handler to invoke for each Lambda event and
       /// the JSON serializer to use for converting Lambda JSON format to the .NET types.
       /// </summary>
       private static async Task Main()
       {
           Func<string, ILambdaContext, string> handler = FunctionHandler;
           await LambdaBootstrapBuilder.Create(handler, new SourceGeneratorLambdaJsonSerializer<LambdaFunctionJsonSerializerContext>())
               .Build()
               .RunAsync();
       }
   
       /// <summary>
       /// A simple function that takes a string and does a ToUpper.
       ///
       /// To use this handler to respond to an AWS event, reference the appropriate package from
       /// https://github.com/aws/aws-lambda-dotnet#events
       /// and change the string input parameter to the desired event type. When the event type
       /// is changed, the handler type registered in the main method needs to be updated and the LambdaFunctionJsonSerializerContext
       /// defined below will need the JsonSerializable updated. If the return type and event type are different then the
       /// LambdaFunctionJsonSerializerContext must have two JsonSerializable attributes, one for each type.
       ///
       // When using Native AOT extra testing with the deployed Lambda functions is required to ensure
       // the libraries used in the Lambda function work correctly with Native AOT. If a runtime
       // error occurs about missing types or methods the most likely solution will be to remove references to trim-unsafe
       // code or configure trimming options. This sample defaults to partial TrimMode because currently the AWS
       // SDK for .NET does not support trimming. This will result in a larger executable size, and still does not
       // guarantee runtime trimming errors won't be hit.
       /// </summary>
       /// <param name="input"></param>
       /// <param name="context"></param>
       /// <returns></returns>
       public static string FunctionHandler(string input, ILambdaContext context)
       {
           return input.ToUpper();
       }
   }
   
   /// <summary>
   /// This class is used to register the input event and return type for the FunctionHandler method with the System.Text.Json source generator.
   /// There must be a JsonSerializable attribute for each type used as the input and return type or a runtime error will occur
   /// from the JSON serializer unable to find the serialization information for unknown types.
   /// </summary>
   [JsonSerializable(typeof(string))]
   public partial class LambdaFunctionJsonSerializerContext : JsonSerializerContext
   {
       // By using this partial class derived from JsonSerializerContext, we can generate reflection free JSON Serializer code at compile time
       // which can deserialize our class and properties. However, we must attribute this class to tell it what types to generate serialization code for.
       // See https://docs.microsoft.com/en-us/dotnet/standard/serialization/system-text-json-source-generation
   ```

   Native AOT compiles your application into a single, native binary. The entrypoint of that binary is the `static Main` method. Within `static Main`, the Lambda runtime is bootstrapped and the `FunctionHandler` method set up. As part of the runtime bootstrap, a source generated serializer is configured using `new SourceGeneratorLambdaJsonSerializer<LambdaFunctionJsonSerializerContext>()`

1. To deploy your application to Lambda, ensure that Docker is running in your local environment and run the following command.

   ```
   dotnet lambda deploy-function
   ```

   Behind the scenes, the .NET global CLI downloads an AL2023 Docker image and compiles your application code inside a running container. The compiled binary is output back to your local filesystem before being deployed to Lambda.

1. Test your function by running the following command. Replace `<FUNCTION_NAME>` with the name you chose for your function in the deployment wizard.

   ```
   dotnet lambda invoke-function <FUNCTION_NAME> --payload "hello world"
   ```

   The response from the CLI includes performance details for the cold start (initialization duration) and total run time for your function invocation.

1. To delete the AWS resources you created by following the preceding steps, run the following command. Replace `<FUNCTION_NAME>` with the name you chose for your function in the deployment wizard. By deleting AWS resources that you're no longer using, you prevent unnecessary charges being billed to your AWS account.

   ```
   dotnet lambda delete-function <FUNCTION_NAME>
   ```

## Serialization
<a name="dotnet-native-aot-serialization"></a>

To deploy functions to Lambda using native AOT, your function code must use [source generated serialization](https://learn.microsoft.com/en-us/dotnet/standard/serialization/system-text-json/source-generation-modes?pivots=dotnet-8-0). Instead of using run-time reflection to gather the metadata needed to access object properties for serialization, source generators generate C\# source files that are compiled when you build your application. To configure your source generated serializer correctly, ensure that you include any input and output objects your function uses, as well as any custom types. For example, a Lambda function that receives events from an API Gateway REST API and returns a custom `Product` type would include a serializer defined as follows.

```
[JsonSerializable(typeof(APIGatewayProxyRequest))]
[JsonSerializable(typeof(APIGatewayProxyResponse))]
[JsonSerializable(typeof(Product))]
public partial class CustomSerializer : JsonSerializerContext
{
}
```

## Trimming
<a name="dotnet-native-aot-trimming"></a>

Native AOT trims your application code as part of the compilation to ensure that the binary is as small as possible. .NET 8 for Lambda provides improved trimming support compared to previous versions of .NET. Support has been added to the [Lambda runtime libraries](https://github.com/aws/aws-lambda-dotnet/pull/1596), [AWS .NET SDK](https://github.com/aws/aws-sdk-net/pulls?q=is%3Apr+trimming), [.NET Lambda Annotations](https://github.com/aws/aws-lambda-dotnet/pull/1610), and .NET 8 itself.

These improvements offer the potential to eliminate build-time trimming warnings, but .NET will never be completely trim safe. This means that parts of libraries that your function relies on may be trimmed out as part of the compilation step. You can manage this by defining `TrimmerRootAssemblies` as part of your `.csproj` file as shown in the following example. 

```
<ItemGroup>
    <TrimmerRootAssembly Include="AWSSDK.Core" />
    <TrimmerRootAssembly Include="AWSXRayRecorder.Core" />
    <TrimmerRootAssembly Include="AWSXRayRecorder.Handlers.AwsSdk" />
    <TrimmerRootAssembly Include="Amazon.Lambda.APIGatewayEvents" />
    <TrimmerRootAssembly Include="bootstrap" />
    <TrimmerRootAssembly Include="Shared" />
</ItemGroup>
```

Note that when you receive a trim warning, adding the class that generates the warning to `TrimmerRootAssembly` might not resolve the issue. A trim warning indicates that the class is trying to access some other class that can't be determined until runtime. To avoid runtime errors, add this second class to `TrimmerRootAssembly`.

To learn more about managing trim warnings, see [Introduction to trim warnings](https://learn.microsoft.com/en-us/dotnet/core/deploying/trimming/fixing-warnings) in the Microsoft .NET documentation.

## Troubleshooting
<a name="dotnet-native-aot-troubleshooting"></a>

**Error: Cross-OS native compilation is not supported.**  
Your version of the Amazon.Lambda.Tools .NET Core global tool is out of date. Update to the latest version and try again.

**Docker: image operating system "linux" cannot be used on this platform.**  
Docker on your system is configured to use Windows containers. Swap to Linux containers to run the native AOT build environment.

For more information about common errors, see the [AWS NativeAOT for .NET](https://github.com/awslabs/dotnet-nativeaot-labs#common-errors) repository on GitHub.