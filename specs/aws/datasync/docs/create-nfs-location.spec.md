---
id: "@specs/aws/datasync/docs/create-nfs-location"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Configuring transfers with an NFS file server"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Configuring transfers with an NFS file server

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/create-nfs-location
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Configuring AWS DataSync transfers with an NFS file server
<a name="create-nfs-location"></a>

With AWS DataSync, you can transfer data between your Network File System (NFS) file server and the following AWS storage services. Supported storage services depend on your task mode, as shown below:


| Basic mode | Enhanced mode | 
| --- | --- | 
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/create-nfs-location.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/create-nfs-location.html)  | 

To set up this kind of transfer, you create a [location](how-datasync-transfer-works.md#sync-locations) for your NFS file server. You can use this location as a transfer source or destination.

## Providing DataSync access to NFS file servers
<a name="accessing-nfs"></a>

For DataSync to access your NFS file server, you need a DataSync [agent](how-datasync-transfer-works.md#sync-agents). The agent mounts an export on your file server by using the NFS protocol. Be sure to use the agent that corresponds to your desired task mode.

**Topics**
+ [Configuring your NFS export](#accessing-nfs-configuring-export)
+ [Supported NFS versions](#supported-nfs-versions)

### Configuring your NFS export
<a name="accessing-nfs-configuring-export"></a>

The export that DataSync needs for your transfer depends on if your NFS file server is a source or destination location and how your file server's permissions are configured.

If your file server is a source location, DataSync just has to read and traverse your files and folders. If it's a destination location, DataSync needs root access to write to the location and set ownership, permissions, and other metadata on the files and folders that you're copying. You can use the `no_root_squash` option to allow root access for your export.

The following examples describe how to configure an NFS export that provides access to DataSync.

**When your NFS file server is a source location (root access)**  
Configure your export by using the following command, which provides DataSync read-only permissions (`ro`) and root access ( `no_root_squash`):

```
{{export-path}} {{datasync-agent-ip-address}}(ro,no_root_squash)
```

**When your NFS file server is a destination location**  
Configure your export by using the following command, which provides DataSync write permissions (`rw`) and root access ( `no_root_squash`):

```
{{export-path}} {{datasync-agent-ip-address}}(rw,no_root_squash)
```

**When your NFS file server is a source location (no root access)**  
Configure your export by using the following command, which specifies the POSIX user ID (UID) and group ID (GID) that you know would provide DataSync read-only permissions on the export:

```
{{export-path}} {{datasync-agent-ip-address}}(ro,all_squash,anonuid={{uid}},anongid={{gid}})
```

### Supported NFS versions
<a name="supported-nfs-versions"></a>

By default, DataSync uses NFS version 4.1. DataSync also supports NFS 4.0 and 3.x.

## Configuring your network for NFS transfers
<a name="configure-network-nfs-location"></a>

For your DataSync transfer, you must configure traffic for a few network connections: 

1. Allow traffic on the following ports from your DataSync agent to your NFS file server:
   + **For NFS version 4.1 and 4.0** – TCP port 2049
   + **For NFS version 3.x** – TCP ports 111 and 2049

   Other NFS clients in your network should be able to mount the NFS export that you're using to transfer data. The export must also be accessible without Kerberos authentication.

1. Configure traffic for your [service endpoint connection](datasync-network.md) (such as a VPC, public, or FIPS endpoint).

1. Allow traffic from the DataSync service to the [AWS storage service](datasync-network.md#storage-service-network-requirements) you're transferring to or from.

## Creating your NFS transfer location
<a name="create-nfs-location-how-to"></a>

Before you begin, note the following:
+ You need an NFS file server that you want to transfer data from.
+ You need a DataSync agent that can [access your file server](#accessing-nfs).
+  DataSync doesn't support copying NFS version 4 access control lists (ACLs).

### Using the DataSync console
<a name="create-nfs-location-console"></a>

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/).

1. In the left navigation pane, expand **Data transfer**, then choose **Locations** and **Create location**.

1. For **Location type**, choose **Network File System (NFS)**.

1. For **Agents**, choose the DataSync agent that can connect to your NFS file server.

   You can choose more than one agent. For more information, see [Using multiple DataSync agents](do-i-need-datasync-agent.md#multiple-agents).

1. For **NFS server**, enter the Domain Name System (DNS) name or IP address of the NFS file server that your DataSync agent connects to.

1. For **Mount path**, enter the NFS export path that you want DataSync to mount.

   This path (or a subdirectory of the path) is where DataSync transfers data to or from. For more information, see [Configuring your NFS export](#accessing-nfs-configuring-export).

1. (Optional) Expand **Additional settings** and choose a specific **NFS version** for DataSync to use when accessing your file server.

   For more information, see [Supported NFS versions](#supported-nfs-versions).

1. (Optional) Choose **Add tag** to tag your NFS location.

   *Tags* are key-value pairs that help you manage, filter, and search for your locations. We recommend creating at least a name tag for your location. 

1. Choose **Create location**.

### Using the AWS CLI
<a name="create-location-nfs-cli"></a>
+ Use the following command to create an NFS location.

  ```
  aws datasync create-location-nfs \
      --server-hostname {{nfs-server-address}} \
      --on-prem-config AgentArns={{datasync-agent-arns}} \
      --subdirectory{{ nfs-export-path}}
  ```

  For more information on creating the location, see [Providing DataSync access to NFS file servers](#accessing-nfs).

  DataSync automatically chooses the NFS version that it uses to read from an NFS location. To specify an NFS version, use the optional `Version` parameter in the [NfsMountOptions](https://docs.aws.amazon.com/datasync/latest/apireference/API_NfsMountOptions.html) API operation.

This command returns the Amazon Resource Name (ARN) of the NFS location, similar to the ARN shown following.

```
{
    "LocationArn": "arn:aws:datasync:us-east-1:111222333444:location/loc-0f01451b140b2af49"
}
```

To make sure that the directory can be mounted, you can connect to any computer that has the same network configuration as your agent and run the following command. 

```
mount -t nfs -o nfsvers=<{{nfs-server-version}} <{{nfs-server-address}}:<{{nfs-export-path}} <{{test-folder}}
```

The following is an example of the command.

```
mount -t nfs -o nfsvers=3 198.51.100.123:/path_for_sync_to_read_from /temp_folder_to_test_mount_on_local_machine
```