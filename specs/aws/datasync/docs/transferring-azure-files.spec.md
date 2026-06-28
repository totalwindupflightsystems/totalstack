---
id: "@specs/aws/datasync/docs/transferring-azure-files"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Configuring transfers with Microsoft Azure Files"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Configuring transfers with Microsoft Azure Files

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/transferring-azure-files
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Configuring AWS DataSync transfers with Microsoft Azure Files SMB shares
<a name="transferring-azure-files"></a>

You can configure AWS DataSync to transfer data to or from a Microsoft Azure Files Server Message Block (SMB) share.

**Tip**  
For a full walkthrough on moving data from Azure Files SMB shares to AWS, see the [AWS Storage Blog](https://aws.amazon.com/blogs/storage/how-to-move-data-from-azure-files-smb-shares-to-aws-using-aws-datasync/).

## Providing DataSync access to SMB shares
<a name="configuring-smb-azure-files"></a>

DataSync connects to your SMB share using the SMB protocol and authenticates with credentials that you provide it.

**Topics**
+ [Supported SMB protocol versions](#configuring-smb-version-azure-files)
+ [Required permissions](#configuring-smb-permissions-azure-files)

### Supported SMB protocol versions
<a name="configuring-smb-version-azure-files"></a>

By default, DataSync automatically chooses a version of the SMB protocol based on negotiation with your SMB file server.

You also can configure DataSync to use a specific SMB version, but we recommend doing this only if DataSync has trouble negotiating with the SMB file server automatically. DataSync supports SMB versions 1.0 and later. For security reasons, we recommend using SMB version 3.0.2 or later. Earlier versions, such as SMB 1.0, contain known security vulnerabilities that attackers can exploit to compromise your data.

See the following table for a list of options in the DataSync console and API:


| Console option | API option | Description | 
| --- | --- | --- | 
| Automatic | `AUTOMATIC` | DataSync and the SMB file server negotiate the highest version of SMB that they mutually support between 2.1 and 3.1.1.<br />This is the default and recommended option. If you instead choose a specific version that your file server doesn't support, you may get an `Operation Not Supported` error. | 
| SMB 3.0.2 | `SMB3` | Restricts the protocol negotiation to only SMB version 3.0.2. | 
| SMB 2.1 | `SMB2` | Restricts the protocol negotiation to only SMB version 2.1. | 
| SMB 2.0 | `SMB2_0` | Restricts the protocol negotiation to only SMB version 2.0. | 
| SMB 1.0 | `SMB1` | Restricts the protocol negotiation to only SMB version 1.0. | 

### Required permissions
<a name="configuring-smb-permissions-azure-files"></a>

DataSync needs a user who has permission to mount and access your SMB location. This can be a local user on your Windows file server or a domain user that's defined in your Microsoft Active Directory.

To set object ownership, DataSync requires the `SE_RESTORE_NAME` privilege, which is usually granted to members of the built-in Active Directory groups **Backup Operators** and **Domain Admins**. Providing a user to DataSync with this privilege also helps ensure sufficient permissions to files, folders, and file metadata, except for NTFS system access control lists (SACLs).

Additional privileges are required to copy SACLs. Specifically, this requires the Windows `SE_SECURITY_NAME` privilege, which is granted to members of the **Domain Admins** group. If you configure your task to copy SACLs, make sure that the user has the required privileges. To learn more about configuring a task to copy SACLs, see [Configuring how to handle files, objects, and metadata](configure-metadata.md).

When you copy data between an SMB file server and Amazon FSx for Windows File Server file system, the source and destination locations must belong to the same Microsoft Active Directory domain or have an Active Directory trust relationship between their domains.

## Creating your Azure Files transfer location by using the console
<a name="create-azure-files-smb-location-how-to"></a>

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/).

1. In the left navigation pane, expand **Data transfer**, then choose **Locations** and **Create location**.

1. For **Location type**, choose **Server Message Block (SMB)**.

   You configure this location as a source or destination later.

1. For **Agents**, choose one or more DataSync agents that you want to connect to your SMB share.

   If you choose more than one agent, make sure you understand using [multiple agents for a location](do-i-need-datasync-agent.md#multiple-agents).

1. For **SMB Server**, enter the Domain Name System (DNS) name or IP address of the SMB share that your DataSync agent will mount.
**Note**  
You can't specify an IP version 6 (IPv6) address.

1. For **Share name**, enter the name of the share exported by your SMB share where DataSync will read or write data.

   You can include a subdirectory in the share path (for example, `/path/to/subdirectory`). Make sure that other SMB clients in your network can also mount this path. 

   To copy all the data in the subdirectory, DataSync must be able to mount the SMB share and access all of its data. For more information, see [Required permissions](create-smb-location.md#configuring-smb-permissions).

1. (Optional) Expand **Additional settings** and choose an **SMB Version** for DataSync to use when accessing your SMB share.

   By default, DataSync automatically chooses a version based on negotiation with the SMB share. For information, see [Supported SMB versions](create-smb-location.md#configuring-smb-version).

1. For **User**, enter a user name that can mount your SMB share and has permission to access the files and folders involved in your transfer.

   For more information, see [Required permissions](create-smb-location.md#configuring-smb-permissions).

1. For **Password**, enter the password of the user who can mount your SMB share and has permission to access the files and folders involved in your transfer.

1. (Optional) For **Domain**, enter the Windows domain name that your SMB share belongs to.

   If you have multiple domains in your environment, configuring this setting makes sure that DataSync connects to the right share.

1. (Optional) Choose **Add tag** to tag your location.

   *Tags* are key-value pairs that help you manage, filter, and search for your locations. We recommend creating at least a name tag for your location. 

1. Choose **Create location**.