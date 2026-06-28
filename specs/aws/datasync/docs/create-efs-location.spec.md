---
id: "@specs/aws/datasync/docs/create-efs-location"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Configuring transfers with Amazon EFS"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Configuring transfers with Amazon EFS

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/create-efs-location
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Configuring AWS DataSync transfers with Amazon EFS
<a name="create-efs-location"></a>

To transfer data to or from your Amazon EFS file system, you must create an AWS DataSync transfer *location*. DataSync can use this location as a source or destination for transferring data.

## Providing DataSync access to Amazon EFS file systems
<a name="create-efs-location-access"></a>

[Creating a location](#create-efs-location-how-to) involves understanding how DataSync can access your storage. For Amazon EFS, DataSync mounts your file system as a root user from your virtual private cloud (VPC) using [network interfaces](required-network-interfaces.md).

**Contents**
+ [Determining the subnet and security groups for your mount target](#create-efs-location-mount-target)
+ [Accessing restricted file systems](#create-efs-location-iam)
  + [Creating a DataSync IAM role for file system access](#create-efs-location-iam-role)
  + [Example file system policy allowing DataSync access](#create-efs-location-iam-policy)

### Determining the subnet and security groups for your mount target
<a name="create-efs-location-mount-target"></a>

When creating your location, you specify the subnet and security groups that allow DataSync to connect to one of your Amazon EFS file system's [mount targets](https://docs.aws.amazon.com/efs/latest/ug/accessing-fs.html).

The subnet that you specify must be located:
+ In the same VPC as your file system.
+ In the same Availability Zone as at least one mount target for your file system.

**Note**  
You don't need to specify a subnet that includes a file system mount target.

The security groups that you specify must allow inbound traffic on Network File System (NFS) port 2049. For information on creating and updating security groups for your mount targets, see the [https://docs.aws.amazon.com/efs/latest/ug/network-access.html](https://docs.aws.amazon.com/efs/latest/ug/network-access.html).

**Specifying security groups associated with a mount target**  
You can specify a security group that's associated with one of your file system's mount targets. We recommend this approach from a network management standpoint.

**Specifying security groups that aren't associated with a mount target**  
You also can specify a security group that isn't associated with one of your file system's mount targets. However, this security group must be able to communicate with a mount target's security group.  
For example, here's how you might create a relationship between security group D (for DataSync) and security group M (for the mount target):  
+ Security group D, which you specify when creating your location, must have a rule that allows outbound connections on NFS port 2049 to security group M.
+ Security group M, which you associate with the mount target, must allow inbound access on NFS port 2049 from security group D.

**To find a mount target's security group**

The following instructions can help you identify the security group of an Amazon EFS file system mount target that you want DataSync to use for your transfer.

1. In the AWS CLI, run the following `describe-mount-targets` command.

   ```
   aws efs describe-mount-targets \
       --region {{file-system-region }} \
       --file-system-id {{file-system-id}}
   ```

   This command returns information about your file system's mount targets (similar to the following example output).

   ```
   {
       "MountTargets": [
           {
               "OwnerId": "111222333444",
               "MountTargetId": "fsmt-22334a10",
               "FileSystemId": "fs-123456ab",
               "SubnetId": "subnet-f12a0e34",
               "LifeCycleState": "available",
               "IpAddress": "11.222.0.123",
               "NetworkInterfaceId": "eni-1234a044"
           }
       ]
   }
   ```

1. Take note of the `MountTargetId` value that you want to use.

1. Run the following `describe-mount-target-security-groups` command using the `MountTargetId` to see the security group of your mount target.

   ```
   aws efs describe-mount-target-security-groups \
       --region {{file-system-region}} \
       --mount-target-id {{mount-target-id}}
   ```

You specify this security group when [creating your location](#create-efs-location-how-to).

### Accessing restricted file systems
<a name="create-efs-location-iam"></a>

DataSync can transfer to or from Amazon EFS file systems that restrict access through [access points](https://docs.aws.amazon.com/efs/latest/ug/efs-access-points.html) and [IAM policies](https://docs.aws.amazon.com/efs/latest/ug/iam-access-control-nfs-efs.html).

**Note**  
If DataSync accesses a destination file system through an access point that [enforces user identity](https://docs.aws.amazon.com/efs/latest/ug/efs-access-points.html#enforce-identity-access-points), the POSIX user and group IDs for your source data aren't preserved if you configure your DataSync task to [copy ownership](configure-metadata.md). Instead, the transferred files and folders are set to the access point's user and group IDs. When this happens, task verification fails because DataSync detects a mismatch between metadata in the source and destination locations.

**Contents**
+ [Creating a DataSync IAM role for file system access](#create-efs-location-iam-role)
+ [Example file system policy allowing DataSync access](#create-efs-location-iam-policy)

#### Creating a DataSync IAM role for file system access
<a name="create-efs-location-iam-role"></a>

If you have an Amazon EFS file system that restricts access through an IAM policy, you can create an IAM role that provides DataSync permission to read from or write data to the file system. You then might need to specify that role in your [file system policy](#create-efs-location-iam-policy).

**To create the DataSync IAM role**

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the left navigation pane, under **Access management**, choose **Roles**, and then choose **Create role**.

1. On the **Select trusted entity** page, for **Trusted entity type**, choose **Custom trust policy**.

1. Paste the following JSON into the policy editor:

   ```
   {
       "Version": "2012-10-17",
       "Statement": [{
           "Effect": "Allow",
           "Principal": {
               "Service": "datasync.amazonaws.com"
           },
           "Action": "sts:AssumeRole"
       }]
   }
   ```

1. Choose **Next**. On the **Add permissions** page, choose **Next**.

1. Give your role a name and choose **Create role**.

You specify this role when [creating your location](#create-efs-location-how-to).

#### Example file system policy allowing DataSync access
<a name="create-efs-location-iam-policy"></a>

The following example file system policy shows how access to an Amazon EFS file system (identified in the policy as `fs-{{1234567890abcdef0}}`) is restricted but still allows access to DataSync through an IAM role named `{{MyDataSyncRole}}`:

```
{
    "Version": "2012-10-17",
    "Id": "ExampleEFSFileSystemPolicy",
    "Statement": [{
        "Sid": "AccessEFSFileSystem",
        "Effect": "Allow",
        "Principal": {
            "AWS": "arn:aws:iam::{{111122223333}}:role/{{MyDataSyncRole}}"
        },
        "Action": [
            "elasticfilesystem:ClientMount",
            "elasticfilesystem:ClientWrite",
            "elasticfilesystem:ClientRootAccess"
        ],
        "Resource": "arn:aws:elasticfilesystem:{{us-east-1}}:{{111122223333}}:file-system/fs-{{1234567890abcdef0}}",
        "Condition": {
            "Bool": {
                "aws:SecureTransport": "true"
            },
            "StringEquals": {
                "elasticfilesystem:AccessPointArn": "arn:aws:elasticfilesystem:{{us-east-1}}:{{111122223333}}:access-point/fsap-{{abcdef01234567890}}"
            }
        }
    }]
}
```
+ `Principal` – Specifies an [IAM role](#create-efs-location-iam) that gives DataSync permission to access the file system.
+ `Action` – Gives DataSync root access and allows it to read from and write to the file system.
+ `aws:SecureTransport` – Requires NFS clients to use TLS when connecting to the file system.
+ `elasticfilesystem:AccessPointArn` – Allows access to the file system only through a specific access point.

## Network considerations with Amazon EFS transfers
<a name="efs-network-considerations"></a>

VPCs that you use with DataSync must have default tenancy. VPCs with dedicated tenancy aren't supported.

## Performance considerations with Amazon EFS transfers
<a name="efs-considerations"></a>

Your Amazon EFS file system's throughput mode can affect transfer duration and file system performance during the transfer. Consider the following:
+ For best results, we recommend using Elastic throughput mode. If you don't use Elastic throughput mode, your transfer might take longer.
+ If you use Bursting throughput mode, the performance of your file system's applications might be affected because DataSync consumes file system burst credits.
+ How you [configure DataSync to verify your transferred data](configure-data-verification-options.md) can affect file system performance and data access costs.

For more information, see [Amazon EFS performance](https://docs.aws.amazon.com/efs/latest/ug/performance.html) in the *Amazon Elastic File System User Guide* and the [Amazon EFS Pricing](https://aws.amazon.com/efs/pricing/) page.

## Creating your Amazon EFS transfer location
<a name="create-efs-location-how-to"></a>

To create the transfer location, you need an existing Amazon EFS file system. If you don't have one, see [Getting started with Amazon EFS](https://docs.aws.amazon.com/efs/latest/ug/getting-started.html) in the *Amazon Elastic File System User Guide*.

### Using the DataSync console
<a name="create-efs-location-how-to-console"></a>

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/).

1. In the left navigation pane, expand **Data transfer**, then choose **Locations** and **Create location**.

1. For ** Location type**, choose **Amazon EFS file system**.

   You configure this location as a source or destination later. 

1. For **File system**, choose the Amazon EFS file system that you want to use as a location.

1. For **Mount path**, enter a mount path for your Amazon EFS file system.

   This specifies where DataSync reads or writes data (depending on if this is a source or destination location) on your file system.

   By default, DataSync uses the root directory (or [access point](https://docs.aws.amazon.com/efs/latest/ug/efs-access-points.html) if you provide one for the **EFS access point** setting). You can also specify subdirectories using forward slashes (for example, `/path/to/directory`).

1. For **Subnet** choose a subnet where you want DataSync to create the [network interfaces](required-network-interfaces.md) for managing your data transfer traffic.

   The subnet must be located:
   + In the same VPC as your file system.
   + In the same Availability Zone as at least one file system mount target.
**Note**  
You don't need to specify a subnet that includes a file system mount target.

1. For **Security groups**, choose the security group associated with your Amazon EFS file system's mount target. You can choose more than one security group.
**Note**  
The security groups that you specify must allow inbound traffic on NFS port 2049. For more information, see [Determining the subnet and security groups for your mount target](#create-efs-location-mount-target).

1. For **In-transit encryption**, choose whether you want DataSync to use Transport Layer Security (TLS) encryption when it transfers data to or from your file system.
**Note**  
You must enable this setting to configure an access point, IAM role, or both with your Amazon EFS location.

1. (Optional) For **EFS access point**, choose an access point that DataSync can use to mount your file system.

   For more information, see [Accessing restricted file systems](#create-efs-location-iam).

1. (Optional) For **IAM role**, specify a role that allows DataSync to access your file system.

   For information on creating this role, see [Creating a DataSync IAM role for file system access](#create-efs-location-iam-role).

1. (Optional) Select **Add tag** to tag your file system.

   A *tag* is a key-value pair that helps you manage, filter, and search for your locations. 

1. Choose **Create location**.

### Using the AWS CLI
<a name="create-location-efs-cli"></a>

1. Copy the following `create-location-efs` command:

   ```
   aws datasync create-location-efs \
       --efs-filesystem-arn 'arn:aws:elasticfilesystem:{{region}}:{{account-id}}:file-system/{{file-system-id}}' \
       --subdirectory {{/path/to/your/subdirectory}} \
       --ec2-config SecurityGroupArns='arn:aws:ec2:{{region}}:{{account-id}}:security-group/{{security-group-id}}',SubnetArn='arn:aws:ec2:{{region}}:{{account-id}}:subnet/{{subnet-id}}' \
       --in-transit-encryption TLS1_2 \
       --access-point-arn 'arn:aws:elasticfilesystem:{{region}}:{{account-id}}:access-point/{{access-point-id}}' \
       --file-system-access-role-arn 'arn:aws:iam::{{account-id}}:role/{{datasync-efs-access-role}}
   ```

1. For `--efs-filesystem-arn`, specify the Amazon Resource Name (ARN) of the Amazon EFS file system that you're transferring to or from.

1. For `--subdirectory`, specify a mount path for your file system.

   This is where DataSync reads or writes data (depending on if this is a source or destination location) on your file system. 

   By default, DataSync uses the root directory (or [access point](https://docs.aws.amazon.com/efs/latest/ug/efs-access-points.html) if you provide one with `--access-point-arn`). You can also specify subdirectories using forward slashes (for example, `/path/to/directory`).

1. For `--ec2-config`, do the following:
   + For `SecurityGroupArns`, specify the ARN of the security group associated with your file system's mount target. You can specify more than one security group.
**Note**  
The security groups that you specify must allow inbound traffic on NFS port 2049. For more information, see [Determining the subnet and security groups for your mount target](#create-efs-location-mount-target).
   + For `SubnetArn`, specify the ARN of the subnet where you want DataSync to create the [network interfaces](required-network-interfaces.md) for managing your data transfer traffic.

     The subnet must be located:
     + In the same VPC as your file system.
     + In the same Availability Zone as at least one file system mount target.
**Note**  
You don't need to specify a subnet that includes a file system mount target.

1. For `--in-transit-encryption`, specify whether you want DataSync to use Transport Layer Security (TLS) encryption when it transfers data to or from your file system.
**Note**  
You must set this to `TLS1_2` to configure an access point, IAM role, or both with your Amazon EFS location.

1. (Optional) For `--access-point-arn`, specify the ARN of an access point that DataSync can use to mount your file system.

   For more information, see [Accessing restricted file systems](#create-efs-location-iam).

1. (Optional) For `--file-system-access-role-arn`, specify the ARN of an IAM role that allows DataSync to access your file system.

   For information on creating this role, see [Creating a DataSync IAM role for file system access](#create-efs-location-iam-role).

1. Run the `create-location-efs` command.

   If the command is successful, you get a response that shows you the ARN of the location that you created. For example:

   ```
   {
       "LocationArn": "arn:aws:datasync:us-east-1:111222333444:location/loc-0b3017fc4ba4a2d8d"
   }
   ```