---
id: "@specs/aws/opensearchserverless/docs/configure-client-source-security-lake"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Amazon Security Lake as a source"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Amazon Security Lake as a source

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/configure-client-source-security-lake
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Using an OpenSearch Ingestion pipeline with Amazon Security Lake as a source
<a name="configure-client-source-security-lake"></a>

You can use the Amazon S3 source plugin within your OpenSearch Ingestion pipeline to ingest data from Amazon Security Lake. Security Lake automatically centralizes security data from AWS environments, on-premises systems, and SaaS providers into a purpose-built data lake.

Amazon Security Lake has the following metadata attributes within a pipeline:
+ `bucket_name`: The name of the Amazon S3 bucket created by Security Lake for storing security data.
+ `path_prefix`: The custom source name defined in the Security Lake IAM role policy.
+ `region`: The AWS Region where the Security Lake S3 bucket is located.
+ `accountID`: The AWS account ID in which Security Lake is enabled.
+ `sts_role_arn`: The ARN of the IAM role intended for use with Security Lake.

## Prerequisites
<a name="sl-prereqs"></a>

Before you create your OpenSearch Ingestion pipeline, perform the following steps:
+ [Enable Security Lake](https://docs.aws.amazon.com/security-lake/latest/userguide/getting-started.html#enable-service).
+ [Create a subscriber](https://docs.aws.amazon.com/security-lake/latest/userguide/subscriber-data-access.html#create-subscriber-data-access) in Security Lake.
  + Choose the sources that you want to ingest into your pipeline.
  + For **Subscriber credentials**, add the ID of the AWS account where you intend to create the pipeline. For the external ID, specify `OpenSearchIngestion-{{{accountid}}}`.
  + For **Data access method**, choose **S3**.
  + For **Notification details**, choose **SQS queue**.

When you create a subscriber, Security Lake automatically creates two inline permissions policies—one for S3 and one for SQS. The policies take the following format: `AmazonSecurityLake-{{amzn-s3-demo-bucket}}-S3` and `AmazonSecurityLake-{{AWSDemo}}-SQS`. To allow your pipeline to access the subscriber sources, you must associate the required permissions with your pipeline role.

## Configure the pipeline role
<a name="sl-pipeline-role"></a>

Create a new permissions policy in IAM that combines only the required permissions from the two policies that Security Lake automatically created. The following example policy shows the least privilege required for an OpenSearch Ingestion pipeline to read data from multiple Security Lake sources:

------
#### [ JSON ]

****  

```
{
   "Version":"2012-10-17",		 	 	 
   "Statement":[
      {
         "Effect":"Allow",
         "Action":[
            "s3:GetObject"
         ],
         "Resource":[
            "arn:aws:s3:::aws-security-data-lake-{{us-east-1}}-{{abcde}}/aws/LAMBDA_EXECUTION/1.0/*",
            "arn:aws:s3:::aws-security-data-lake-{{us-east-1}}-{{abcde}}/aws/S3_DATA/1.0/*",
            "arn:aws:s3:::aws-security-data-lake-{{us-east-1}}-{{abcde}}/aws/VPC_FLOW/1.0/*",
            "arn:aws:s3:::aws-security-data-lake-{{us-east-1}}-{{abcde}}/aws/ROUTE53/1.0/*",
            "arn:aws:s3:::aws-security-data-lake-{{us-east-1}}-{{abcde}}/aws/SH_FINDINGS/1.0/*"
         ]
      },
      {
         "Effect":"Allow",
         "Action":[
            "sqs:ReceiveMessage",
            "sqs:DeleteMessage"
         ],
         "Resource":[
            "arn:aws:sqs:{{us-east-1}}:{{111122223333}}:AmazonSecurityLake-{{abcde}}-Main-Queue"
         ]
      }
   ]
}
```

------

**Important**  
Security Lake doesn’t manage the pipeline role policy for you. If you add or remove sources from your Security Lake subscription, you must manually update the policy. Security Lake creates partitions for each log source, so you need to manually add or remove permissions in the pipeline role.

You must attach these permissions to the IAM role that you specify in the `sts_role_arn` option within the S3 source plugin configuration, under `sqs`.

```
version: "2"
source:
  s3:
    ...
    sqs:
      queue_url: "https://sqs.{{us-east-1}}amazonaws.com/{{account-id}}/AmazonSecurityLake-{{amzn-s3-demo-bucket}}-Main-Queue"
    aws:
      ...
processor:
  ...
sink:
  - opensearch:
      ...
```

## Create the pipeline
<a name="sl-pipeline"></a>

After you add the permissions to the pipeline role, use the preconfigured Security Lake blueprint to create the pipeline. For more information, see [Working with blueprints](pipeline-blueprint.md).

You must specify the `queue_url` option within the `s3` source configuration, which is the Amazon SQS queue URL to read from. To format the URL, locate the **Subscription endpoint** in the subscriber configuration and change `arn:aws:` to `https://`. For example, `https://sqs.{{us-east-1}}amazonaws.com/{{account-id}}/AmazonSecurityLake-{{AWSDemo}}-Main-Queue`.

The `sts_role_arn` that you specify within the S3 source configuration must be the ARN of the pipeline role.