---
id: "@specs/aws/lambda/docs/dotnet-layers"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Layers"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Layers

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/dotnet-layers
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Working with layers for .NET Lambda functions
<a name="dotnet-layers"></a>

We don't recommend using [layers](chapter-layers.md) to manage dependencies for Lambda functions written in .NET. This is because .NET is a compiled language, and your functions still have to manually load any shared assemblies into memory during the [Init](lambda-runtime-environment.md#runtimes-lifecycle-ib) phase, which can increase cold start times. Using layers not only complicates the deployment process, but also prevents you from taking advantage of built-in compiler optimizations.

To use external dependencies with your .NET handlers, include them directly in your deployment package at compile time. By doing so, you simplify the deployment process and also take advantage of built-in .NET compiler optimizations. For an example of how to import and use dependencies like NuGet packages in your function, see [Define Lambda function handler in C\#](csharp-handler.md).