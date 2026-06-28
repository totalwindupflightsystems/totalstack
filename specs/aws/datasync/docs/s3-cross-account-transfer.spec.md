---
id: "@specs/aws/datasync/docs/s3-cross-account-transfer"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Transferring from on-premises to S3 across accounts"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Transferring from on-premises to S3 across accounts

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/s3-cross-account-transfer
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Tutorial: Transferring data from on-premises storage to Amazon S3 across AWS accounts
<a name="s3-cross-account-transfer"></a>

When using AWS DataSync with on-premises storage, you typically transfer data to an AWS storage service that belongs to the same AWS account as your DataSync agent. There are situations, however, where you might need to transfer data to an Amazon S3 bucket that's associated with a different account.

**Important**  
Transferring data across AWS accounts by using the methods in this tutorial works only when Amazon S3 is one of the DataSync transfer locations.

## Overview
<a name="s3-cross-account-overview"></a>

It's not uncommon to need to transfer data between different AWS accounts, especially if you have separate teams managing your organization's resources. Here's what a cross-account transfer using DataSync can look like:
+ **Source account**: The AWS account for managing network resources. This is the account that you activate your DataSync agent with.
+ **Destination account**: The AWS account for managing the S3 bucket that you need to transfer data to.

The following diagram illustrates this kind of scenario.

![An example DataSync scenario of data moving from an on-premises storage system through an Direct Connect connection across the internet into AWS. The data is first transferred into one AWS account (your source account), before finally making it into an Amazon S3 bucket in a different AWS account (your destination account).](http://docs.aws.amazon.com/datasync/latest/userguide/images/s3-cross-account-diagram.png)


## Prerequisite: Required source account permissions
<a name="onprem-s3-cross-account-required-permissions-source"></a>

For your source AWS account, there are two sets of permissions to consider with this kind of cross-account transfer:
+ *User permissions* that allow a user to work with DataSync (this might be you or your storage administrator). These permissions let you create DataSync locations and tasks.
+ *DataSync service permissions* that allow DataSync to transfer data to your destination account bucket.

------
#### [ User permissions ]

In your source account, add at least the following permissions to an IAM role for creating your DataSync locations and task. For information on how to add permissions to a role, see [creating](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html) or [modifying](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_modify.html) an IAM role.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "SourceUserRolePermissions",
            "Effect": "Allow",
            "Action": [
                "datasync:CreateLocationS3",
                "datasync:CreateTask",
                "datasync:DescribeLocation*",
                "datasync:DescribeTaskExecution",
                "datasync:ListLocations",
                "datasync:ListTaskExecutions",
                "datasync:DescribeTask",
                "datasync:CancelTaskExecution",
                "datasync:ListTasks",
                "datasync:StartTaskExecution",
                "s3:GetBucketLocation",
                "s3:ListAllMyBuckets"
            ],
            "Resource": "*"
        },
        {
            "Sid": "IAMPermissions",
            "Effect": "Allow",
            "Action": [
                "iam:CreateRole",
                "iam:ListRoles",
                "iam:CreatePolicy"
            ],
            "Resource": "arn:aws:iam::111122223333:role/DataSync-*"
        },
        {
            "Sid": "IAMAttachRolePermissions",
            "Effect": "Allow",
            "Action": [
                "iam:AttachRolePolicy"
            ],
            "Resource": "arn:aws:iam::111122223333:role/DataSync-*",
            "Condition": {
            "ArnLike": {
                "iam:PolicyARN": [
                   "arn:aws:iam::111122223333:policy/DataSync-*",
                   "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess",
                   "arn:aws:iam::aws:policy/service-role/AWSDataSyncFullAccess"
                ]
            }
          }
        },
        {
            "Effect": "Allow",
            "Action": [
                "iam:PassRole"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": [
                        "datasync.amazonaws.com"
                    ]
                }
            }
        }
    ]
}
```

**Tip**  
To set up your *user permissions*, consider using [AWSDataSyncFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-awsdatasyncfullaccess). This is an AWS managed policy that provides a user full access to DataSync and minimal access to its dependencies.

------
#### [ DataSync service permissions ]

The DataSync service needs the following permissions in your source account to transfer data to your destination account bucket.

Later in this tutorial, you add these permissions when [creating an IAM role](#s3-cross-account-create-iam-role-source-account) for DataSync. You also specify this role (`{{source-datasync-role}}`) in your [destination bucket policy](#s3-cross-account-update-s3-policy-destination-account) and when [creating your DataSync destination location](#s3-cross-account-create-datasync-destination).

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
      "Resource": "arn:aws:s3:::{{amzn-s3-demo-destination-bucket}}"
    },
    {
      "Action": [
        "s3:AbortMultipartUpload",
        "s3:DeleteObject",
        "s3:GetObject",
        "s3:ListMultipartUploadParts",
        "s3:PutObject",
        "s3:GetObjectTagging",
        "s3:PutObjectTagging"
      ],
      "Effect": "Allow",
      "Resource": "arn:aws:s3:::{{amzn-s3-demo-destination-bucket}}/*"
    }
  ]
}
```

------

## Prerequisite: Required destination account permissions
<a name="onprem-s3-cross-account-required-permissions-destination"></a>

In your destination account, your *user permissions* must allow you to update your destination bucket's policy and disable its access control lists (ACLs). For more information on these specific permissions, see the [https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html).

## Step 1: In your source account, create a DataSync agent
<a name="s3-cross-account-deploy-agent"></a>

To get started, you must create a DataSync agent that can read from your on-premises storage system and communicate with the DataSync service. This process includes deploying an agent in your on-premises storage environment and activating the agent in your source AWS account.

**Note**  
The steps in this tutorial apply to any type of agent and service endpoint that you use.

**To create a DataSync agent**

1. [Deploy a DataSync agent](deploy-agents.md) in your on-premises storage environment.

1. [Choose a service endpoint](choose-service-endpoint.md) that the agent will use to communicate with AWS.

1. [Activate your agent](activate-agent.md) in your source account.

## Step 2: In your source account, create a DataSync IAM role for destination bucket access
<a name="s3-cross-account-create-iam-role-source-account"></a>

In your source account, you need an IAM role that gives DataSync the permissions to transfer data to your destination account bucket. 

Since you're transferring across accounts, you must create the role manually. (DataSync can create this role for you in the console when transferring in the same account.)

### Create the DataSync IAM role
<a name="s3-cross-account-create-iam-role"></a>

Create an IAM role with DataSync as the trusted entity.

**To create the IAM role**

1. Log in to the AWS Management Console with your source account.

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the left navigation pane, under **Access management**, choose **Roles**, and then choose **Create role**.

1. On the **Select trusted entity** page, for **Trusted entity type**, choose **AWS service**.

1. For **Use case**, choose **DataSync** in the dropdown list and select **DataSync**. Choose **Next**.

1. On the **Add permissions** page, choose **Next**.

1. Give your role a name and choose **Create role**.

For more information, see [Creating a role for an AWS service (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html#roles-creatingrole-service-console) in the *IAM User Guide*.

### Add permissions to the DataSync IAM role
<a name="s3-cross-account-attach-custom-policy"></a>

The IAM role that you just created needs the permissions that allow DataSync to transfer data to the S3 bucket in your destination account.

**To add permissions to your IAM role**

1. On the **Roles** page of the IAM console, search for the role that you just created and choose its name.

1. On the role's details page, choose the **Permissions** tab. Choose **Add permissions** then **Create inline policy**.

1. Choose the **JSON** tab and do the following:

   1. Paste the following JSON into the policy editor:
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
               "Resource": "arn:aws:s3:::amzn-s3-demo-destination-bucket",
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
               "Resource": "arn:aws:s3:::amzn-s3-demo-destination-bucket/*",
               "Condition": {
                   "StringEquals": {
                       "aws:ResourceAccount": "123456789012"
                   }
               }
           }
       ]
      }
      ```

   1. Replace each instance of `{{amzn-s3-demo-destination-bucket}}` with the name of the S3 bucket in your destination account.

1. Choose **Next**. Give your policy a name and choose **Create policy**.

## Step 3: In your destination account, update your S3 bucket policy
<a name="s3-cross-account-update-s3-policy-destination-account"></a>

In your destination account, modify the destination S3 bucket policy to include the [DataSync IAM role](#s3-cross-account-create-iam-role-source-account) that you created in your source account.

**Before you begin**: Make sure that you have the [required permissions for your destination account](#onprem-s3-cross-account-required-permissions-destination).

**To update the destination S3 bucket policy**

1. In the AWS Management Console, switch to your destination account.

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the left navigation pane, choose **Buckets**. 

1. In the **Buckets** list, choose the S3 bucket that you're transferring data to.

1. On the bucket's detail page, choose the **Permissions** tab.

1. Under **Bucket policy**, choose **Edit** and do the following to modify your S3 bucket policy:

   1. Update what's in the editor to include the following policy statements:

      ```
      {
        "Version": "2012-10-17",
        "Statement": [
          {
            "Sid": "DataSyncCreateS3LocationAndTaskAccess",
            "Effect": "Allow",
            "Principal": {
            "AWS": "arn:aws:iam::{{111122223333}}:role/{{source-datasync-role}}"
            },
            "Action": [
              "s3:GetBucketLocation",
              "s3:ListBucket",
              "s3:ListBucketMultipartUploads",
              "s3:AbortMultipartUpload",
              "s3:DeleteObject",
              "s3:GetObject",
              "s3:ListMultipartUploadParts",
              "s3:PutObject",
              "s3:GetObjectTagging",
              "s3:PutObjectTagging"
            ],
            "Resource": [
              "arn:aws:s3:::{{amzn-s3-demo-destination-bucket}}",
              "arn:aws:s3:::{{amzn-s3-demo-destination-bucket}}/*"
            ]
          }
        ]
      }
      ```

   1. Replace each instance of `{{source-account}}` with the AWS account ID for your source account.

   1. Replace `{{source-datasync-role}}` with the [IAM role that you created for DataSync in your source account](#s3-cross-account-create-iam-role-source-account).

   1. Replace each instance of `{{amzn-s3-demo-destination-bucket}}` with the name of the S3 bucket in your destination account.

1. Choose **Save changes**.

## Step 4: In your destination account, disable ACLs for your S3 bucket
<a name="s3-cross-account-disable-acls-destination-account"></a>

It's important that all the data that you copy to the S3 bucket belongs to your destination account. To ensure that this account owns the data, disable the bucket's access control lists (ACLs). For more information, see [Controlling ownership of objects and disabling ACLs for your bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html) in the *Amazon S3 User Guide*.

**To disable ACLs for your destination bucket**

1. While still logged in to the S3 console with your destination account, choose the S3 bucket that you're transferring data to.

1. On the bucket's detail page, choose the **Permissions** tab.

1. Under **Object Ownership**, choose **Edit**.

1. If it isn't already selected, choose the **ACLs disabled (recommended)** option.

1. Choose **Save changes**.

## Step 5: In your source account, create a DataSync source location for your on-premises storage
<a name="s3-on-prem-cross-account-create-source-location"></a>

In your source account, create a [DataSync source location](working-with-locations.md) for the on-premises storage system that you're transferring data from. This location uses the [agent that you activated](#s3-cross-account-deploy-agent) in your source account.

## Step 6: In your source account, create a DataSync destination location for your S3 bucket
<a name="s3-cross-account-create-datasync-destination"></a>

While still in your source account, create a location for the S3 bucket that you're transferring data to.

**Before you begin**: Make sure that you have the [required permissions for your source account](#onprem-s3-cross-account-required-permissions-source).

Since you can't create cross-account locations by using the DataSync console interface, these instructions require that you run a `create-location-s3` command to create your destination location. We recommend running the command by using AWS CloudShell, a browser-based, pre-authenticated shell that you launch directly from the console. CloudShell allows you to run AWS CLI commands like `create-location-s3` without downloading or installing command line tools.

**Note**  
To complete the following steps by using a command line tool other than CloudShell, make sure that your [AWS CLI profile](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-role.html) uses the same IAM role that includes the [required user permissions](#onprem-s3-cross-account-required-permissions-source) to use DataSync in your source account. 

**To create a DataSync destination location by using CloudShell**

1. While still in your source account, do one of the following to launch CloudShell from the console:
   + Choose the CloudShell icon on the console navigation bar. It's located to the right of the search box.
   + Use the search box on the console navigation bar to search for **CloudShell** and then choose the **CloudShell** option.

1. Copy the following command:

   ```
   aws datasync create-location-s3 \
     --s3-bucket-arn arn:aws:s3:::{{amzn-s3-demo-destination-bucket}} \
     --s3-config '{
       "BucketAccessRoleArn":"arn:aws:iam::{{source-user-account}}:role/{{source-datasync-role}}"
     }'
   ```

1. Replace `{{amzn-s3-demo-destination-bucket}}` with the name of the S3 bucket in your destination account.

1. Replace `{{source-user-account}}` with the AWS account ID for your source account.

1. Replace `{{source-datasync-role}}` with the [DataSync IAM role](#s3-cross-account-create-iam-role-source-account) that you created in your source account.

1. Run the command in CloudShell.

   If the command returns a DataSync location ARN similar to this, you successfully created the location:

   ```
   {
     "LocationArn": "arn:aws:datasync:us-east-2:123456789012:location/loc-abcdef01234567890"
   }
   ```

1. In the left navigation pane, expand **Data transfer**, then choose **Locations**.

From your source account, you can see the S3 location that you just created for your destination account bucket.

## Step 7: In your source account, create and start your DataSync task
<a name="s3-cross-account-create-start-datasync-task"></a>

Before starting a DataSync task to transfer your data, let's recap what you've done so far:
+ In your source account, you created your DataSync agent. The agent can read from your on-premises storage system and communicate with the DataSync service.
+ In your source account, you created an IAM role that allows DataSync to transfer data to the S3 bucket in your destination account.
+ In your destination account, you configured your S3 bucket so that DataSync can transfer data to it.
+ In your source account, you created the DataSync source and destination locations for your transfer.

**To create and start the DataSync task**

1. While still using the DataSync console in your source account, expand **Data transfer** in the left navigation pane, then choose **Tasks** and **Create task**.

1. On the **Configure source location** page, choose **Choose an existing location**. Choose the source location that you're copying data from (your on-premises storage) then **Next**.

1. On the **Configure destination location** page, choose **Choose an existing location**. Choose the destination location that you're copying data to (the S3 bucket in your destination account) then **Next**.

1. On the **Configure settings** page, give the task a name. As needed, configure additional settings, such as specifying an Amazon CloudWatch log group. Choose **Next**.

1. On the **Review** page, review your settings and choose **Create task**.

1. On the task's details page, choose **Start**, and then choose one of the following:
   + To run the task without modification, choose **Start with defaults**.
   + To modify the task before running it, choose **Start with overriding options**.

When your task finishes, check the S3 bucket in your destination account. You should see the data that moved from your source location.

## Related resources
<a name="s3-cross-account-create-start-datasync-task"></a>

For more information about what you did in this tutorial, see the following topics:
+ [Creating a role for an AWS service (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html#roles-creatingrole-service-console)
+ [Modifying a role trust policy (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/roles-managingrole-editing-console.html#roles-managingrole_edit-trust-policy)
+ [Adding a bucket policy by using the Amazon S3 console](https://docs.aws.amazon.com/AmazonS3/latest/userguide/add-bucket-policy.html)
+ [Create an S3 location with the AWS CLI](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/create-location-s3.html)