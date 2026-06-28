---
id: "@specs/aws/datasync/docs/security-iam-awsmanpol"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AWS managed policies"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# AWS managed policies

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/security-iam-awsmanpol
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AWS managed policies for AWS DataSync
<a name="security-iam-awsmanpol"></a>





To add permissions to users, groups, and roles, it's easier to use AWS managed policies than to write policies yourself. It takes time and expertise to [create IAM customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) that provide your team with only the permissions they need. To get started quickly, you can use our AWS managed policies. These policies cover common use cases and are available in your AWS account. For more information about AWS managed policies, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

AWS services maintain and update AWS managed policies. You can't change the permissions in AWS managed policies. Services occasionally add additional permissions to an AWS managed policy to support new features. This type of update affects all identities (users, groups, and roles) where the policy is attached. Services are most likely to update an AWS managed policy when a new feature is launched or when new operations become available. Services do not remove permissions from an AWS managed policy, so policy updates won't break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple services. For example, the `ReadOnlyAccess` AWS managed policy provides read-only access to all AWS services and resources. When a service launches a new feature, AWS adds read-only permissions for new operations and resources. For a list and descriptions of job function policies, see [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.









## AWS managed policy: AWSDataSyncReadOnlyAccess
<a name="security-iam-awsmanpol-awsdatasyncreadonlyaccess"></a>

You can attach the `AWSDataSyncReadOnlyAccess` policy to your IAM identities. This policy grants read-only permissions for DataSync.

To view the permissions for this policy, see [https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSDataSyncReadOnlyAccess.html](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSDataSyncReadOnlyAccess.html) in the *AWS Managed Policy Reference* .

## AWS managed policy: AWSDataSyncFullAccess
<a name="security-iam-awsmanpol-awsdatasyncfullaccess"></a>

You can attach the `AWSDataSyncFullAccess` policy to your IAM identities. This policy grants administrative permissions for DataSync and is required for AWS Management Console access to the service. `AWSDataSyncFullAccess` provides full access to DataSync API operations and the operations that interact with related resources (such as Amazon S3 buckets, Amazon EFS file systems, AWS KMS keys, and Secrets Manager secrets). The policy also grants permissions for Amazon CloudWatch, including creating log groups and creating or updating a resource policy.

To view the permissions for this policy, see [https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSDataSyncFullAccess.html](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSDataSyncFullAccess.html) in the *AWS Managed Policy Reference* .

## AWS managed policy: AWSDataSyncServiceRolePolicy
<a name="security-iam-awsmanpol-awsdatasyncservicerolepolicy"></a>

You can't attach the `AWSDataSyncServiceRolePolicy` policy to your IAM identities. This policy is attached to a service-linked role that allows DataSync to perform actions on your behalf. For more information, see [Using service-linked roles for DataSync](using-service-linked-roles.md).

This policy grants administrative permissions that allow the service-linked role to create Amazon CloudWatch logs for DataSync tasks using Enhanced mode.

## Policy updates
<a name="security-iam-awsmanpol-updates"></a>


| Change | Description | Date | 
| --- | --- | --- | 
| [AWSDataSyncFullAccess](#security-iam-awsmanpol-awsdatasyncfullaccess) – Change | DataSync modified permission statements for `AWSDataSyncFullAccess`:<br />The updated statements remove tagging conditions from the permissions DataSync uses to create Secrets Manager secrets. | May 13, 2025 | 
| [AWSDataSyncFullAccess](#security-iam-awsmanpol-awsdatasyncfullaccess) – Change | DataSync added new permissions to `AWSDataSyncFullAccess`: [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/security-iam-awsmanpol.html)<br />These permissions let DataSync create, edit, and delete AWS Secrets Manager secrets. | May 7, 2025 | 
| [AWSDataSyncFullAccess](#security-iam-awsmanpol-awsdatasyncfullaccess) – Change | DataSync added new permissions to `AWSDataSyncFullAccess`: [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/security-iam-awsmanpol.html)<br />These permissions let DataSync retrieve metadata about your AWS Secrets Manager secrets and AWS KMS keys, including any aliases associated with your keys. | April 23, 2025 | 
| [AWSDataSyncServiceRolePolicy](#security-iam-awsmanpol-awsdatasyncservicerolepolicy) – Change | DataSync added new permissions to the `AWSDataSyncServiceRolePolicy` policy that's used by the DataSync service-linked role `AWSServiceRoleForDataSync`:[See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/security-iam-awsmanpol.html)<br />These permissions let DataSync read metadata and values for secrets managed by AWS Secrets Manager. | April 15, 2025 | 
| [AWSDataSyncServiceRolePolicy](#security-iam-awsmanpol-awsdatasyncservicerolepolicy) – New policy | DataSync added a policy that's used by the DataSync service-linked role `AWSServiceRoleForDataSync`. This new managed policy automatically creates Amazon CloudWatch logs for your DataSync tasks that use Enhanced mode. | October 30, 2024 | 
| [AWSDataSyncFullAccess](#security-iam-awsmanpol-awsdatasyncfullaccess) – Change | DataSync added new a permission to `AWSDataSyncFullAccess`: [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/security-iam-awsmanpol.html)<br />This permission lets DataSync create service-linked roles for you. | October 30, 2024 | 
| [AWSDataSyncFullAccess](#security-iam-awsmanpol-awsdatasyncfullaccess) – Change | DataSync added new a permission to `AWSDataSyncFullAccess`: [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/security-iam-awsmanpol.html)<br />This permission lets you choose opt-in Regions when creating a DataSync task for transfers between AWS Regions. | July 22, 2024 | 
| [AWSDataSyncFullAccess](#security-iam-awsmanpol-awsdatasyncfullaccess) – Change | DataSync added new a permission to `AWSDataSyncFullAccess`: [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/security-iam-awsmanpol.html)<br />This permission lets you choose a specific version of your [DataSync manifest](transferring-with-manifest.md). | February 16, 2024 | 
| [AWSDataSyncFullAccess](#security-iam-awsmanpol-awsdatasyncfullaccess) – Change | DataSync added new permissions to `AWSDataSyncFullAccess`: [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/security-iam-awsmanpol.html)<br />These permissions help you create DataSync agents and locations for Amazon EFS, Amazon FSx for NetApp ONTAP, Amazon S3, and S3 on Outposts. | May 2, 2023 | 
| DataSync started tracking changes | DataSync started tracking changes for its AWS managed policies. | March 1, 2021 | 