---
id: "@specs/aws/datasync/docs/create-ontap-location"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Configuring transfers with FSx for ONTAP"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Configuring transfers with FSx for ONTAP

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/create-ontap-location
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Configuring transfers with Amazon FSx for NetApp ONTAP
<a name="create-ontap-location"></a>

To transfer data to or from your Amazon FSx for NetApp ONTAP file system, you must create an AWS DataSync transfer *location*. DataSync can use this location as a source or destination for transferring data.

## Providing DataSync access to FSx for ONTAP file systems
<a name="create-ontap-location-access"></a>

To access an FSx for ONTAP file system, DataSync mounts a storage virtual machine (SVM) on your file system using [network interfaces](required-network-interfaces.md) in your virtual private cloud (VPC). DataSync creates these network interfaces in your file system’s preferred subnet only when you create a task that includes your FSx for ONTAP location.

**Note**  
VPCs that you use with DataSync must have default tenancy. VPCs with dedicated tenancy aren't supported.

DataSync can connect to an FSx for ONTAP file system's SVM and copy data by using the Network File System (NFS) or Server Message Block (SMB) protocol.

**Topics**
+ [Using the NFS protocol](#create-ontap-location-supported-protocols)
+ [Using the SMB protocol](#create-ontap-location-smb)
+ [Unsupported protocols](#create-ontap-location-unsupported-protocols)
+ [Choosing the right protocol](#create-ontap-location-choosing-protocol)
+ [Accessing SnapLock volumes](#create-ontap-location-snaplock)

### Using the NFS protocol
<a name="create-ontap-location-supported-protocols"></a>

With the NFS protocol, DataSync uses the `AUTH_SYS` security mechanism with a user ID (UID) and group ID (GID) of `0` to authenticate with your SVM.

**Note**  
DataSync currently only supports NFS version 3 with FSx for ONTAP locations.

### Using the SMB protocol
<a name="create-ontap-location-smb"></a>

With the SMB protocol, DataSync uses credentials that you provide to authenticate with your SVM.

**Supported SMB versions**  
By default, DataSync automatically chooses a version of the SMB protocol based on negotiation with your SMB file server. You also can configure DataSync to use a specific version, but we recommend doing this only if DataSync has trouble negotiating with the SMB file server automatically. For security reasons, we recommend using SMB version 3.0.2 or later.  
See the following table for a list of options in the DataSync console and API for configuring an SMB version with your FSx for ONTAP location:      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/create-ontap-location.html)

**Required permissions**  
You must provide DataSync a local user in your SVM or a domain user in your Microsoft Active Directory with the necessary rights to mount and access your files, folders, and file metadata.  
If you provide a user in your Active Directory, note the following:  
+ If you're using AWS Directory Service for Microsoft Active Directory, the user must be a member of the **AWS Delegated FSx Administrators** group.
+ If you're using a self-managed Active Directory, the user must be a member of one of two groups:
  + The **Domain Admins** group, which is the default delegated administrators group.
  + A custom delegated administrators group with user rights that allow DataSync to copy object ownership permissions and Windows access control lists (ACLs).
**Important**  
You can't change the delegated administrators group after the file system has been deployed. You must either redeploy the file system or restore it from a backup to use the custom delegated administrator group with the following user rights that DataSync needs to copy metadata.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/create-ontap-location.html)
+ If you want to copy Windows ACLs and are transferring between FSx for ONTAP file systems using SMB (or other types of file systems using SMB), the users that you provide DataSync must belong to the same Active Directory domain or have an Active Directory trust relationship between their domains.

**Required authentication protocols**  
For DataSync to access your SMB share, your FSx for ONTAP file system must use NTLM authentication. DataSync can't access FSx for ONTAP file systems that use Kerberos authentication.

**DFS Namespaces**  
DataSync doesn't support Microsoft Distributed File System (DFS) Namespaces. We recommend specifying an underlying file server or share instead when creating your DataSync location.

### Unsupported protocols
<a name="create-ontap-location-unsupported-protocols"></a>

DataSync can't access FSx for ONTAP file systems using the iSCSI (Internet Small Computer Systems Interface) protocol.

### Choosing the right protocol
<a name="create-ontap-location-choosing-protocol"></a>

To preserve file metadata in FSx for ONTAP migrations, configure your DataSync source and destination locations to use the same protocol. Between the supported protocols, SMB preserves metadata with the highest fidelity (see [Understanding how DataSync handles file and object metadata](metadata-copied.md) for details).

When migrating from a Unix (Linux) server or network-attached storage (NAS) share that serves users through NFS, do the following:

1. [Create an NFS location](create-nfs-location.md) for the Unix (Linux) server or NAS share. (This will be your source location.)

1. Configure the FSx for ONTAP volume you’re transferring data to with the [Unix security style](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-volumes.html#volume-security-style).

1. Create a location for your FSx for ONTAP file system that’s configured for NFS. (This will be your destination location.)

When migrating from a Windows server or NAS share that serves users through SMB, do the following:

1. [Create an SMB location](create-smb-location.md) for the Windows server or NAS share. (This will be your source location.)

1. Configure the FSx for ONTAP volume you’re transferring data to with the [NTFS security style](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-volumes.html#volume-security-style).

1. Create a location for your FSx for ONTAP file system that’s configured for SMB. (This will be your destination location.)

If your FSx for ONTAP environment uses multiple protocols, we recommend working with an AWS storage specialist. To learn about best practices for multiprotocol access, see [Enabling multiprotocol workloads with Amazon FSx for NetApp ONTAP](https://aws.amazon.com/blogs/storage/enabling-multiprotocol-workloads-with-amazon-fsx-for-netapp-ontap/).

### Accessing SnapLock volumes
<a name="create-ontap-location-snaplock"></a>

If you're transferring data to a [SnapLock volume](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snaplock.html) on an FSx for ONTAP file system, make sure the SnapLock settings **Autocommit** and **Volume append mode** are disabled on the volume during your transfer. You can re-enable these settings when you're done transferring data.

## Creating your FSx for ONTAP transfer location
<a name="create-ontap-location-how-to"></a>

To create the location, you need an existing FSx for ONTAP file system. If you don't have one, see [Getting started with Amazon FSx for NetApp ONTAP](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/getting-started.html) in the *Amazon FSx for NetApp ONTAP User Guide*.

### Using the DataSync console
<a name="create-ontap-location-console"></a>

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/).

1. In the left navigation pane, expand **Data transfer**, then choose **Locations** and **Create location**.

1. For **Location type**, choose **Amazon FSx**.

   You configure this location as a source or destination later.

1. For **FSx file system**, choose the FSx for ONTAP file system that you want to use as a location.

1. For **Storage virtual machine**, choose a storage virtual machine (SVM) in your file system where you want to copy data to or from.

1. For **Mount path**, specify a path to the file share in that SVM where you'll copy your data.

   You can specify a junction path (also known as a mount point), qtree path (for NFS file shares), or share name (for SMB file shares). For example, your mount path might be `/vol1`, `/vol1/tree1`, or `/share1`.
**Tip**  
Don't specify a path in the SVM's root volume. For more information, see [Managing FSx for ONTAP storage virtual machines](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-svms.html) in the *Amazon FSx for NetApp ONTAP User Guide*.

1. For **Security groups**, choose up to five Amazon EC2 security groups that provide access to your file system's preferred subnet.

   The security groups must allow outbound traffic on the following ports (depending on the protocol you use):
   + **NFS** – TCP ports 111, 635, and 2049 
   + **SMB** – TCP port 445

   Your file system's security groups must also allow inbound traffic on the same ports.

1. For **Protocol**, choose the data transfer protocol that DataSync uses to access your file system's SVM.

   For more information, see [Choosing the right protocol](#create-ontap-location-choosing-protocol).

------
#### [ NFS ]

   DataSync uses NFS version 3.

------
#### [ SMB ]

   Configure an SMB version, user, password, and Active Directory domain name (if needed) to access the SVM.
   + (Optional) Expand **Additional settings** and choose an **SMB version** for DataSync to use when accessing your SVM.

     By default, DataSync automatically chooses a version based on negotiation with the SMB file server. For more information, see [Using the SMB protocol](#create-ontap-location-smb).
   + For **User**, enter a user name that can mount and access the files, folders, and metadata that you want to transfer in the SVM.

     For more information, see [Using the SMB protocol](#create-ontap-location-smb).
   + For **Password**, enter the password of the user that you specified that can access the SVM.
   + (Optional) For **Active Directory domain name**, enter the fully qualified domain name (FQDN) of the Active Directory that your SVM belongs to.

     If you have multiple domains in your environment, configuring this setting makes sure that DataSync connects to the right SVM.

------

1. (Optional) Enter values for the **Key** and **Value** fields to tag the FSx for ONTAP file system.

   Tags help you manage, filter, and search for your AWS resources. We recommend creating at least a name tag for your location. 

1. Choose **Create location**.

### Using the AWS CLI
<a name="create-ontap-location-cli"></a>

**To create an FSx for ONTAP location by using the AWS CLI**

1. Copy the following `create-location-fsx-ontap` command:

   ```
   aws datasync create-location-fsx-ontap \
      --storage-virtual-machine-arn arn:aws:fsx:{{region}}:{{account-id}}:storage-virtual-machine/fs-{{file-system-id}} \
      --security-group-arns arn:aws:ec2:{{region}}:{{account-id}}:security-group/{{group-id}} \
      --protocol {{data-transfer-protocol}}={}
   ```

1. Specify the following required options in the command:
   + For `storage-virtual-machine-arn`, specify the fully qualified Amazon Resource Name (ARN) of a storage virtual machine (SVM) in your file system where you want to copy data to or from.

     This ARN includes the AWS Region where your file system resides, your AWS account, and the file system and SVM IDs.
   + For `security-group-arns`, specify the ARNs of the Amazon EC2 security groups that provide access to the [network interfaces](required-network-interfaces.md) of your file system's preferred subnet.

     This includes the AWS Region where your Amazon EC2 instance resides, your AWS account, and your security group IDs. You can specify up to five security group ARNs.

     For more information about security groups, see [File System Access Control with Amazon VPC](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/limit-access-security-groups.html) in the *Amazon FSx for NetApp ONTAP User Guide*.
   + For `protocol`, configure the protocol that DataSync uses to access your file system's SVM.
     + For NFS, you can use the default configuration:

       `--protocol NFS={}`
     + For SMB, you must specify a user name and password that can access the SVM:

       `--protocol SMB={User={{smb-user}},Password={{smb-password}}}`

1. Run the command.

   You get a response that shows the location that you just created.

   ```
   { 
       "LocationArn": "arn:aws:datasync:us-west-2:123456789012:location/loc-abcdef01234567890" 
   }
   ```