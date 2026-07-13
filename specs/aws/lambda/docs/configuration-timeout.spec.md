---
id: "@specs/aws/lambda/docs/configuration-timeout"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Timeout"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Timeout

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/configuration-timeout
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Configure Lambda function timeout
<a name="configuration-timeout"></a>

Lambda runs your code for a set amount of time before timing out. *Timeout* is the maximum amount of time in seconds that a Lambda function can run. The default value for this setting is 3 seconds, but you can adjust this in increments of 1 second up to a maximum value of 900 seconds (15 minutes).

This page describes how and when to update the timeout setting for a Lambda function.

**Topics**
+ [Determining the appropriate timeout value for a Lambda function](#configuration-timeout-use-cases)
+ [Configuring timeout (console)](#configuration-timeout-console)
+ [Configuring timeout (AWS CLI)](#configuration-timeout-cli)
+ [Configuring timeout (AWS SAM)](#configuration-timeout-sam)

## Determining the appropriate timeout value for a Lambda function
<a name="configuration-timeout-use-cases"></a>

If the timeout value is close to the average duration of a function, there is a higher risk that the function will time out unexpectedly. The duration of a function can vary based on the amount of data transfer and processing, and the latency of any services the function interacts with. Some common causes of timeout include:
+ Downloads from Amazon Simple Storage Service (Amazon S3) are larger or take longer than average.
+ A function makes a request to another service, which takes longer to respond.
+ The parameters provided to a function require more computational complexity in the function, which causes the invocation to take longer.

When testing your application, ensure that your tests accurately reflect the size and quantity of data and realistic parameter values. Tests often use small samples for convenience, but you should use datasets at the upper bounds of what is reasonably expected for your workload.

## Configuring timeout (console)
<a name="configuration-timeout-console"></a>

You can configure function timeout in the Lambda console.

**To modify the timeout for a function**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Choose a function.

1. Choose the **Configuration** tab and then choose **General configuration**.  
![The Configuration tab in the Lambda console.](http://docs.aws.amazon.com/lambda/latest/dg/images/configuration-tab.png)

1. Under **General configuration**, choose **Edit**.

1. For **Timeout**, set a value between 1 and 900 seconds (15 minutes).

1. Choose **Save**.

## Configuring timeout (AWS CLI)
<a name="configuration-timeout-cli"></a>

You can use the [update-function-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-function-configuration.html) command to configure the timeout value, in seconds. The following example command increases the function timeout to 120 seconds (2 minutes).

**Example**  

```
aws lambda update-function-configuration \
  --function-name {{my-function}} \
  --timeout {{120}}
```

## Configuring timeout (AWS SAM)
<a name="configuration-timeout-sam"></a>

You can use the [AWS Serverless Application Model](https://docs.aws.amazon.com//serverless-application-model/latest/developerguide/serverless-getting-started.html ) to configure the timeout value for your function. Update the [Timeout](https://docs.aws.amazon.com//serverless-application-model/latest/developerguide/sam-resource-function.html#sam-function-timeout) property in your `template.yaml` file and then run [sam deploy](https://docs.aws.amazon.com//serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-deploy.html).

**Example template.yaml**  

```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Description: An AWS Serverless Application Model template describing your function.
Resources:
  {{my-function}}:
    Type: AWS::Serverless::Function
    Properties:
      CodeUri: .
      Description: ''
      MemorySize: 128
      Timeout: {{120}}
      # Other function properties...
```