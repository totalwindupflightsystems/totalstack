---
id: "@specs/aws/lambda/docs/java-samples"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Sample apps"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Sample apps

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/java-samples
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Java sample applications for AWS Lambda
<a name="java-samples"></a>

The GitHub repository for this guide provides sample applications that demonstrate the use of Java in AWS Lambda. Each sample application includes scripts for easy deployment and cleanup, an CloudFormation template, and supporting resources.

**Sample Lambda applications in Java**
+ [example-java](https://github.com/awsdocs/aws-lambda-developer-guide/tree/main/sample-apps/example-java) – A Java function that demonstrates how you can use Lambda to process orders. This function illustrates how to define and deserialize a custom input event object, use the AWS SDK, and output logging.
+ [java-basic](https://github.com/awsdocs/aws-lambda-developer-guide/tree/main/sample-apps/java-basic) – A collection of minimal Java functions with unit tests and variable logging configuration.
+ [java-events](https://github.com/awsdocs/aws-lambda-developer-guide/tree/main/sample-apps/java-events) – A collection of Java functions that contain skeleton code for how to handle events from various services such as Amazon API Gateway, Amazon SQS, and Amazon Kinesis. These functions use the latest version of the [aws-lambda-java-events](java-package.md) library (3.0.0 and newer). These examples do not require the AWS SDK as a dependency.
+ [s3-java](https://github.com/awsdocs/aws-lambda-developer-guide/tree/main/sample-apps/s3-java) – A Java function that processes notification events from Amazon S3 and uses the Java Class Library (JCL) to create thumbnails from uploaded image files.
+ [layer-java](https://github.com/awsdocs/aws-lambda-developer-guide/tree/main/sample-apps/layer-java) – A Java function that illustrates how to use a Lambda layer to package dependencies separate from your core function code.

**Running popular Java frameworks on Lambda**
+ [spring-cloud-function-samples](https://github.com/spring-cloud/spring-cloud-function/tree/3.2.x/spring-cloud-function-samples/function-sample-aws) – An example from Spring that shows how to use the [Spring Cloud Function](https://spring.io/projects/spring-cloud-function) framework to create AWS Lambda functions. 
+ [Serverless Spring Boot Application Demo](https://github.com/aws-samples/serverless-java-frameworks-samples/tree/main/springboot) – An example that shows how to set up a typical Spring Boot application in a managed Java runtime with and without SnapStart, or as a GraalVM native image with a custom runtime.
+ [Serverless Micronaut Application Demo](https://github.com/aws-samples/serverless-java-frameworks-samples/tree/main/micronaut) – An example that shows how to use Micronaut in a managed Java runtime with and without SnapStart, or as a GraalVM native image with a custom runtime. Learn more in the [Micronaut/Lambda guides](https://guides.micronaut.io/latest/tag-lambda.html).
+ [Serverless Quarkus Application Demo](https://github.com/aws-samples/serverless-java-frameworks-samples/tree/main/quarkus) – An example that shows how to use Quarkus in a managed Java runtime with and without SnapStart, or as a GraalVM native image with a custom runtime. Learn more in the [Quarkus/Lambda guide](https://quarkus.io/guides/aws-lambda) and [Quarkus/SnapStart guide](https://quarkus.io/guides/aws-lambda-snapstart).

If you're new to Lambda functions in Java, start with the `java-basic` examples. To get started with Lambda event sources, see the `java-events` examples. Both of these example sets show the use of Lambda's Java libraries, environment variables, the AWS SDK, and the AWS X-Ray SDK. These examples require minimal setup and you can deploy them from the command line in less than a minute.