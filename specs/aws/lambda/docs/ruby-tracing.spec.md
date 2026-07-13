---
id: "@specs/aws/lambda/docs/ruby-tracing"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Tracing"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Tracing

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/ruby-tracing
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Instrumenting Ruby code in AWS Lambda
<a name="ruby-tracing"></a>

Lambda integrates with AWS X-Ray to enable you to trace, debug, and optimize Lambda applications. You can use X-Ray to trace a request as it traverses resources in your application, from the frontend API to storage and database on the backend. By simply adding the X-Ray SDK library to your build configuration, you can record errors and latency for any call that your function makes to an AWS service.

After you've configured active tracing, you can observe specific requests through your application. The [ X-Ray service graph](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html#xray-concepts-servicegraph) shows information about your application and all its components. The following example shows an application with two functions. The primary function processes events and sometimes returns errors. The second function at the top processes errors that appear in the first's log group and uses the AWS SDK to call X-Ray, Amazon Simple Storage Service (Amazon S3), and Amazon CloudWatch Logs.

![A diagram that shows two separate applications and their respective service maps in X-Ray](http://docs.aws.amazon.com/lambda/latest/dg/images/sample-errorprocessor-servicemap.png)


To toggle active tracing on your Lambda function with the console, follow these steps:

**To turn on active tracing**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Choose a function.

1. Choose **Configuration** and then choose **Monitoring and operations tools**.

1. Under **Additional monitoring tools**, choose **Edit**.

1. Under **CloudWatch Application Signals and AWS X-Ray**, choose **Enable** for **Lambda service traces**.

1. Choose **Save**.

**Pricing**  
You can use X-Ray tracing for free each month up to a certain limit as part of the AWS Free Tier. Beyond that threshold, X-Ray charges for trace storage and retrieval. For more information, see [AWS X-Ray pricing](https://aws.amazon.com/xray/pricing/).

Your function needs permission to upload trace data to X-Ray. When you activate tracing in the Lambda console, Lambda adds the required permissions to your function's [execution role](lambda-intro-execution-role.md). Otherwise, add the [AWSXRayDaemonWriteAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSXRayDaemonWriteAccess) policy to the execution role.

X-Ray doesn't trace all requests to your application. X-Ray applies a sampling algorithm to ensure that tracing is efficient, while still providing a representative sample of all requests. The sampling rate is 1 request per second and 5 percent of additional requests. You can't configure the X-Ray sampling rate for your functions.

In X-Ray, a *trace* records information about a request that is processed by one or more *services*. Lambda records 2 segments per trace, which creates two nodes on the service graph. The following image highlights these two nodes:

![An X-Ray service map with a single function.](http://docs.aws.amazon.com/lambda/latest/dg/images/xray-servicemap-function.png)


The first node on the left represents the Lambda service, which receives the invocation request. The second node represents your specific Lambda function. The following example shows a trace with these two segments. Both are named **my-function**, but one has an origin of `AWS::Lambda` and the other has an origin of `AWS::Lambda::Function`. If the `AWS::Lambda` segment shows an error, the Lambda service had an issue. If the `AWS::Lambda::Function` segment shows an error, your function had an issue.

![An X-Ray trace that shows latency across each subsegment of a specific Lambda invocation.](http://docs.aws.amazon.com/lambda/latest/dg/images/V2_sandbox_images/my-function-2-v1.png)


This example expands the `AWS::Lambda::Function` segment to show its three subsegments.

**Note**  
AWS is currently implementing changes to the Lambda service. Due to these changes, you may see minor differences between the structure and content of system log messages and trace segments emitted by different Lambda functions in your AWS account.  
The example trace shown here illustrates the old-style function segment. The differences between the old- and new-style segments are described in the following paragraphs.  
These changes will be implemented during the coming weeks, and all functions in all AWS Regions except the China and GovCloud regions will transition to use the new-format log messages and trace segments.

The old-style function segment contains the following subsegments:
+ **Initialization** – Represents time spent loading your function and running [initialization code](foundation-progmodel.md). This subsegment only appears for the first event that each instance of your function processes.
+ **Invocation** – Represents the time spent running your handler code.
+ **Overhead** – Represents the time the Lambda runtime spends preparing to handle the next event.

The new-style function segment doesn't contain an `Invocation` subsegment. Instead, customer subsegments are attached directly to the function segment. For more information about the structure of the old- and new-style function segments, see [Understanding X-Ray traces](services-xray.md#services-xray-traces).

You can instrument your handler code to record metadata and trace downstream calls. To record detail about calls that your handler makes to other resources and services, use the X-Ray SDK for Ruby. To get the SDK, add the `aws-xray-sdk` package to your application's dependencies.

**Example [blank-ruby/function/Gemfile](https://github.com/awsdocs/aws-lambda-developer-guide/tree/main/sample-apps/blank-ruby/function/Gemfile)**  

```
# Gemfile
source 'https://rubygems.org'

gem 'aws-xray-sdk', '0.11.4'
gem 'aws-sdk-lambda', '1.39.0'
gem 'test-unit', '3.3.5'
```

To instrument AWS SDK clients, require the `aws-xray-sdk/lambda` module after creating a client in initialization code.

**Example [blank-ruby/function/lambda\_function.rb](https://github.com/awsdocs/aws-lambda-developer-guide/tree/main/sample-apps/blank-ruby/function/lambda_function.rb) – Tracing an AWS SDK client**  

```
# lambda_function.rb
require 'logger'
require 'json'
require 'aws-sdk-lambda'
$client = Aws::Lambda::Client.new()
$client.get_account_settings()

require 'aws-xray-sdk/lambda'

def lambda_handler(event:, context:)
  logger = Logger.new($stdout)
  ...
```

In X-Ray, a *trace* records information about a request that is processed by one or more *services*. Lambda records 2 segments per trace, which creates two nodes on the service graph. The following image highlights these two nodes:

![An X-Ray service map with a single function.](http://docs.aws.amazon.com/lambda/latest/dg/images/xray-servicemap-function.png)


The first node on the left represents the Lambda service, which receives the invocation request. The second node represents your specific Lambda function. The following example shows a trace with these two segments. Both are named **my-function**, but one has an origin of `AWS::Lambda` and the other has an origin of `AWS::Lambda::Function`. If the `AWS::Lambda` segment shows an error, the Lambda service had an issue. If the `AWS::Lambda::Function` segment shows an error, your function had an issue.

![An X-Ray trace that shows latency across each subsegment of a specific Lambda invocation.](http://docs.aws.amazon.com/lambda/latest/dg/images/V2_sandbox_images/my-function-2-v1.png)


This example expands the `AWS::Lambda::Function` segment to show its three subsegments.

**Note**  
AWS is currently implementing changes to the Lambda service. Due to these changes, you may see minor differences between the structure and content of system log messages and trace segments emitted by different Lambda functions in your AWS account.  
The example trace shown here illustrates the old-style function segment. The differences between the old- and new-style segments are described in the following paragraphs.  
These changes will be implemented during the coming weeks, and all functions in all AWS Regions except the China and GovCloud regions will transition to use the new-format log messages and trace segments.

The old-style function segment contains the following subsegments:
+ **Initialization** – Represents time spent loading your function and running [initialization code](foundation-progmodel.md). This subsegment only appears for the first event that each instance of your function processes.
+ **Invocation** – Represents the time spent running your handler code.
+ **Overhead** – Represents the time the Lambda runtime spends preparing to handle the next event.

The new-style function segment doesn't contain an `Invocation` subsegment. Instead, customer subsegments are attached directly to the function segment. For more information about the structure of the old- and new-style function segments, see [Understanding X-Ray traces](services-xray.md#services-xray-traces).

You can also instrument HTTP clients, record SQL queries, and create custom subsegments with annotations and metadata. For more information, see [The X-Ray SDK for Ruby](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-ruby.html) in the AWS X-Ray Developer Guide.

**Topics**
+ [Enabling active tracing with the Lambda API](#ruby-tracing-api)
+ [Enabling active tracing with CloudFormation](#ruby-tracing-cloudformation)
+ [Storing runtime dependencies in a layer](#ruby-tracing-layers)

## Enabling active tracing with the Lambda API
<a name="ruby-tracing-api"></a>

To manage tracing configuration with the AWS CLI or AWS SDK, use the following API operations:
+ [UpdateFunctionConfiguration](https://docs.aws.amazon.com/lambda/latest/api/API_UpdateFunctionConfiguration.html)
+ [GetFunctionConfiguration](https://docs.aws.amazon.com/lambda/latest/api/API_GetFunctionConfiguration.html)
+ [CreateFunction](https://docs.aws.amazon.com/lambda/latest/api/API_CreateFunction.html)

The following example AWS CLI command enables active tracing on a function named **my-function**.

```
aws lambda update-function-configuration --function-name my-function \
--tracing-config Mode=Active
```

Tracing mode is part of the version-specific configuration when you publish a version of your function. You can't change the tracing mode on a published version.

## Enabling active tracing with CloudFormation
<a name="ruby-tracing-cloudformation"></a>

To activate tracing on an `AWS::Lambda::Function` resource in an CloudFormation template, use the `TracingConfig` property.

**Example [function-inline.yml](https://github.com/awsdocs/aws-lambda-developer-guide/blob/master/templates/function-inline.yml) – Tracing configuration**  

```
Resources:
  function:
    Type: [AWS::Lambda::Function](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html)
    Properties:
      TracingConfig:
        Mode: Active
      ...
```

For an AWS Serverless Application Model (AWS SAM) `AWS::Serverless::Function` resource, use the `Tracing` property.

**Example [template.yml](https://github.com/awsdocs/aws-lambda-developer-guide/tree/main/sample-apps/blank-nodejs/template.yml) – Tracing configuration**  

```
Resources:
  function:
    Type: [AWS::Serverless::Function](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-function.html)
    Properties:
      Tracing: Active
      ...
```

## Storing runtime dependencies in a layer
<a name="ruby-tracing-layers"></a>

If you use the X-Ray SDK to instrument AWS SDK clients your function code, your deployment package can become quite large. To avoid uploading runtime dependencies every time you update your function code, package the X-Ray SDK in a [Lambda layer](chapter-layers.md).

The following example shows an `AWS::Serverless::LayerVersion` resource that stores X-Ray SDK for Ruby.

**Example [template.yml](https://github.com/awsdocs/aws-lambda-developer-guide/tree/main/sample-apps/blank-ruby/template.yml) – Dependencies layer**  

```
Resources:
  function:
    Type: [AWS::Serverless::Function](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-function.html)
    Properties:
      CodeUri: function/.
      Tracing: Active
      Layers:
        - !Ref libs
      ...
  libs:
    Type: [AWS::Serverless::LayerVersion](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-layerversion.html)
    Properties:
      LayerName: blank-ruby-lib
      Description: Dependencies for the blank-ruby sample app.
      ContentUri: lib/.
      CompatibleRuntimes:
        - ruby2.5
```

With this configuration, you update the library layer only if you change your runtime dependencies. Since the function deployment package contains only your code, this can help reduce upload times.

Creating a layer for dependencies requires build changes to generate the layer archive prior to deployment. For a working example, see the [blank-ruby](https://github.com/awsdocs/aws-lambda-developer-guide/tree/main/sample-apps/blank-ruby) sample application.