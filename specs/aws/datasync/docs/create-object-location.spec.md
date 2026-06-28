---
id: "@specs/aws/datasync/docs/create-object-location"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Configuring transfers with an object storage system"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Configuring transfers with an object storage system

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/create-object-location
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Configuring DataSync transfers with an object storage system
<a name="create-object-location"></a>

With AWS DataSync, you can transfer data between your object storage system and one of the following AWS storage services using Basic mode tasks:
+ [Amazon S3](create-s3-location.md)
+ [Amazon EFS](create-efs-location.md)
+ [Amazon FSx for Windows File Server](create-fsx-location.md)
+ [Amazon FSx for Lustre](create-lustre-location.md)
+ [Amazon FSx for OpenZFS](create-openzfs-location.md)
+ [Amazon FSx for NetApp ONTAP](create-ontap-location.md)

To set up this kind of transfer, you create a [location](how-datasync-transfer-works.md#sync-locations) for your object storage system. You can use this location as a transfer source or destination. Transferring data to or from your on-premises object storage requires a Basic mode DataSync agent.

## Prerequisites
<a name="create-object-location-prerequisites"></a>

Your object storage system must be compatible with the following [Amazon S3 API operations](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Operations.html) for DataSync to connect to it:
+ `AbortMultipartUpload`
+ `CompleteMultipartUpload`
+ `CopyObject`
+ `CreateMultipartUpload`
+ `DeleteObject`
+ `DeleteObjects`
+ `DeleteObjectTagging`
+ `GetBucketLocation`
+ `GetObject`
+ `GetObjectTagging`
+ `HeadBucket`
+ `HeadObject`
+ `ListObjectsV2`
+ `PutObject`
+ `PutObjectTagging`
+ `UploadPart`

## Creating your object storage transfer location
<a name="create-object-location-how-to"></a>

Before you begin, you need an object storage system that you plan to transfer data to or from.

### Using the DataSync console
<a name="create-object-location-how-to-console"></a>

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/).

1. In the left navigation pane, expand **Data transfer**, then choose **Locations** and **Create location**.

1. For **Location type**, choose **Object storage**.

   You configure this location as a source or destination later.

1. For **Server**, provide the domain name or IP address of the object storage server. 

1. For **Bucket name**, enter the name of the object storage bucket involved in the transfer.

1. For **Folder**, enter an object prefix.

   DataSync only copies objects with this prefix. 

1. If your transfer requires an agent, choose **Use agents**, then choose the DataSync agent that connects to your object storage system.

   Some transfers don't require agents. In other scenarios, you might want to use more than one agent. For more information, see [Situations when you don't need a DataSync agent](do-i-need-datasync-agent.md#when-agent-not-required) and [Using multiple DataSync agents](do-i-need-datasync-agent.md#multiple-agents).

1. To configure the connection to the object storage server, expand **Additional settings** and do the following:

   1. For **Server protocol**, choose **HTTP** or **HTTPS**.

   1. For **Server port**, use a default port (**80** for HTTP or **443** for HTTPS) or specify a custom port if needed.

   1. For **Certificate**, if your object storage system uses a private or self-signed certificate authority (CA), select **Choose file** and specify a single `.pem` file with a full certificate chain.

      The certificate chain might include:
      + The object storage system's certificate
      + All intermediate certificates (if there are any)
      + The root certificate of the signing CA

      You can concatenate your certificates into a `.pem` file (which can be up to 32768 bytes before base64 encoding). The following example `cat` command creates an `{{object_storage_certificates}}.pem` file that includes three certificates:

      ```
      cat {{object_server_certificate}}.pem {{intermediate_certificate}}.pem {{ca_root_certificate}}.pem > {{object_storage_certificates}}.pem
      ```

1. If the object storage server requires credentials for access, select **Requires credentials** and enter the **Access key** you use to access the bucket. Then either enter the **Secret key** directly, or specify an AWS Secrets Manager secret that contains the key. For more information, see [Providing credentials for storage locations](https://docs.aws.amazon.com/datasync/latest/userguide/location-credentials.html).

   The access key and secret key can be a user name and password, respectively.

1. (Optional) Choose **Add tag** to tag your object storage location.

   *Tags* are key-value pairs that help you manage, filter, and search for your locations. We recommend creating at least a name tag for your location. 

1. Choose **Create location**.

### Using the AWS CLI
<a name="create-location-object-cli"></a>

1. Copy the following `create-location-object-storage` command:

   ```
   aws datasync create-location-object-storage \
       --server-hostname {{object-storage-server.example.com}} \
       --bucket-name {{your-bucket}} \
       --agent-arns arn:aws:datasync:{{us-east-1}}:{{123456789012}}:agent/agent-{{01234567890deadfb}}
   ```

1. Specify the following required parameters in the command:
   + `--server-hostname` – Specify the domain name or IP address of your object storage server.
   + `--bucket-name` – Specify the name of the bucket on your object storage server that you're transferring to or from.

1. (Optional) Add any of the following parameters to the command:
   + `--agent-arns` – Specify the DataSync agents that you want to connect to your object storage server.
   + `--server-port` – Specifies the port that your object storage server accepts inbound network traffic on (for example, port `443`).
   + `--server-protocol` – Specifies the protocol (`HTTP` or `HTTPS`) which your object storage server uses to communicate.
   + `--access-key` – Specifies the access key (for example, a user name) if credentials are required to authenticate with the object storage server.
   + `--secret-key` – Specifies the secret key (for example, a password) if credentials are required to authenticate with the object storage server.

     You can also provide additional parameters for securing your keys using AWS Secrets Manager. For more information, see [Providing credentials for storage locations](https://docs.aws.amazon.com/datasync/latest/userguide/location-credentials.html).
   + `--server-certificate` – Specifies a certificate chain for DataSync to authenticate with your object storage system if the system uses a private or self-signed certificate authority (CA). You must specify a single `.pem` file with a full certificate chain (for example, `file:///home/user/.ssh/object_storage_certificates.pem`).

     The certificate chain might include:
     + The object storage system's certificate
     + All intermediate certificates (if there are any)
     + The root certificate of the signing CA

     You can concatenate your certificates into a `.pem` file (which can be up to 32768 bytes before base64 encoding). The following example `cat` command creates an `{{object_storage_certificates}}.pem` file that includes three certificates:

     ```
     cat {{object_server_certificate}}.pem {{intermediate_certificate}}.pem {{ca_root_certificate}}.pem > {{object_storage_certificates}}.pem
     ```
   + `--subdirectory` – Specifies the object prefix for your object storage server.

     DataSync only copies objects with this prefix. 
   + `--tags` – Specifies the key-value pair that represents a tag that you want to add to the location resource.

     Tags can help you manage, filter, and search for your resources. We recommend creating a name tag for your location.

1. Run the `create-location-object-storage` command.

   You get a response that shows you the location ARN that you just created.

   ```
   {
       "LocationArn": "arn:aws:datasync:us-east-1:123456789012:location/loc-01234567890abcdef"
   }
   ```