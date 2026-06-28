---
id: "@specs/aws/datasync/docs/using-identity-based-policies"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Customer managed policies"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Customer managed policies

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/using-identity-based-policies
> **target_lang:** meta — documentation tier. ALL sections preserved.



# IAM customer managed policies for AWS DataSync
<a name="using-identity-based-policies"></a>

In addition to AWS managed policies, you also can create your own identity-based policies for AWS DataSync and attach them to the AWS Identity and Access Management (IAM) identities that require those permissions. These are known as *customer managed policies*, which are standalone policies that you administer in your own AWS account.

**Important**  
Before you begin, we recommend that you learn about the basic concepts and options for managing access to your DataSync resources. For more information, see [Access management for AWS DataSync](managing-access-overview.md). 

When creating a customer managed policy, you include statements about DataSync operations that can be used on certain AWS resources. The following example policy has two statements (note the `Action` and `Resource` elements in each statement):

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowsSpecifiedActionsOnAllTasks",
            "Effect": "Allow",
            "Action": "datasync:DescribeTask",
            "Resource": "arn:aws:datasync:{{us-east-1}}:{{111122223333}}:task/*"
        },  
        {
            "Sid": "ListAllTasks",
            "Effect": "Allow",
            "Action": "datasync:ListTasks",
            "Resource": "*"
        }
    ]    
}
```

The policy's statements do the following:
+ The first statement grants permissions to perform the `datasync:DescribeTask` action on certain transfer task resources by specifying an Amazon Resource Name (ARN) with a wildcard character (`*`). 
+ The second statement grants permissions to perform the `datasync:ListTasks` action on all tasks by specifying just a wildcard character (`*`) .

## Examples of customer managed policies
<a name="customer-managed-policies"></a>

The following example customer managed policies grant permissions for various DataSync operations. The policies work if you're using the AWS Command Line Interface (AWS CLI) or an AWS SDK. To use these policies in the console, you must also use the managed policy `AWSDataSyncFullAccess`.

**Topics**
+ [Example 1: Create a trust relationship that allows DataSync to access your Amazon S3 bucket](#datasync-example1)
+ [Example 2: Allow DataSync to read and write to your Amazon S3 bucket](#datasync-example2)
+ [Example 3: Allow DataSync to upload logs to CloudWatch log groups](#datasync-example4)

### Example 1: Create a trust relationship that allows DataSync to access your Amazon S3 bucket
<a name="datasync-example1"></a>

The following is an example of a trust policy that allows DataSync to assume an IAM role. This role allows DataSync to access an Amazon S3 bucket. To prevent the [cross-service confused deputy problem](cross-service-confused-deputy-prevention.md), we recommend using the [https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourcearn](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourcearn) and [https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourceaccount](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourceaccount) global condition context keys in the policy.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "datasync.amazonaws.com"
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "StringEquals": {
                "aws:SourceAccount": "{{111111111111}}"
                },
                "ArnLike": {
                "aws:SourceArn": "arn:aws:datasync:{{us-east-1}}:{{111111111111}}:*"
                }
            }
        }
    ]
}
```

### Example 2: Allow DataSync to read and write to your Amazon S3 bucket
<a name="datasync-example2"></a>

The following example policy grants DataSync the minimum permissions to read and write data to an S3 bucket that's used as a destination location.

**Note**  
The value for `aws:ResourceAccount` should be the account ID that owns the Amazon S3 bucket specified in the policy.

```
{
 "Version": "2012-10-17",		 	 	 
 "Statement": [
     {
         "Action": [
             "s3:GetBucketLocation",
             "s3:ListBucket",
             "s3:ListBucketMultipartUploads"
         ],
         "Effect": "Allow",
         "Resource": "arn:aws:s3:::amzn-s3-demo-bucket",
         "Condition": {
             "StringEquals": {
                 "aws:ResourceAccount": "123456789012"
             }
         }
     },
     {
         "Action": [
             "s3:AbortMultipartUpload",
             "s3:DeleteObject",
             "s3:GetObject",
             "s3:GetObjectTagging",
             "s3:GetObjectVersion",
             "s3:GetObjectVersionTagging",
             "s3:ListMultipartUploadParts",
             "s3:PutObject",
             "s3:PutObjectTagging"
           ],
         "Effect": "Allow",
         "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/*",
         "Condition": {
             "StringEquals": {
                 "aws:ResourceAccount": "123456789012"
             }
         }
     }
 ]
}
```

### Example 3: Allow DataSync to upload logs to CloudWatch log groups
<a name="datasync-example4"></a>

DataSync requires permissions to be able to upload logs to your Amazon CloudWatch log groups. You can use CloudWatch log groups to monitor and debug your tasks.

For an example of an IAM policy that grants such permissions, see [Allowing DataSync to upload logs to a CloudWatch log group](configure-logging.md#cloudwatchlogs).