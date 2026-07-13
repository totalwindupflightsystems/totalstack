---
id: "@specs/aws/lambda/docs/rust-layers"
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
> **spec:id:** @specs/aws/lambda/docs/rust-layers
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Working with layers for Rust Lambda functions
<a name="rust-layers"></a>

We don't recommend using [layers](chapter-layers.md) to manage dependencies for Lambda functions written in Rust. This is because Lambda functions in Rust compile into a single executable, which you provide to Lambda when you deploy your function. This executable contains your compiled function code, along with all of its dependencies. Using layers not only complicates this process, but also leads to increased cold start times because your functions need to manually load extra assemblies into memory during the init phase.

To use external dependencies with your Rust handlers, include them directly in your deployment package. By doing so, you simplify the deployment process and also take advantage of built-in Rust compiler optimizations. For an example of how to import and use a dependency like the AWS SDK for Rust in your function, see [Define Lambda function handlers in Rust](rust-handler.md).