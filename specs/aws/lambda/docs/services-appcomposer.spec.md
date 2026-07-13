---
id: "@specs/aws/lambda/docs/services-appcomposer"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Infrastructure Composer"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Infrastructure Composer

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/services-appcomposer
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Using AWS Lambda with AWS Infrastructure Composer
<a name="services-appcomposer"></a>

AWS Infrastructure Composer is a visual builder for desiging modern applications on AWS. You design your application architecture by dragging, grouping, and connecting AWS services in a visual canvas. Infrastructure Composer creates infrastructure as code (IaC) templates from your design that you can deploy using [AWS SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) or [CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

## Exporting a Lambda function to Infrastructure Composer
<a name="services-appcomposer-export"></a>

You can get started using Infrastructure Composer by creating a new project based on the configuration of an existing Lambda function using the Lambda console. To export your function's configuration and code to Infrastructure Composer to create a new project, do the following:

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Select the function you want to use as a basis for your Infrastructure Composer project.

1. In the **Function overview** pane, choose **Export to Infrastructure Composer**.

   To export your function's configuration and code to Infrastructure Composer, Lambda creates an Amazon S3 bucket in your account to temporarily store this data.

1. In the dialog box, choose **Confirm and create project** to accept the default name for this bucket and export your function's configuration and code to Infrastructure Composer.

1. (Optional) To choose another name for the Amazon S3 bucket that Lambda creates, enter a new name and choose **Confirm and create project**. Amazon S3 bucket names must be globally unique and follow the [bucket naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html).

1. To save your project and function files in Infrastructure Composer, activate [local sync mode](https://docs.aws.amazon.com/application-composer/latest/dg/reference-features-local-sync.html).

**Note**  
If you've used the **Export to Application Composer** feature before and created an Amazon S3 bucket using the default name, Lambda can re-use this bucket if it still exists. Accept the default bucket name in the dialog box to re-use the existing bucket.

### Amazon S3 transfer bucket configuration
<a name="services-appcomposer-bucket-info"></a>

The Amazon S3 bucket that Lambda creates to transfer your function's configuration automatically encrypts objects using the AES 256 encryption standard. Lambda also configures the bucket to use the [bucket owner condition](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-owner-condition.html) to ensure that only your AWS account is able to add objects to the bucket.

Lambda configures the bucket to automatically delete objects 10 days after they are uploaded. However, Lambda doesn't automaticaly delete the bucket itself. To delete the bucket from your AWS account, follow the instructions in [Deleting a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/delete-bucket.html). The default bucket name uses the prefix `lambdasam`, a 10-digit alphanumeric string, and the AWS Region you created your function in:

```
lambdasam-{{06f22da95b}}-{{us-east-1}}
```

To avoid additional charges being added to your AWS account, we recommend that you delete the Amazon S3 bucket as soon as you have finished exporting your function to Infrastructure Composer.

Standard [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/) applies.

### Required permissions
<a name="services-appcomposer-permissions"></a>

To use the Lambda integration with Infrastructure Composer feature, you need certain permissions to download an AWS SAM template and to write your function's configuration to Amazon S3.

To download an AWS SAM template, you must have permission to use the following API actions:
+ [GetPolicy](https://docs.aws.amazon.com/lambda/latest/api/API_GetPolicy.html)
+ [iam:GetPolicyVersion](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetPolicyVersion.html)
+ [iam:GetRole](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetRole.html)
+ [iam:GetRolePolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetRolePolicy.html)
+ [iam:ListAttachedRolePolicies](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListAttachedRolePolicies.html)
+ [iam:ListRolePolicies](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListRolePolicies.html)
+ [iam:ListRoles](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListRoles.html)

You can grant permission to use all of these actions by adding the [https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSLambda_ReadOnlyAccess.html](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSLambda_ReadOnlyAccess.html) AWS managed policy to your IAM user role.

For Lambda to write your function's configuration to Amazon S3, you must have permission to use the following API actions:
+ [S3:PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html)
+ [S3:CreateBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html)
+ [S3:PutBucketEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketEncryption.html)
+ [S3:PutBucketLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLifecycleConfiguration.html)

If you are unable to export your function's configuration to Infrastructure Composer, check that your account has the required permissions for these operations. If you have the required permissions, but still cannot export your function's configuration, check for any [resource-based policies](access-control-resource-based.md) that might limit access to Amazon S3.

## Other resources
<a name="w2aac15c43c33b7"></a>

For a more detailed tutorial on how to design a serverless application in Infrastructure Composer based on an existing Lambda function, see [Using Lambda with infrastructure as code (IaC)](foundation-iac.md).

To use Infrastructure Composer and AWS SAM to design and deploy a complete serverless application using Lambda, you can also follow the [AWS Infrastructure Composer tutorial](https://catalog.workshops.aws/serverless-patterns/en-US/dive-deeper/module1a) in the [AWS Serverless Patterns Workshop](https://catalog.workshops.aws/serverless-patterns/en-US).