---
id: "@specs/aws/lambda/docs/configuration-ephemeral-storage"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Ephemeral storage"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Ephemeral storage

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/configuration-ephemeral-storage
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Configure ephemeral storage for Lambda functions
<a name="configuration-ephemeral-storage"></a>

Lambda provides ephemeral storage for functions in the `/tmp` directory. This storage is temporary and unique to each execution environment. You can control the amount of ephemeral storage allocated to your function using the **Ephemeral storage** setting. You can configure ephemeral storage between 512 MB and 10,240 MB, in 1-MB increments. All data stored in `/tmp` is encrypted at rest with a key managed by AWS.

This page describes common use cases and how to update the ephemeral storage for a Lambda function.

**Topics**
+ [Common use cases for increased ephemeral storage](#configuration-ephemeral-storage-use-cases)
+ [Configuring ephemeral storage (console)](#configuration-ephemeral-storage-console)
+ [Configuring ephemeral storage (AWS CLI)](#configuration-ephemeral-storage-cli)
+ [Configuring ephemeral storage (AWS SAM)](#configuration-ephemeral-storage-sam)

## Common use cases for increased ephemeral storage
<a name="configuration-ephemeral-storage-use-cases"></a>

Here are several common use cases that benefit from increased ephemeral storage:
+ **Extract-transform-load (ETL) jobs:** Increase ephemeral storage when your code performs intermediate computation or downloads other resources to complete processing. More temporary space enables more complex ETL jobs to run in Lambda functions.
+ **Machine learning (ML) inference:** Many inference tasks rely on large reference data files, including libraries and models. With more ephemeral storage, you can download larger models from Amazon Simple Storage Service (Amazon S3) to `/tmp` and use them in your processing.
+ **Data processing:** For workloads that download objects from Amazon S3 in response to S3 events, more `/tmp` space makes it possible to handle larger objects without using in-memory processing. Workloads that create PDFs or process media also benefit from more ephemeral storage.
+ **Graphics processing:** Image processing is a common use case for Lambda-based applications. For workloads that process large TIFF files or satellite images, more ephemeral storage makes it easier to use libraries and perform the computation in Lambda.

## Configuring ephemeral storage (console)
<a name="configuration-ephemeral-storage-console"></a>

You can configure ephemeral storage in the Lambda console.

**To modify ephemeral storage for a function**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Choose a function.

1. Choose the **Configuration** tab and then choose **General configuration**.  
![The Configuration tab in the Lambda console.](http://docs.aws.amazon.com/lambda/latest/dg/images/configuration-tab.png)

1. Under **General configuration**, choose **Edit**.

1. For **Ephemeral storage**, set a value between 512 MB and 10,240 MB, in 1-MB increments.

1. Choose **Save**.

## Configuring ephemeral storage (AWS CLI)
<a name="configuration-ephemeral-storage-cli"></a>

You can use the [update-function-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-function-configuration.html) command to configure ephemeral storage.

**Example**  

```
aws lambda update-function-configuration \
  --function-name {{my-function}} \
  --ephemeral-storage {{'{"Size": 1024}'}}
```

## Configuring ephemeral storage (AWS SAM)
<a name="configuration-ephemeral-storage-sam"></a>

You can use the [AWS Serverless Application Model](https://docs.aws.amazon.com//serverless-application-model/latest/developerguide/serverless-getting-started.html ) to configure ephemeral storage for your function. Update the [EphemeralStorage](https://docs.aws.amazon.com//serverless-application-model/latest/developerguide/sam-resource-function.html#sam-function-ephemeralstorage) property in your `template.yaml` file and then run [sam deploy](https://docs.aws.amazon.com//serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-deploy.html).

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
      Timeout: 120
      Handler: index.handler
      Runtime: nodejs22.x
      Architectures:
        - x86_64
      EphemeralStorage:
        Size: {{10240}}
      # Other function properties...
```