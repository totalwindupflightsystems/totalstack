---
id: "@specs/aws/opensearchserverless/docs/ac-managed"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AWS managed policies"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# AWS managed policies

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/ac-managed
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AWS managed policies for Amazon OpenSearch Service
<a name="ac-managed"></a>

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they're available for all AWS customers to use. We recommend that you reduce permissions further by defining [ customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services.

For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

## AmazonOpenSearchDirectQueryGlueCreateAccess
<a name="AmazonOpenSearchDirectQueryGlueCreateAccess"></a>

Grants Amazon OpenSearch Service Direct Query Service access to the `CreateDatabase`, `CreatePartition`,`CreateTable`, and `BatchCreatePartition` AWS Glue API.

You can find the [AmazonOpenSearchDirectQueryGlueCreateAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonOpenSearchDirectQueryGlueCreateAccess) policy in the IAM console.

## AmazonOpenSearchServiceFullAccess
<a name="AmazonOpenSearchServiceFullAccess"></a>

Grants full access to the OpenSearch Service configuration API operations and resources for an AWS account.

You can find the [AmazonOpenSearchServiceFullAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonOpenSearchServiceFullAccess) policy in the IAM console.

## AmazonOpenSearchServiceReadOnlyAccess
<a name="AmazonOpenSearchServiceReadOnlyAccess"></a>

Grants read-only access to all OpenSearch Service resources for an AWS account.

You can find the [AmazonOpenSearchServiceReadOnlyAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonOpenSearchServiceReadOnlyAccess) policy in the IAM console.

## AmazonOpenSearchServiceRolePolicy
<a name="AmazonOpenSearchServiceRolePolicy"></a>

You can't attach `AmazonOpenSearchServiceRolePolicy` to your IAM entities. This policy is attached to a service-linked role that allows OpenSearch Service to access account resources. For more information, see [Permissions](slr-aos.md#slr-permissions).

You can find the [AmazonOpenSearchServiceRolePolicy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonOpenSearchServiceRolePolicy) policy in the IAM console.

## AmazonOpenSearchServiceCognitoAccess
<a name="AmazonOpenSearchServiceCognitoAccess"></a>

Provides the minimum Amazon Cognito permissions necessary to enable [Cognito authentication](cognito-auth.md).

You can find the [AmazonOpenSearchServiceCognitoAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonOpenSearchServiceCognitoAccess) policy in the IAM console.

## AmazonOpenSearchIngestionServiceRolePolicy
<a name="AmazonOpenSearchIngestionServiceRolePolicy"></a>

You can't attach `AmazonOpenSearchIngestionServiceRolePolicy` to your IAM entities. This policy is attached to a service-linked role that allows OpenSearch Ingestion to enable VPC access for ingestion pipelines, create tags, and publish ingestion-related CloudWatch metrics to your account. For more information, see [Using service-linked roles for Amazon OpenSearch Service](slr.md).

You can find the [AmazonOpenSearchIngestionServiceRolePolicy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonOpenSearchIngestionServiceRolePolicy) policy in the IAM console.

## OpenSearchIngestionSelfManagedVpcePolicy
<a name="OpenSearchIngestionSelfManagedVpcePolicy"></a>

You can't attach `OpenSearchIngestionSelfManagedVpcePolicy` to your IAM entities. This policy is attached to a service-linked role that allows OpenSearch Ingestion to enable self-managed VPC access for ingestion pipelines, create tags, and publish ingestion-related CloudWatch metrics to your account. For more information, see [Using service-linked roles for Amazon OpenSearch Service](slr.md).

You can find the [OpenSearchIngestionSelfManagedVpcePolicy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/OpenSearchIngestionSelfManagedVpcePolicy) policy in the IAM console.

## AmazonOpenSearchIngestionFullAccess
<a name="AmazonOpenSearchIngestionFullAccess"></a>

Grants full access to the OpenSearch Ingestion API operations and resources for an AWS account.

You can find the [AmazonOpenSearchIngestionFullAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonOpenSearchIngestionFullAccess) policy in the IAM console.

## AmazonOpenSearchIngestionReadOnlyAccess
<a name="AmazonOpenSearchIngestionReadOnlyAccess"></a>

Grants read-only access to all OpenSearch Ingestion resources for an AWS account.

You can find the [AmazonOpenSearchIngestionReadOnlyAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonOpenSearchIngestionReadOnlyAccess) policy in the IAM console.

## AmazonOpenSearchServerlessServiceRolePolicy
<a name="AmazonOpenSearchServerlessServiceRolePolicy"></a>

Provides the minimum Amazon CloudWatch permissions necessary to send OpenSearch Serverless metric data to CloudWatch.

You can find the [AmazonOpenSearchServerlessServiceRolePolicy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonOpenSearchServerlessServiceRolePolicy) policy in the IAM console.

## OpenSearch Service updates to AWS managed policies
<a name="ac-managed-updates"></a>

View details about updates to AWS managed policies for OpenSearch Service since this service began tracking changes.


| Change | Description | Date | 
| --- | --- | --- | 
| Updated the `AmazonOpenSearchIngestionServiceRolePolicy` | The update gives OpenSearch Ingestion permission to modify VPC endpoints created by OpenSearch in order to share pipelines across VPCs.<br />For the policy JSON, see the [IAM console](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonOpenSearchIngestionServiceRolePolicy). | 28 August 2025 | 
| Updated the `AmazonOpenSearchServiceRolePolicy` | Added the following statement to the policy. When Amazon OpenSearch Service assumes the `AWSServiceRoleForAmazonOpenSearchService` service-linked role, this new statement in the policy enables OpenSearch to update the access scope of any AWS IAM Identity Center application that is only managed by OpenSearch. <pre>{<br />      "Effect": "Allow",<br />      "Action": "sso:PutApplicationAccessScope",<br />      "Resource": "arn:aws:sso::*:application/*/*",<br />      "Condition": {<br />        "StringEquals": {<br />          "aws:ResourceOrgID": "${aws:PrincipalOrgID}"<br />        }<br />      }<br />    }</pre> | 31 March 2025 | 
| Updated `AmazonOpenSearchServerlessServiceRolePolicy` | Added the Sid `AllowAOSSCloudwatchMetrics` to the policy `AmazonOpenSearchServerlessServiceRolePolicy`. A Sid is a statement ID that acts as an optional identifier for the policy statement. | 12 July 2024 | 
| Added `OpenSearchIngestionSelfManagedVpcePolicy` | A new policy that allows OpenSearch Ingestion to enable self-managed VPC access for ingestion pipelines, create tags, and publish ingestion-related CloudWatch metrics to your account.<br />For the policy JSON, see the [IAM console](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonOpenSearchIngestionServiceRolePolicy). | 12 June 2024 | 
| Added`AmazonOpenSearchDirectQueryGlueCreateAccess` | Grants Amazon OpenSearch Service Direct Query Service access to the `CreateDatabase`, `CreatePartition`,`CreateTable`, and `BatchCreatePartition` AWS Glue API. | 6 May 2024 | 
| Updated `AmazonOpenSearchServiceRolePolicy` and `AmazonElasticsearchServiceRolePolicy` | Added the permissions necessary for [the service-linked role](slr-aos.md#slr-permissions) to assign and unassign IPv6 addresses.<br />The deprecated Elasticsearch policy has also been updated to ensure backwards compatibility. | 18 October 2023 | 
| Added `AmazonOpenSearchIngestionServiceRolePolicy` | A new policy that allows OpenSearch Ingestion to enable VPC access for ingestion pipelines, create tags, and publish ingestion-related CloudWatch metrics to your account.<br />For the policy JSON, see the [IAM console](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonOpenSearchIngestionServiceRolePolicy). | 26 April 2023 | 
| Added `AmazonOpenSearchIngestionFullAccess` | A new policy that grants full access to the OpenSearch Ingestion API operations and resources for an AWS account.<br />For the policy JSON, see the [IAM console](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonOpenSearchIngestionFullAccess). | 26 April 2023 | 
| Added `AmazonOpenSearchIngestionReadOnlyAccess` | A new policy that grants read-only access to all OpenSearch Ingestion resources for an AWS account.<br />For the policy JSON, see the [IAM console](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonOpenSearchIngestionReadOnlyAccess). | 26 April 2023 | 
| Added `AmazonOpenSearchServerlessServiceRolePolicy` | A new policy that provides the minimum permissions necessary to send OpenSearch Serverless metric data to Amazon CloudWatch.<br />For the policy JSON, see the [IAM console](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonOpenSearchServerlessServiceRolePolicy). | 29 November 2022 | 
| Updated `AmazonOpenSearchServiceRolePolicy` and `AmazonElasticsearchServiceRolePolicy` | Added the permissions necessary for [the service-linked role](slr-aos.md#slr-permissions) to create [OpenSearch Service-managed VPC endpoints](slr-aos.md#slr-permissions). Some actions can only be performed when the request contains the tag `OpenSearchManaged=true`.<br />The deprecated Elasticsearch policy has also been updated to ensure backwards compatibility. | 7 November 2022 | 
| Updated `AmazonOpenSearchServiceRolePolicy` and `AmazonElasticsearchServiceRolePolicy` | Added support for the `PutMetricData` action, which is required to publish OpenSearch cluster metrics to Amazon CloudWatch.<br />The deprecated Elasticsearch policy has also been updated to ensure backwards compatibility.<br />For the policy JSON, see the [IAM console](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonOpenSearchServiceRolePolicy). | 12 September 2022 | 
| Updated `AmazonOpenSearchServiceRolePolicy` and `AmazonElasticsearchServiceRolePolicy` | Added support for the `acm` resource type. The policy provides the minimum AWS Certificate Manager (ACM) read-only permission necessary for the [service-linked role](slr-aos.md#slr-permissions) to verify and validate ACM resources in order to create and update [custom endpoint](customendpoint.md) enabled domains.<br />The deprecated Elasticsearch policy has also been updated to ensure backwards compatibility. | 28 July 2022 | 
| Updated `AmazonOpenSearchServiceCognitoAccess` and `AmazonESCognitoAccess` | Added support for the `UpdateUserPoolClient` action, which is required to set Cognito user pool configuration during upgrade from Elasticsearch to OpenSearch.<br />Corrected permissions for the `SetIdentityPoolRoles` action to allow access to all resources.<br />The deprecated Elasticsearch policy has also been updated to ensure backwards compatibility. | 20 December 2021 | 
| Updated `AmazonOpenSearchServiceRolePolicy` | Added support for the `security-group` resource type. The policy provides the minimum Amazon EC2 and Elastic Load Balancing permissions necessary for [the service-linked role](slr-aos.md#slr-permissions) to enable [VPC access](cognito-auth.md). | 9 September 2021 | 
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/ac-managed.html)  | This new policy is meant to replace the old policy. Both policies provide full access to the OpenSearch Service configuration API and all HTTP methods for the OpenSearch APIs. [Fine-grained access control](fgac.md) and [resource-based policies](ac.md#ac-types-resource) can still restrict access. | 7 September 2021 | 
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/ac-managed.html)  | This new policy is meant to replace the old policy. Both policies provide read-only access to the OpenSearch Service configuration API (`es:Describe*`, `es:List*`, and `es:Get*`) and *no* access to the HTTP methods for the OpenSearch APIs. | 7 September 2021 | 
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/ac-managed.html)  | This new policy is meant to replace the old policy. Both policies provide the minimum Amazon Cognito permissions necessary to enable [Cognito authentication](cognito-auth.md). | 7 September 2021 | 
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/ac-managed.html)  | This new policy is meant to replace the old policy. Both policies provide the minimum Amazon EC2 and Elastic Load Balancing permissions necessary for [the service-linked role](slr-aos.md#slr-permissions) to enable [VPC access](cognito-auth.md). | 7 September 2021 | 
| Started tracking changes | Amazon OpenSearch Service now tracks changes to AWS-managed policies. | 7 September 2021 | 