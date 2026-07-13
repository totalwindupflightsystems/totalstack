---
id: "@specs/aws/lambda/docs/configuration-filesystem-s3files"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Amazon S3 Files"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Amazon S3 Files

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/configuration-filesystem-s3files
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Configuring Amazon S3 Files access
<a name="configuration-filesystem-s3files"></a>

Amazon S3 Files delivers a shared file system that connects any AWS compute resource directly with your data in Amazon S3. Amazon S3 Files provides access to your Amazon S3 objects as files using standard file system operations such as read and write on the local mount path. Learn more about [Amazon S3 Files](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-files.html).

**Topics**
+ [Prerequisites and setup](#configuration-filesystem-s3files-setup)
+ [Execution role and user permissions](#configuration-filesystem-s3files-permissions)
+ [Connecting to a file system (console)](#configuration-filesystem-s3files-config)

## Prerequisites and setup
<a name="configuration-filesystem-s3files-setup"></a>

Before you set up Amazon S3 Files with your Lambda function, make sure you have the following:
+ An Amazon S3 file system and mount targets in available state in the same account and AWS Region as your Lambda function.
+ A Lambda function in the same VPC as the mount target. You must have a mount target in each subnet where your function is deployed.
+ Security groups that allow NFS traffic (port 2049) between your Lambda function and the mount targets. [Learn more about configuring security groups](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-files-prereq-policies.html#s3-files-prereq-security-groups).

For more information, see the following topics in the *Amazon S3 User Guide*:
+ [Getting started with Amazon S3 Files](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-files-getting-started.html)
+ [Amazon S3 Files prerequisites](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-files-prereq-policies.html)
+ [Amazon S3 Files best practices](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-files-best-practices.html)

## Execution role and user permissions
<a name="configuration-filesystem-s3files-permissions"></a>

Your function's execution role must have the following permissions to access an Amazon S3 Files file system:

**Execution role permissions**
+ **s3files:ClientMount** – Required to mount the file system.
+ **s3files:ClientWrite** – Required for read-write access. Not needed for read-only connections.

These permissions are included in the [AmazonS3FilesClientReadWriteAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonS3FilesClientReadWriteAccess.html) managed policy. Additionally, your execution role must have the [permissions required to connect to the file system's VPC](configuration-vpc.md#configuration-vpc-permissions).

**Note**  
Amazon S3 Files optimizes throughput by reading directly from Amazon S3. Direct reads from Amazon S3 are supported only for functions configured with 512 MB or more of memory.

Your function also needs the following permissions to read directly from Amazon S3:
+ **s3:GetObject**
+ **s3:GetObjectVersion**

For more information about required permissions, see [IAM permissions for Amazon S3 Files](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-files-prereq-policies.html#s3-files-prereq-iam) in the *Amazon S3 User Guide*.

When you configure a file system in the console, Lambda uses your permissions to verify mount targets and access points. To configure a function to connect to a file system, your user needs the following permissions:

**User permissions**
+ **s3files:ListFileSystems**
+ **s3files:ListAccessPoints**
+ **s3files:GetFileSystem**
+ **s3files:GetAccessPoint**
+ **s3files:CreateAccessPoint** – Needed if attaching the file system to the function from the console.

The following example policy grants your function's execution role permissions to mount an Amazon S3 file system with read-write access and read directly from Amazon S3.

```
{
    "Version": "2012-10-17", 		 	 	 
    "Statement": [
        {
            "Sid": "S3FilesLambdaAccess",
            "Effect": "Allow",
            "Action": [
                "s3files:ClientMount",
                "s3files:ClientWrite"
            ],
            "Resource": "*"
        },
        {
            "Sid": "S3DirectRead",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:GetObjectVersion"
            ],
            "Resource": "arn:aws:s3:::{{bucket-name}}/*"
        },
        {
            "Sid": "S3FilesConsoleSetup",
            "Effect": "Allow",
            "Action": [
                "s3files:ListFileSystems",
                "s3files:ListAccessPoints",
                "s3files:GetFileSystem",
                "s3files:GetAccessPoint",
                "s3files:CreateAccessPoint"
            ],
            "Resource": "*"
        }
    ]
}
```

## Connecting to a file system (console)
<a name="configuration-filesystem-s3files-config"></a>

A function connects to a file system over the local network in a VPC. The subnets that your function connects to can be the same subnets that contain mount points for your file system, or subnets in the same Availability Zone that can route NFS traffic (port 2049) to the file system.

**Note**  
If your function is not already connected to a VPC, see [Giving Lambda functions access to resources in an Amazon VPC](configuration-vpc.md).

**To configure S3 Files access**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Choose a function.

1. Choose **Configuration**, then choose **File systems**.

1. Choose **Add file system** (or **Edit** to modify an existing configuration).

1. Select **S3 Files**.

1. Configure the following properties:
   + **S3 file system** – Choose a file system from the dropdown.
   + **Access point** (optional) – Choose an access point. If the file system has no access points, Lambda automatically creates one when you save (UID/GID 1000:1000, root directory `/lambda`, permissions 755). If access points exist, you must select one.
   + **Local mount path** – The location where the file system is mounted on the Lambda function, starting with `/mnt/`.

1. Choose **Save**.

Your file system will be attached the next time you invoke your Lambda function.