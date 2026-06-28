---
id: "@specs/aws/datasync/docs/create-hdfs-location"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Configuring transfers with an HDFS cluster"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Configuring transfers with an HDFS cluster

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/create-hdfs-location
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Configuring AWS DataSync transfers with an HDFS cluster
<a name="create-hdfs-location"></a>

With AWS DataSync, you can transfer data between your Hadoop Distributed File System (HDFS) cluster and one of the following AWS storage services using Basic mode tasks:
+ [Amazon S3](create-s3-location.md)
+ [Amazon EFS](create-efs-location.md)
+ [Amazon FSx for Windows File Server](create-fsx-location.md)
+ [Amazon FSx for Lustre](create-lustre-location.md)
+ [Amazon FSx for OpenZFS](create-openzfs-location.md)
+ [Amazon FSx for NetApp ONTAP](create-ontap-location.md)

To set up this kind of transfer, you create a [location](how-datasync-transfer-works.md#sync-locations) for your HDFS cluster. You can use this location as a transfer source or destination.

## Providing DataSync access to HDFS clusters
<a name="accessing-hdfs"></a>

To connect to your HDFS cluster, DataSync uses a Basic mode agent [agent that you deploy](deploy-agents.md) as close as possible to your HDFS cluster. The DataSync agent acts as an HDFS client and communicates with the NameNodes and DataNodes in your cluster.

When you start a transfer task, DataSync queries the NameNode for locations of files and folders on the cluster. If you configure your HDFS location as a source location, DataSync reads files and folder data from the DataNodes in your cluster and copies that data to the destination. If you configure your HDFS location as a destination location, then DataSync writes files and folders from the source to the DataNodes in your cluster.

### Authentication
<a name="accessing-hdfs-authentication"></a>

When connecting to an HDFS cluster, DataSync supports simple authentication or Kerberos authentication. To use simple authentication, provide the user name of a user with rights to read and write to the HDFS cluster. To use Kerberos authentication, provide a Kerberos configuration file, a Kerberos key table (keytab) file, and a Kerberos principal name. The credentials of the Kerberos principal must be in the provided keytab file.

### Encryption
<a name="accessing-hdfs-encryption"></a>

When using Kerberos authentication, DataSync supports encryption of data as it's transmitted between the DataSync agent and your HDFS cluster. Encrypt your data by using the Quality of Protection (QOP) configuration settings on your HDFS cluster and by specifying the QOP settings when creating your HDFS location. The QOP configuration includes settings for data transfer protection and Remote Procedure Call (RPC) protection. 

**DataSync supports the following Kerberos encryption types:**
+ `des-cbc-crc`
+ `des-cbc-md4`
+ `des-cbc-md5`
+ `des3-cbc-sha1`
+ `arcfour-hmac`
+ `arcfour-hmac-exp`
+ `aes128-cts-hmac-sha1-96`
+ `aes256-cts-hmac-sha1-96`
+ `aes128-cts-hmac-sha256-128`
+ `aes256-cts-hmac-sha384-192`
+ `camellia128-cts-cmac`
+ `camellia256-cts-cmac`

You can also configure HDFS clusters for encryption at rest using Transparent Data Encryption (TDE). When using simple authentication, DataSync reads and writes to TDE-enabled clusters. If you're using DataSync to copy data to a TDE-enabled cluster, first configure the encryption zones on the HDFS cluster. DataSync doesn't create encryption zones. 

## Unsupported HDFS features
<a name="hdfs-unsupported-features"></a>

The following HDFS capabilities aren't currently supported by DataSync:
+ Transparent Data Encryption (TDE) when using Kerberos authentication
+ Configuring multiple NameNodes
+ Hadoop HDFS over HTTP (HttpFS)
+ POSIX access control lists (ACLs)
+ HDFS extended attributes (xattrs)
+ HDFS clusters using Apache HBase

## Creating your HDFS transfer location
<a name="create-hdfs-location-how-to"></a>

You can use your location as a source or destination for your DataSync transfer.

**Before you begin**: Verify network connectivity between your agent and Hadoop cluster by doing the following:
+ Test access to the TCP ports listed in [Network requirements for on-premises, self-managed, and other cloud storage](datasync-network.md#on-premises-network-requirements).
+ Test access between your local agent and your Hadoop cluster. For instructions, see [Verifying your agent's connection to your storage system](test-agent-connections.md#self-managed-storage-connectivity).

### Using the DataSync console
<a name="create-hdfs-location-how-to-console"></a>

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/).

1. In the left navigation pane, expand **Data transfer**, then choose **Locations** and **Create location**.

1. For **Location type**, choose **Hadoop Distributed File System (HDFS)**.

   You can configure this location as a source or destination later. 

1. For **Agents**, choose the agent that can connect to your HDFS cluster.

   You can choose more than one agent. For more information, see [Using multiple DataSync agents](do-i-need-datasync-agent.md#multiple-agents).

1. For **NameNode**, provide the domain name or IP address of your HDFS cluster's primary NameNode.

1. For **Folder**, enter a folder on your HDFS cluster that you want DataSync to use for the data transfer.

   If your HDFS location is a source, DataSync copies the files in this folder to the destination. If your location is a destination, DataSync writes files to this folder.

1. To set the **Block size** or **Replication factor**, choose **Additional settings**.

   The default block size is 128 MiB. The block sizes that you provide must be a multiple of 512 bytes.

   The default replication factor is three DataNodes when transferring to the HDFS cluster. 

1. In the **Security** section, choose the **Authentication type** used on your HDFS cluster. 
   + **Simple** – For **User**, specify the user name with the following permissions on the HDFS cluster (depending on your use case):
     + If you plan to use this location as a source location, specify a user that only has read permissions.
     + If you plan to use this location as a destination location, specify a user that has read and write permissions.

     Optionally, specify the URI of the Key Management Server (KMS) of your HDFS cluster. 
   + **Kerberos** – Specify the Kerberos **Principal** with access to your HDFS cluster. Next, provide the **KeyTab file** that contains the provided Kerberos principal. Then, provide the **Kerberos configuration file**. Finally, specify the type of encryption in transit protection in the **RPC protection** and **Data transfer protection** dropdown lists.

1. (Optional) Choose **Add tag** to tag your HDFS location.

   *Tags* are key-value pairs that help you manage, filter, and search for your locations. We recommend creating at least a name tag for your location. 

1. Choose **Create location**.

### Using the AWS CLI
<a name="create-location-hdfs-cli"></a>

1. Copy the following `create-location-hdfs` command.

   ```
   aws datasync create-location-hdfs --name-nodes [{"Hostname":"{{host1}}", "Port": {{8020}}}] \
       --authentication-type "{{SIMPLE|KERBEROS}}" \
       --agent-arns [{{arn:aws:datasync:us-east-1:123456789012:agent/agent-01234567890example}}] \
       --subdirectory "{{/path/to/my/data}}"
   ```

1. For the `--name-nodes` parameter, specify the hostname or IP address of your HDFS cluster's primary NameNode and the TCP port that the NameNode is listening on.

1. For the `--authentication-type` parameter, specify the type of authentication to use when connecting to the Hadoop cluster. You can specify `SIMPLE` or `KERBEROS`.

   If you use `SIMPLE` authentication, use the `--simple-user` parameter to specify the user name of the user. If you use `KERBEROS` authentication, use the `--kerberos-principal`, `--kerberos-keytab`, and `--kerberos-krb5-conf` parameters. For more information, see [create-location-hdfs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/create-location-hdfs.html).

1. For the `--agent-arns` parameter, specify the ARN of the DataSync agent that can connect to your HDFS cluster.

   You can choose more than one agent. For more information, see [Using multiple DataSync agents](do-i-need-datasync-agent.md#multiple-agents).

1. (Optional) For the `--subdirectory` parameter, specify a folder on your HDFS cluster that you want DataSync to use for the data transfer.

   If your HDFS location is a source, DataSync copies the files in this folder to the destination. If your location is a destination, DataSync writes files to this folder.

1. Run the `create-location-hdfs` command.

   If the command is successful, you get a response that shows you the ARN of the location that you created. For example:

   ```
   {
       "arn:aws:datasync:us-east-1:123456789012:location/loc-01234567890example"
   }
   ```