---
id: "@specs/aws/datasync/docs/create-smb-location"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Configuring transfers with an SMB file server"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Configuring transfers with an SMB file server

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/create-smb-location
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Configuring AWS DataSync transfers with an SMB file server
<a name="create-smb-location"></a>

With AWS DataSync, you can transfer data between your Server Message Block (SMB) file server and the following AWS storage services. Supported storage services depend on your task mode, as shown below:


| Basic mode | Enhanced mode | 
| --- | --- | 
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/create-smb-location.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/create-smb-location.html)  | 

To set up this kind of transfer, you create a [location](how-datasync-transfer-works.md#sync-locations) for your SMB file server. You can use this as a transfer source or destination. Be sure to use the agent that corresponds to your desired task mode.

## Providing DataSync access to SMB file servers
<a name="configuring-smb"></a>

DataSync connects to your file server using the SMB protocol and can authenticate with NTLM or Kerberos.

**Topics**
+ [Supported SMB versions](#configuring-smb-version)
+ [Using NTLM authentication](#configuring-smb-ntlm-authentication)
+ [Using Kerberos authentication](#configuring-smb-kerberos-authentication)
+ [Required permissions](#configuring-smb-permissions)
+ [DFS Namespaces](#configuring-smb-location-dfs)

### Supported SMB versions
<a name="configuring-smb-version"></a>

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

### Using NTLM authentication
<a name="configuring-smb-ntlm-authentication"></a>

To use NTLM authentication, you provide a user name and password that allows DataSync to access the SMB file server that you're transferring to or from. The user can be a local user on your file server or a domain user in your Microsoft Active Directory.

### Using Kerberos authentication
<a name="configuring-smb-kerberos-authentication"></a>

To use Kerberos authentication, you provide a Kerberos principal, Kerberos key table (keytab) file, and Kerberos configuration file that allows DataSync to access the SMB file server that you're transferring to or from.

**Topics**
+ [Prerequisites](#configuring-smb-kerberos-prerequisites)
+ [DataSync configuration options for Kerberos](#configuring-smb-kerberos-options)

#### Prerequisites
<a name="configuring-smb-kerberos-prerequisites"></a>

You need to create a couple Kerberos artifacts and configure your network so that DataSync can access your SMB file server.
+ Create a Kerberos keytab file by using the [ktpass](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ktpass) or [kutil](https://web.mit.edu/kerberos/krb5-1.12/doc/admin/admin_commands/ktutil.html) utility.

  The following example creates a keytab file by using `ktpass`. The Kerberos realm that you specify (`MYDOMAIN.ORG`) must be upper case.

  ```
  ktpass /out C:\YOUR_KEYTAB.keytab /princ HOST/kerberosuser@MYDOMAIN.ORG /mapuser kerberosuser /pass * /crypto AES256-SHA1 /ptype KRB5_NT_PRINCIPAL
  ```
+ Prepare a simplified version of the Kerberos configuration file (`krb5.conf`). Include information about the realm, the location of the domain admin servers, and mappings of hostnames onto a Kerberos realm.

  Verify that the `krb5.conf` content is formatted with the correct mixed casing for the realms and domain realm names. For example:

  ```
  [libdefaults] 
    dns_lookup_realm = true 
    dns_lookup_kdc = true 
    forwardable = true 
    default_realm = MYDOMAIN.ORG
  
  [realms] 
    MYDOMAIN.ORG = { 
      kdc = mydomain.org 
      admin_server = mydomain.org 
    }
  
  [domain_realm] 
    .mydomain.org = MYDOMAIN.ORG 
    mydomain.org = MYDOMAIN.ORG
  ```
+ In your network configuration, make sure that your Kerberos Key Distribution Center (KDC) server port is open. The KDC port is typically TCP port 88.

#### DataSync configuration options for Kerberos
<a name="configuring-smb-kerberos-options"></a>

When creating an SMB location that uses Kerberos, you configure the following options.


| Console option | API option | Description | 
| --- | --- | --- | 
| **SMB server** | `ServerHostName` | The domain name of the SMB file server that your DataSync agent will mount. For Kerberos, you can't specify the file server's IP address. | 
| **Kerberos principal** | `KerberosPrincipal` | An identity in your Kerberos realm that has permission to access the files, folders, and file metadata in your SMB file server.<br />A Kerberos principal might look like `HOST/kerberosuser@MYDOMAIN.ORG`.<br />Principal names are case sensitive. | 
| **Keytab file** | `KerberosKeytab`  | A Kerberos key table (keytab) file, which includes mappings between your Kerberos principal and encryption keys. | 
| **Kerberos configuration file** | `KerberosKrbConf` | A `krb5.conf` file that defines your Kerberos realm configuration. | 
| **DNS IP addresses** (optional) | `DnsIpAddresses` | The IPv4 addresses for the DNS servers that your SMB file server belongs to.<br />If you have multiple domains in your environment, configuring this makes sure that DataSync connects to the right SMB file server. | 

### Required permissions
<a name="configuring-smb-permissions"></a>

The identity that you provide DataSync must have permission to mount and access your SMB file server's files, folders, and file metadata.

If you provide an identity in your Active Directory, it must be a member of an Active Directory group with one or both of the following user rights (depending the [metadata that you want DataSync to copy](configure-metadata.md)):


| User right | Description | 
| --- | --- | 
| **Restore files and directories** (`SE_RESTORE_NAME`) | Allows DataSync to copy object ownership, permissions, file metadata, and NTFS discretionary access lists (DACLs).<br />This user right is usually granted to members of the **Domain Admins** and **Backup Operators** groups (both of which are default Active Directory groups). | 
| **Manage auditing and security log** (`SE_SECURITY_NAME`) | Allows DataSync to copy NTFS system access control lists (SACLs).<br />This user right is usually granted to members of the **Domain Admins** group.  | 

If you want to copy Windows ACLs and are transferring between an SMB file server and another storage system that uses SMB (such as Amazon FSx for Windows File Server or FSx for ONTAP), the identity that you provide DataSync must belong to the same Active Directory domain or have an Active Directory trust relationship between their domains.

### DFS Namespaces
<a name="configuring-smb-location-dfs"></a>

DataSync doesn't support Microsoft Distributed File System (DFS) Namespaces. We recommend specifying an underlying file server or share instead when creating your DataSync location.

## Creating your SMB transfer location
<a name="create-smb-location-how-to"></a>

Before you begin, you need an SMB file server that you want to transfer data from.

### Using the DataSync console
<a name="create-smb-location-how-to-console"></a>

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/).

1. In the left navigation pane, expand **Data transfer**, then choose **Locations** and **Create location**.

1. For **Location type**, choose **Server Message Block (SMB)**.

   You configure this location as a source or destination later.

1. For **Agents**, choose the DataSync agent that can connect to your SMB file server.

   You can choose more than one agent. For more information, see [Using multiple DataSync agents](do-i-need-datasync-agent.md#multiple-agents).

1. For **SMB server**, enter the domain name or IP address of the SMB file server that your DataSync agent will mount.

   Remember the following with this setting:
   + You can't specify an IP version 6 (IPv6) address.
   + If you're using Kerberos authentication, you must specify a domain name.

1. For **Share name**, enter the name of the share exported by your SMB file server where DataSync will read or write data.

   You can include a subdirectory in the share path (for example, `/path/to/subdirectory`). Make sure that other SMB clients in your network can also mount this path. 

   To copy all the data in the subdirectory, DataSync must be able to mount the SMB share and access all of its data. For more information, see [Required permissions](#configuring-smb-permissions).

1. (Optional) Expand **Additional settings** and choose an **SMB Version** for DataSync to use when accessing your file server.

   By default, DataSync automatically chooses a version based on negotiation with the SMB file server. For information, see [Supported SMB versions](#configuring-smb-version).

1. For **Authentication type**, choose **NTLM** or **Kerberos**.

1. Do one of the following depending on your authentication type:

------
#### [ NTLM ]
   + For **User**, enter a user name that can mount your SMB file server and has permission to access the files and folders involved in your transfer.

     For more information, see [Required permissions](#configuring-smb-permissions).
   + For **Password**, enter the password of the user who can mount your SMB file server and has permission to access the files and folders involved in your transfer.
   + (Optional) For **Domain**, enter the Windows domain name that your SMB file server belongs to.

     If you have multiple domains in your environment, configuring this setting makes sure that DataSync connects to the right SMB file server.

------
#### [ Kerberos ]
   + For **Kerberos principal**, specify a principal in your Kerberos realm that has permission to access the files, folders, and file metadata in your SMB file server.

     A Kerberos principal might look like `HOST/kerberosuser@MYDOMAIN.ORG`.

     Principal names are case sensitive. Your DataSync task execution will fail if the principal that you specify for this setting doesn’t exactly match the principal that you use to create the keytab file.
   + For **Keytab file**, upload a keytab file that includes mappings between your Kerberos principal and encryption keys.
   + For **Kerberos configuration file**, upload a `krb5.conf` file that defines your Kerberos realm configuration.
   + (Optional) For **DNS IP addresses**, specify up to two IPv4 addresses for the DNS servers that your SMB file server belongs to. 

     If you have multiple domains in your environment, configuring this parameter makes sure that DataSync connects to the right SMB file server.

------

1. (Optional) Choose **Add tag** to tag your SMB location.

   *Tags* are key-value pairs that help you manage, filter, and search for your locations. We recommend creating at least a name tag for your location. 

1. Choose **Create location**.

### Using the AWS CLI
<a name="create-location-smb-cli"></a>

The following instructions describe how to create SMB locations with NTLM or Kerberos authentication.

------
#### [ NTLM ]

1. Copy the following `create-location-smb` command.

   ```
   aws datasync create-location-smb \
       --agent-arns {{datasync-agent-arns}} \
       --server-hostname {{smb-server-address}} \
       --subdirectory{{ smb-export-path}} \
       --authentication-type "NTLM" \
       --user {{user-who-can-mount-share}} \
       --password {{user-password}} \
       --domain {{windows-domain-of-smb-server}}
   ```

1. For `--agent-arns`, specify the DataSync agent that can connect to your SMB file server.

   You can choose more than one agent. For more information, see [Using multiple DataSync agents](do-i-need-datasync-agent.md#multiple-agents).

1. For `--server-hostname`, specify the domain name or IPv4 address of the SMB file server that your DataSync agent will mount. 

1. For `--subdirectory`, specify the name of the share exported by your SMB file server where DataSync will read or write data.

   You can include a subdirectory in the share path (for example, `/path/to/subdirectory`). Make sure that other SMB clients in your network can also mount this path. 

   To copy all the data in the subdirectory, DataSync must be able to mount the SMB share and access all of its data. For more information, see [Required permissions](#configuring-smb-permissions).

1. For `--user`, specify a user name that can mount your SMB file server and has permission to access the files and folders involved in your transfer.

   For more information, see [Required permissions](#configuring-smb-permissions).

1. For `--password`, specify the password of the user who can mount your SMB file server and has permission to access the files and folders involved in your transfer.

1. (Optional) For `--domain`, specify the Windows domain name that your SMB file server belongs to.

   If you have multiple domains in your environment, configuring this setting makes sure that DataSync connects to the right SMB file server.

1. (Optional) Add the `--version` option if you want DataSync to use a specific SMB version. For more information, see [Supported SMB versions](#configuring-smb-version).

1. Run the `create-location-smb` command.

   If the command is successful, you get a response that shows you the ARN of the location that you created. For example:

   ```
   {
       "arn:aws:datasync:us-east-1:123456789012:location/loc-01234567890example"
   }
   ```

------
#### [ Kerberos ]

1. Copy the following `create-location-smb` command.

   ```
   aws datasync create-location-smb \
       --agent-arns {{datasync-agent-arns}} \
       --server-hostname {{smb-server-address}} \
       --subdirectory{{ smb-export-path}} \
       --authentication-type "KERBEROS" \
       --kerberos-principal "{{HOST/kerberosuser@EXAMPLE.COM}}" \
       --kerberos-keytab "fileb://{{path/to/file.keytab}}" \
       --kerberos-krb5-conf "file://{{path/to/}}krb5.conf" \
       --dns-ip-addresses {{array-of-ipv4-addresses}}
   ```

1. For `--agent-arns`, specify the DataSync agent that can connect to your SMB file server.

   You can choose more than one agent. For more information, see [Using multiple DataSync agents](do-i-need-datasync-agent.md#multiple-agents).

1. For `--server-hostname`, specify the domain name of the SMB file server that your DataSync agent will mount. 

1. For `--subdirectory`, specify the name of the share exported by your SMB file server where DataSync will read or write data.

   You can include a subdirectory in the share path (for example, `/path/to/subdirectory`). Make sure that other SMB clients in your network can also mount this path. 

   To copy all the data in the subdirectory, DataSync must be able to mount the SMB share and access all of its data. For more information, see [Required permissions](#configuring-smb-permissions).

1. For the Kerberos options, do the following:
   + `--kerberos-principal`: Specify a principal in your Kerberos realm that has permission to access the files, folders, and file metadata in your SMB file server.

     A Kerberos principal might look like `HOST/kerberosuser@MYDOMAIN.ORG`.

     Principal names are case sensitive. Your DataSync task execution will fail if the principal that you specify for this option doesn’t exactly match the principal that you use to create the keytab file.
   + `--kerberos-keytab`: Specify a keytab file that includes mappings between your Kerberos principal and encryption keys.
   + `--kerberos-krb5-conf`: Specify a `krb5.conf` file that defines your Kerberos realm configuration.
   + (Optional) `--dns-ip-addresses`: Specify up to two IPv4 addresses for the DNS servers that your SMB file server belongs to. 

     If you have multiple domains in your environment, configuring this parameter makes sure that DataSync connects to the right SMB file server.

1. (Optional) Add the `--version` option if you want DataSync to use a specific SMB version. For more information, see [Supported SMB versions](#configuring-smb-version).

1. Run the `create-location-smb` command.

   If the command is successful, you get a response that shows you the ARN of the location that you created. For example:

   ```
   {
       "arn:aws:datasync:us-east-1:123456789012:location/loc-01234567890example"
   }
   ```

------