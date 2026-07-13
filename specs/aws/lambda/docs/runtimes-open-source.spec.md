---
id: "@specs/aws/lambda/docs/runtimes-open-source"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Open source repositories"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Open source repositories

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/runtimes-open-source
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Open source repositories
<a name="runtimes-open-source"></a>

AWS Lambda provides a variety of open source tools, libraries, and components to help you build, customize, and optimize your serverless applications. These resources include runtime interface clients, event libraries, container base images, development tools, and sample projects that are maintained by AWS and available on GitHub. By leveraging these open source repositories, you can extend Lambda's capabilities, create custom runtimes, process events from various AWS services, and gain deeper insights into your function's performance. This page provides an overview of the key open source projects that support Lambda development.

## Runtime Interface Clients
<a name="open-source-ric"></a>

Lambda Runtime Interface Clients (RICs) are open source libraries that implement the [Runtime API](runtimes-api.md) and manage the interaction between your function code and the Lambda service. These clients handle receiving invocation events, passing context information, and reporting errors.

The runtime interface clients used by Lambda's managed runtimes and container base images are published as open source. When you build custom runtimes or extend existing ones, you can use these open source libraries to simplify your implementation. The following open source GitHub repositories contain the source code for Lambda's RICs:
+ [Node.js Runtime Interface Client](https://github.com/aws/aws-lambda-nodejs-runtime-interface-client)
+ [Python Runtime Interface Client](https://github.com/aws/aws-lambda-python-runtime-interface-client)
+ [Java Runtime Interface Client](https://github.com/aws/aws-lambda-java-libs/tree/main/aws-lambda-java-runtime-interface-client)
+ [Ruby Runtime Interface Client](https://github.com/aws/aws-lambda-ruby-runtime-interface-client)
+ [.NET Runtime Interface Client](https://github.com/aws/aws-lambda-dotnet)
+ [Rust Runtime Interface Client](https://github.com/aws/aws-lambda-rust-runtime)
+ [Go Runtime Interface Client](https://github.com/aws/aws-lambda-go)
+ [Swift Runtime Interface Client](https://github.com/awslabs/swift-aws-lambda-runtime) (experimental)
+ [C\+\+ Runtime Interface Client](https://github.com/awslabs/aws-lambda-cpp) (experimental)
+ [Lambda Base Images](https://github.com/aws/aws-lambda-base-images)

For more information about using these clients to build custom runtimes, see [Building a custom runtime for AWS Lambda](runtimes-custom.md).

## Event libraries
<a name="open-source-event-libraries"></a>

Lambda event libraries provide type definitions and helper utilities for processing events from various AWS services. These libraries help you parse and handle event data in a type-safe manner, making it easier to work with events from services like Amazon S3, Amazon DynamoDB, and Amazon API Gateway.

For compiled languages, AWS provides the following event libraries:
+ [Java Event Library](https://github.com/aws/aws-lambda-java-libs/tree/main/aws-lambda-java-events)
+ [.NET Event Libraries](https://github.com/aws/aws-lambda-dotnet/tree/master/Libraries/src)
+ [Go Event Library](https://github.com/aws/aws-lambda-go/tree/main/events)
+ [Rust Event Library](https://github.com/awslabs/aws-lambda-rust-runtime)

For interpreted languages like Node.js, Python, and Ruby, events can be parsed directly as JSON objects without requiring a separate library. However, developers using Node.js and Python can leverage powertools for AWS Lambda, which provides built-in schemas for AWS events that offer type hinting, data validation, and functionality similar to what compiled language libraries provide.
+ [Powertools for TypeScript](https://docs.powertools.aws.dev/lambda/typescript/latest/features/parser/#built-in-schemas)
+ [Powertools for Python](https://docs.powertools.aws.dev/lambda/python/latest/utilities/parser/#built-in-models)

## Container base images
<a name="open-source-container-base-images"></a>

AWS provides open source container base images that you can use as a starting point for building container images for your Lambda functions. These base images include the runtime interface client and other components needed to run your functions in the Lambda execution environment.

For more information about the available base images and how to use them, see the [AWS Lambda Base Images](https://github.com/aws/aws-lambda-base-images) repository and [Create a Lambda function using a container image](images-create.md).

## Development tools
<a name="open-source-development-tools"></a>

AWS provides additional open source development tools to help you build and optimize your Lambda functions:

### Powertools for AWS Lambda
<a name="open-source-powertools"></a>

Powertools for AWS Lambda simplifies serverless development with essential utilities to prevent duplicate processing, and batch processing for multi-record handling and Kafka consumer library. These features help you minimize code complexity and operational overhead.

You can also leverage built-in event schema validation, structured logging and tracing, and parameter store integration which are designed to accelerate the creation of production-ready Lambda functions while following AWS well-architected best practices.

GitHub repositories:
+ [Python](https://github.com/aws-powertools/powertools-lambda-python)
+ [TypeScript](https://github.com/aws-powertools/powertools-lambda-typescript)
+ [Java](https://github.com/aws-powertools/powertools-lambda-java)
+ [.NET](https://github.com/aws-powertools/powertools-lambda-dotnet)

### Java development tools
<a name="open-source-java-tools"></a>
+ [Java Profiler (experimental)](https://github.com/aws/aws-lambda-java-libs/tree/main/experimental/aws-lambda-java-profiler) - A tool for profiling Java Lambda functions.
+ [ Java Libraries](https://github.com/aws/aws-lambda-java-libs) - A repository that contains a comprehensive collection of Java libraries and tools for Lambda development, including key projects such as JUnit testing utilities and profiling tools.
+ [Serverless Java Container](https://github.com/aws/serverless-java-container) - A library that enables you to run existing Java applications on Lambda with minimal changes.

### .NET development tools
<a name="open-source-dotnet-tools"></a>

The [AWS Lambda .NET](https://github.com/aws/aws-lambda-dotnet) repository provides .NET libraries and tools for Lambda development, including key projects such as for AWS Lambda tools for the .NET CLI and .NET Core server for hosting .NET Core applications.

## Sample projects
<a name="open-source-sample-projects"></a>

Explore a comprehensive collection of sample Lambda projects and applications at [Serverless Land repositories](https://serverlessland.com/repos). These samples demonstrate various Lambda use cases, integration patterns, and best practices to help you get started with your serverless applications.