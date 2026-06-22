---
id: "@specs/aws/timestream-influxdb/docs/security-iam-awsmanpol"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AWS managed policies"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# AWS managed policies

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/security-iam-awsmanpol
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# AWS managed policies for Amazon Timestream Live Analytics
<a name="security-iam-awsmanpol"></a>







An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they're available for all AWS customers to use. We recommend that you reduce permissions further by defining [ customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services.

For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

**Topics**
+ [AmazonTimestreamInfluxDBFullAccess](#security-iam-awsmanpol-AmazonTimestreamInfluxDBFullAccess)
+ [AmazonTimestreamReadOnlyAccess](#security-iam-awsmanpol-AmazonTimestreamReadOnlyAccess)
+ [AmazonTimestreamConsoleFullAccess](#security-iam-awsmanpol-AmazonTimestreamConsoleFullAccess)
+ [AmazonTimestreamFullAccess](#security-iam-awsmanpol-AmazonTimestreamFullAccess)
+ [Policy updates](#security-iam-awsmanpol-updates)









## AWS managed policy: AmazonTimestreamInfluxDBFullAccess
<a name="security-iam-awsmanpol-AmazonTimestreamInfluxDBFullAccess"></a>

You can attach `AmazonTimestreamInfluxDBFullAccess` to your users, groups, and roles. The policy access to create, update, delete and list Amazon Timestream InfluxDB instances.

**Permission details**  
This policy includes the following permission:
+ `Amazon Timestream` – Provides full administrative access to create, update, delete and list Amazon Timestream InfluxDB instances and create and list parameter groups. 

To review this policy in JSON format, see [AmazonTimestreamInfluxDBFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonTimestreamInfluxDBFullAccess.html).

## AWS managed policy: AmazonTimestreamReadOnlyAccess
<a name="security-iam-awsmanpol-AmazonTimestreamReadOnlyAccess"></a>





You can attach `AmazonTimestreamReadOnlyAccess` to your users, groups, and roles. The policy provides read-only access to Amazon Timestream.

**Permission details**  
This policy includes the following permission:
+ `Amazon Timestream` – Provides read-only access to Amazon Timestream. This policy also grants permission to cancel any running query.

To review this policy in JSON format, see [AmazonTimestreamReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonTimestreamReadOnlyAccess.html).

## AWS managed policy: AmazonTimestreamConsoleFullAccess
<a name="security-iam-awsmanpol-AmazonTimestreamConsoleFullAccess"></a>





You can attach `AmazonTimestreamConsoleFullAccess` to your users, groups, and roles.

The policy provides full access to manage Amazon Timestream using the AWS Management Console. This policy also grants permissions for certain AWS KMS operations and operations to manage your saved queries.

**Permission details**  
This policy includes the following permissions:
+ `Amazon Timestream` – Grants principals full access to Amazon Timestream.
+ `AWS KMS` – Allows principals to list aliases and describe keys.
+ `Amazon S3` – Allows principals to list all Amazon S3 buckets.
+ `Amazon SNS` – Allows principals to list Amazon SNS topics.
+ `IAM` – Allows principals to list IAM roles.
+ `DBQMS` – Allows principals to access, create, delete, describe, and update queries. The Database Query Metadata Service (dbqms) is an internal-only service. It provides your recent and saved queries for the query editor on the AWS Management Console for multiple AWS services, including Amazon Timestream.
+ `Pricing` – Allows principals to access pricing estimation for InfluxDB resource configuration during creation.
+ `Marketplace` – Allows principals to access marketplace resources and create agreements for InfluxDB Cluster with Read Replicas creation.

To review this policy in JSON format, see [AmazonTimestreamConsoleFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonTimestreamConsoleFullAccess.html).

## AWS managed policy: AmazonTimestreamFullAccess
<a name="security-iam-awsmanpol-AmazonTimestreamFullAccess"></a>





You can attach `AmazonTimestreamFullAccess` to your users, groups, and roles.

The policy provides full access to Amazon Timestream. This policy also grants permissions for certain AWS KMS operations.

**Permission details**  
This policy includes the following permissions:
+ `Amazon Timestream` – Grants principals full access to Amazon Timestream.
+ `AWS KMS` – Allows principals to list aliases and describe keys.
+ `Amazon S3` – Allows principals to list all Amazon S3 buckets.

To review this policy in JSON format, see [AmazonTimestreamFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonTimestreamFullAccess.html).

## Timestream Live Analytics updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>



View details about updates to AWS managed policies for Timestream Live Analytics since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the [Timestream Live Analytics Document history](doc-history.md) page.




| Change | Description | Date | 
| --- | --- | --- | 
| [AmazonTimestreamConsoleFullAccess](#security-iam-awsmanpol-AmazonTimestreamConsoleFullAccess) – Update to an existing policy |  Timestream for InfluxDB has added Influx Enterprise marketplace product ID to the existing `AmazonTimestreamInfluxDBFullAccess` managed policy to support subscription to enterprise marketplace offerings. These permissions are restricted to specific AWS Marketplace products through a condition that limits the access to only certain `ProductIds`. See [AmazonTimestreamInfluxDBFullAccess](https://docs.aws.amazon.com/timestream/latest/developerguide/security-iam-awsmanpol-influxdb.html#iam.identitybasedpolicies.predefinedpolicies). | October 17, 2025 | 
| [AmazonTimestreamConsoleFullAccess](#security-iam-awsmanpol-AmazonTimestreamConsoleFullAccess) – Update to an existing policy | Added the AWS Marketplace permissions to the existing `AmazonTimestreamConsoleFullAccess` managed policy to access marketplace resources and create agreements for InfluxDB Cluster with Read Replicas creation.<br />Timestream Live Analytics has also updated this managed policy by adding an `Sid` field.<br />The policy update doesn't impact the usage of the `AmazonTimestreamConsoleFullAccess` managed policy. | August 20, 2025 | 
| [AmazonTimestreamConsoleFullAccess](#security-iam-awsmanpol-AmazonTimestreamConsoleFullAccess) – Update to an existing policy | Added the `pricing:GetProducts` action to the existing `AmazonTimestreamConsoleFullAccess` managed policy to provide pricing estimations for InfluxDB resource configurations during creation.<br />The policy update doesn't impact the usage of the `AmazonTimestreamConsoleFullAccess` managed policy. | June 10, 2025 | 
| [AmazonTimestreamReadOnlyAccess](#security-iam-awsmanpol-AmazonTimestreamReadOnlyAccess) – Update to an existing policy | Added the `timestream:DescribeAccountSettings` action to the existing `AmazonTimestreamReadOnlyAccess` managed policy. This action is used for describing AWS account settings.<br />Timestream Live Analytics has also updated this managed policy by adding an `Sid` field.<br />The policy update doesn't impact the usage of the `AmazonTimestreamReadOnlyAccess` managed policy. | June 03, 2024 | 
| [AmazonTimestreamReadOnlyAccess](#security-iam-awsmanpol-AmazonTimestreamReadOnlyAccess) – Update to an existing policy | Added the `timestream:DescribeBatchLoadTask` and `timestream:ListBatchLoadTasks` actions to the existing `AmazonTimestreamReadOnlyAccess` managed policy. These actions are used when listing and describing batch load tasks.<br />The policy update doesn't impact the usage of the `AmazonTimestreamReadOnlyAccess` managed policy. | February 24, 2023 | 
| [AmazonTimestreamReadOnlyAccess](#security-iam-awsmanpol-AmazonTimestreamReadOnlyAccess) – Update to an existing policy | Added the `timestream:DescribeScheduledQuery` and `timestream:ListScheduledQueries` actions to the existing `AmazonTimestreamReadOnlyAccess` managed policy. These actions are used when listing and describing existing scheduled queries.<br />The policy update doesn't impact the usage of the `AmazonTimestreamReadOnlyAccess` managed policy. | November 29, 2021 | 
| [AmazonTimestreamConsoleFullAccess](#security-iam-awsmanpol-AmazonTimestreamConsoleFullAccess) – Update to an existing policy | Added the `s3:ListAllMyBuckets` action to the existing `AmazonTimestreamConsoleFullAccess` managed policy. This action is used when you specify an Amazon S3 bucket for Timestream to log magnetic store write errors.<br />The policy update doesn't impact the usage of the `AmazonTimestreamConsoleFullAccess` managed policy. | November 29, 2021 | 
| [AmazonTimestreamFullAccess](#security-iam-awsmanpol-AmazonTimestreamFullAccess) – Update to an existing policy | Added the `s3:ListAllMyBuckets` action to the existing `AmazonTimestreamFullAccess` managed policy. This action is used when you specify an Amazon S3 bucket for Timestream to log magnetic store write errors.<br />The policy update doesn't impact the usage of the `AmazonTimestreamFullAccess` managed policy. | November 29, 2021 | 
| [AmazonTimestreamConsoleFullAccess](#security-iam-awsmanpol-AmazonTimestreamConsoleFullAccess) – Update to an existing policy | Removed redundant actions from the existing `AmazonTimestreamConsoleFullAccess` managed policy. Previously, this policy included a redundant action `dbqms:DescribeQueryHistory`. The updated policy removes the redundant action.<br />The policy update doesn't impact the usage of the `AmazonTimestreamConsoleFullAccess` managed policy. | April 23, 2021 | 
| Timestream Live Analytics started tracking changes | Timestream Live Analytics started tracking changes for its AWS managed policies. | April 21, 2021 | 