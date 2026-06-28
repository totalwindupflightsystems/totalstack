---
id: "@specs/aws/datasync/docs/create-fsx-location"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Configuring transfers with FSx for Windows File Server"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Configuring transfers with FSx for Windows File Server

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/create-fsx-location
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Configuring transfers with FSx for Windows File Server
<a name="create-fsx-location"></a>

To transfer data to or from your Amazon FSx for Windows File Server file system, you must create an AWS DataSync transfer *location*. DataSync can use this location as a source or destination for transferring data.

## Providing DataSync access to FSx for Windows File Server file systems
<a name="create-fsx-location-access"></a>

DataSync connects to your FSx for Windows File Server file system with the Server Message Block (SMB) protocol and mounts it from your virtual private cloud (VPC) using [network interfaces](required-network-interfaces.md).

**Note**  
VPCs that you use with DataSync must have default tenancy. VPCs with dedicated tenancy aren't supported.

**Topics**
+ [Required permissions](#create-fsx-windows-location-permissions)
+ [Required authentication protocols](#configuring-fsx-windows-authentication-protocols)
+ [DFS Namespaces](#configuring-fsx-windows-location-dfs)

### Required permissions
<a name="create-fsx-windows-location-permissions"></a>

You must provide DataSync a user with the necessary rights to mount and access your FSx for Windows File Server files, folders, and file metadata.

We recommend that this user belong to a Microsoft Active Directory group for administering your file system. The specifics of this group depends on your Active Directory setup:
+ If you're using AWS Directory Service for Microsoft Active Directory with FSx for Windows File Server, the user must be a member of the **AWS Delegated FSx Administrators** group.
+ If you're using self-managed Active Directory with FSx for Windows File Server, the user must be a member of one of two groups:
  + The **Domain Admins** group, which is the default delegated administrators group.
  + A custom delegated administrators group with user rights that allow DataSync to copy object ownership permissions and Windows access control lists (ACLs).
**Important**  
You can't change the delegated administrators group after the file system has been deployed. You must either redeploy the file system or restore it from a backup to use the custom delegated administrator group with the following user rights that DataSync needs to copy metadata.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/create-fsx-location.html)
+ If you want to copy Windows ACLs and are transferring between an SMB file server and FSx for Windows File Server file system or between FSx for Windows File Server file systems, the users that you provide DataSync must belong to the same Active Directory domain or have an Active Directory trust relationship between their domains.

**Warning**  
Your FSx for Windows File Server file system's SYSTEM user must have **Full control** permissions on all folders in your file system. Do not change the NTFS ACL permissions for this user on your folders. If you do, DataSync can change your file system's permissions in a way that makes your file share inaccessible and prevents file system backups from being usable. For more information on file- and folder-level access, see the*[ Amazon FSx for Windows File Server User Guide](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/limit-access-file-folder.html)*.

### Required authentication protocols
<a name="configuring-fsx-windows-authentication-protocols"></a>

Your FSx for Windows File Server must use NTLM authentication for DataSync to access it. DataSync can't access a file server that uses Kerberos authentication. 

### DFS Namespaces
<a name="configuring-fsx-windows-location-dfs"></a>

DataSync doesn't support Microsoft Distributed File System (DFS) Namespaces. We recommend specifying an underlying file server or share instead when creating your DataSync location.

For more information, see [Grouping multiple file systems with DFS Namespaces](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/group-file-systems.html) in the *Amazon FSx for Windows File Server User Guide*.

## Creating your FSx for Windows File Server transfer location
<a name="create-fsx-location-how-to"></a>

Before you begin, make sure that you have an existing FSx for Windows File Server in your AWS Region. For more information, see [Getting started with Amazon FSx ](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/getting-started.html) in the *Amazon FSx for Windows File Server User Guide*.

### Using the DataSync console
<a name="create-fsx-location-access-how-to-console"></a>

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/).

1. In the left navigation pane, expand **Data transfer**, then choose **Locations** and **Create location**.

1. For **Location type**, choose **Amazon FSx**.

1. For **FSx file system**, choose the FSx for Windows File Server file system that you want to use as a location.

1. For **Share name**, enter a mount path for your FSx for Windows File Server using forward slashes.

   This specifies the path where DataSync reads or writes data (depending on if this is a source or destination location).

   You can also include subdirectories (for example, `/path/to/directory`).

1. For **Security groups**, choose up to five Amazon EC2 security groups that provide access to your file system's preferred subnet.

   The security groups that you choose must be able to communicate with your file system's security groups. For information about configuring security groups for file system access, see the [https://docs.aws.amazon.com/fsx/latest/WindowsGuide/limit-access-security-groups.html](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/limit-access-security-groups.html).
**Note**  
If you choose a security group that doesn't allow connections from within itself, do one of the following:  
Configure the security group to allow it to communicate within itself.
Choose a different security group that can communicate with the mount target's security group.

1. For **User**, enter the name of a user that can access your FSx for Windows File Server.

   For more information, see [Required permissions](#create-fsx-windows-location-permissions).

1. For **Password**, enter password of the user name.

1. (Optional) For **Domain**, enter the name of the Windows domain that your FSx for Windows File Server file system belongs to.

   If you have multiple Active Directory domains in your environment, configuring this setting makes sure that DataSync connects to the right file system.

1. (Optional) Enter values for the **Key** and **Value** fields to tag the FSx for Windows File Server.

   Tags help you manage, filter, and search for your AWS resources. We recommend creating at least a name tag for your location. 

1. Choose **Create location**.

### Using the AWS CLI
<a name="create-location-fsx-cli"></a>

**To create an FSx for Windows File Server location by using the AWS CLI**
+ Use the following command to create an Amazon FSx location.

  ```
  aws datasync create-location-fsx-windows \
      --fsx-filesystem-arn arn:aws:fsx:{{region}}:{{account-id}}:file-system/{{filesystem-id}} \
      --security-group-arns arn:aws:ec2:{{region}}:{{account-id}}:security-group/{{group-id}} \
      --user {{smb-user}} --password {{password}}
  ```

  In the `create-location-fsx-windows` command, do the following:
  + `fsx-filesystem-arn` – Specify the Amazon Resource Name (ARN) of the file system that you want to transfer to or from.
  + `security-group-arns` – Specify the ARNs of up to five Amazon EC2 security groups that provide access to your file system's preferred subnet.

    The security groups that you specify must be able to communicate with your file system's security groups. For information about configuring security groups for file system access, see the [https://docs.aws.amazon.com/fsx/latest/WindowsGuide/limit-access-security-groups.html](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/limit-access-security-groups.html).
**Note**  
If you choose a security group that doesn't allow connections from within itself, do one of the following:  
Configure the security group to allow it to communicate within itself.
Choose a different security group that can communicate with the mount target's security group.
  + The AWS Region – The Region that you specify is the one where your target Amazon FSx file system is located.

The preceding command returns a location ARN similar to the one shown following.

```
{ 
    "LocationArn": "arn:aws:datasync:us-west-2:111222333444:location/loc-07db7abfc326c50fb" 
}
```