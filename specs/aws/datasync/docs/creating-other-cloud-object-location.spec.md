---
id: "@specs/aws/datasync/docs/creating-other-cloud-object-location"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Configuring transfers with other cloud object storage"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Configuring transfers with other cloud object storage

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/creating-other-cloud-object-location
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Configuring transfers with other cloud object storage
<a name="creating-other-cloud-object-location"></a>

With AWS DataSync, you can transfer data between [AWS storage services](transferring-aws-storage.md) and the following cloud object storage providers:
+ [https://docs.wasabi.com/](https://docs.wasabi.com/)
+ [https://docs.digitalocean.com/](https://docs.digitalocean.com/)
+ [https://docs.oracle.com/iaas/Content/home.htm](https://docs.oracle.com/iaas/Content/home.htm)
+ [https://developers.cloudflare.com/r2/](https://developers.cloudflare.com/r2/)
+ [https://www.backblaze.com/docs/cloud-storage](https://www.backblaze.com/docs/cloud-storage)
+ [https://guide.ncloud-docs.com/docs/](https://guide.ncloud-docs.com/docs/)
+ [https://www.alibabacloud.com/help/en/oss/product-overview/what-is-oss](https://www.alibabacloud.com/help/en/oss/product-overview/what-is-oss)
+ [https://cloud.ibm.com/docs/cloud-object-storage?topic=cloud-object-storage-getting-started-cloud-object-storage](https://cloud.ibm.com/docs/cloud-object-storage?topic=cloud-object-storage-getting-started-cloud-object-storage)
+ [https://help.lyvecloud.seagate.com/en/product-features.html](https://help.lyvecloud.seagate.com/en/product-features.html)

A DataSync agent is required only when transferring data between storage systems in other clouds and Amazon EFS or Amazon FSx, or when using **Basic** mode tasks. You don't need an agent to transfer data between storage systems in other clouds and Amazon S3 using **Enhanced** mode.

Regardless of whether you use an agent, you must also create a transfer [location](how-datasync-transfer-works.md#sync-locations) for your cloud object storage (specifically an **Object storage** location). DataSync can use this location as a source or destination for your transfer.

## Providing DataSync access to your other cloud object storage
<a name="other-cloud-access"></a>

How DataSync accesses your cloud object storage depends on several factors, including whether your storage is compatible with the Amazon S3 API and the permissions and credentials that DataSync needs to access your storage.

**Topics**
+ [Amazon S3 API compatibility](#other-cloud-s3-compatibility)
+ [Storage permissions and endpoints](#other-cloud-permissions)
+ [Storage credentials](#other-cloud-credentials)

### Amazon S3 API compatibility
<a name="other-cloud-s3-compatibility"></a>

Your cloud object storage must be compatible with the following [Amazon S3 API operations](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Operations.html) for DataSync to connect to it:
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

### Storage permissions and endpoints
<a name="other-cloud-permissions"></a>

You must configure the permissions that allow DataSync to access your cloud object storage. If your object storage is a source location, DataSync needs read and list permissions for the bucket that you're transferring data from. If your object storage is a destination location, DataSync needs read, list, write, and delete permissions for the bucket.

DataSync also needs an endpoint (or server) to connect to your storage. The following table describes the endpoints that DataSync can use to access other cloud object storage:


| Other cloud provider | Endpoint | 
| --- | --- | 
| Wasabi Cloud Storage | `S3.{{region}}.wasabisys.com` | 
| DigitalOcean Spaces | `{{region}}.digitaloceanspaces.com` | 
| Oracle Cloud Infrastructure Object Storage | `{{namespace}}.compat.objectstorage.{{region}}.oraclecloud.com` | 
| Cloudflare R2 Storage | `{{account-id}}.r2.cloudflarestorage.com` | 
| Backblaze B2 Cloud Storage | `S3.{{region}}.backblazeb2.com` | 
| NAVER Cloud Object Storage | `{{region}}.object.ncloudstorage.com` (most regions) | 
| Alibaba Cloud Object Storage Service | `{{region}}.aliyuncs.com` | 
| IBM Cloud Object Storage | `s3.{{region}}.cloud-object-storage.appdomain.cloud` | 
| Seagate Lyve Cloud | `s3.{{region}}.lyvecloud.seagate.com` | 

**Important**  
For details on how to configure bucket permissions and updated information on storage endpoints, see your cloud provider's documentation.

### Storage credentials
<a name="other-cloud-credentials"></a>

DataSync also needs the credentials to access the object storage bucket involved in your transfer. This might be an access key and secret key or something similar depending on how your cloud storage provider refers to these credentials.

For more information, see your cloud provider's documentation.

## Considerations when transferring from other cloud object storage
<a name="other-cloud-considerations"></a>

When planning to transfer objects to or from another cloud storage provider by using DataSync, there are some things to keep in mind.

**Topics**
+ [Costs](#other-cloud-considerations-costs)
+ [Storage classes](#other-cloud-considerations-storage-classes)
+ [Object tags](#other-cloud-considerations-object-tags)
+ [Transferring to Amazon S3](#other-cloud-considerations-s3)

### Costs
<a name="other-cloud-considerations-costs"></a>

The fees associated with moving data in and out of another cloud storage provider can include:
+ Running an [Amazon EC2](https://aws.amazon.com/ec2/pricing/) instance for your DataSync agent
+ Transferring the data by using [DataSync](https://aws.amazon.com/datasync/pricing/), including request charges related to your cloud object storage and [Amazon S3](create-s3-location.md#create-s3-location-s3-requests) (if S3 is your transfer destination)
+ Transferring data in or out of your cloud storage (check your cloud provider's pricing)
+ Storing data in an [AWS storage service](transferring-aws-storage.md) supported by DataSync
+ Storing data in another cloud provider (check your cloud provider's pricing)

### Storage classes
<a name="other-cloud-considerations-storage-classes"></a>

Some cloud storage providers have storage classes (similar to [Amazon S3](create-s3-location.md#using-storage-classes)) which DataSync can't read without being restored first. For example, Oracle Cloud Infrastructure Object Storage has an archive storage class. You need to restore objects in that storage class before DataSync can transfer them. For more information, see your cloud provider's documentation.

### Object tags
<a name="other-cloud-considerations-object-tags"></a>

Not all cloud providers support object tags. The ones that do might not allow querying tags through the Amazon S3 API. In either situation, your DataSync transfer task might fail if you try to copy object tags.

You can avoid this by clearing the **Copy object tags** checkbox in the DataSync console when creating, starting, or updating your task.

### Transferring to Amazon S3
<a name="other-cloud-considerations-s3"></a>

When transferring to Amazon S3, DataSync can't transfer objects larger than 5 TB. DataSync also can only copy object metadata up to 2 KB.

## Creating your DataSync agent
<a name="other-cloud-creating-agent"></a>

A DataSync agent is required only when transferring data between storage systems in other clouds and Amazon EFS or Amazon FSx, or when using **Basic** mode tasks. You don't need an agent to transfer data between storage systems in other clouds and Amazon S3 using **Enhanced** mode. This section desribes how to deploy and activate an agent on an Amazon EC2 instance in your virtual private cloud (VPC) in AWS.

**To create an Amazon EC2 agent**

1. [Deploy an Amazon EC2 agent](deploy-agents.md#ec2-deploy-agent).

1. [Choose a service endpoint](choose-service-endpoint.md) that the agent uses to communicate with AWS.

   In this situation, we recommend using a VPC service endpoint.

1. Configure your network to work with [VPC service endpoints](datasync-network.md#using-vpc-endpoint).

1. [Activate the agent](activate-agent.md).

## Creating a transfer location for your other cloud object storage
<a name="creating-other-cloud-location-how-to"></a>

You can configure DataSync to use your cloud object storage as a source or destination location.

**Before you begin**  
Make sure that you know [how DataSync accesses your cloud object storage](#other-cloud-access). You also need a [DataSync agent](#other-cloud-creating-agent) that can connect to your cloud object storage.

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/).

1. In the left navigation pane, expand **Data transfer**, then choose **Locations** and **Create location**.

1. For **Location type**, choose **Object storage**.

1. For **Server**, enter the [endpoint](#other-cloud-permissions) that DataSync can use to access your cloud object storage:
   + **Wasabi Cloud Storage** – `S3.{{region}}.wasabisys.com`
   + **DigitalOcean Spaces** – `{{region}}.digitaloceanspaces.com`
   + **Oracle Cloud Infrastructure Object Storage** – `{{namespace}}.compat.objectstorage.{{region}}.oraclecloud.com`
   + **Cloudflare R2 Storage** – `{{account-id}}.r2.cloudflarestorage.com`
   + **Backblaze B2 Cloud Storage** – `S3.{{region}}.backblazeb2.com`
   + **NAVER Cloud Object Storage** – `{{region}}.object.ncloudstorage.com` (most regions)
   + **Alibaba Cloud Object Storage Service** – `{{region}}.aliyuncs.com`
   + **IBM Cloud Object Storage** – `s3.{{region}}.cloud-object-storage.appdomain.cloud`
   + **Seagate Lyve Cloud** – `s3.{{region}}.lyvecloud.seagate.com`

1. For **Bucket name**, enter the name of the object storage bucket that you're transferring data to or from.

1. For **Folder**, enter an object preﬁx. DataSync only transfers objects with this prefix.

1. If your transfer requires an agent, choose **Use agents**, then choose the DataSync agent that can connect with your cloud object storage.

1. Expand **Additional settings**. For **Server protocol**, choose **HTTPS**. For **Server port**, choose **443**.

1. Scroll down to the **Authentication** section. Make sure that the **Requires credentials** check box is selected, and then provide DataSync your [storage credentials](#other-cloud-credentials).
   + For **Access key**, enter the ID to access your cloud object storage.
   + For **Secret key**, provide the secret key to access your cloud object storage. You can either enter the key directly, or specify an AWS Secrets Manager secret that contains the key. For more information, see [Providing credentials for storage locations](https://docs.aws.amazon.com/datasync/latest/userguide/location-credentials.html).

1. (Optional) Enter values for the **Key** and **Value** fields to tag the location.

   Tags help you manage, filter, and search for your AWS resources. We recommend creating at least a name tag for your location. 

1. Choose **Create location**.

## Next steps
<a name="other-cloud-location-next-steps"></a>

After you finish creating a DataSync location for your cloud object storage, you can continue setting up your transfer. Here are some next steps to consider:

1. If you haven't already, [create another location](transferring-aws-storage.md) where you plan to transfer your data to or from in AWS.

1. Learn how DataSync [handles metadata and special files](metadata-copied.md) for object storage locations.

1. Configure how your data gets transferred. For example, maybe you only want to [transfer a subset of your data](filtering.md).
**Important**  
Make sure that you configure how DataSync copies object tags correctly. For more information, see considerations with [object tags](#other-cloud-considerations-object-tags).

1. [Start your transfer](run-task.md). 

 