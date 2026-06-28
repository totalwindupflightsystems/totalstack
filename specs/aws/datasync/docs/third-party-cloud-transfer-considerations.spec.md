---
id: "@specs/aws/datasync/docs/third-party-cloud-transfer-considerations"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Planning transfers to or from third-party cloud storage systems"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Planning transfers to or from third-party cloud storage systems

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/third-party-cloud-transfer-considerations
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Planning transfers to or from third-party cloud storage systems
<a name="third-party-cloud-transfer-considerations"></a>

When planning cross-cloud data transfers, consider the following:
+ **Using an agent:** An agent is only required to access storage in other clouds when using Basic mode tasks. [Enhanced mode tasks](https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html) do not require an agent. If you decide to use an agent, you can deploy it as an [Amazon EC2 instance](https://docs.aws.amazon.com/datasync/latest/userguide/deploy-agents.html#ec2-deploy-agent) when transferring from a cloud providers' S3-compatible object storage, or as a Google Compute Engine or Azure Virtual Machine for transfers from those specific storage services, respectively. When transferring from filesystems in Google and Azure, we recommend deploying the agent as a Google or Azure VM so that the agent is as close to the filesystem as possible. Additionally, DataSync compresses the data from the agent to AWS, which can help reduce egress costs. DataSync provides a list of [validated cloud locations](https://docs.aws.amazon.com/datasync/latest/userguide/creating-other-cloud-object-location.html) that provide the required [Amazon S3 API compatibility](https://docs.aws.amazon.com/datasync/latest/userguide/creating-other-cloud-object-location.html#other-cloud-access).
+ **The other cloud’s object storage endpoint:** The storage endpoint for a third-party cloud provider is typically region or account specific. The regional endpoint is used as the server in the DataSync object storage location, together with a specified bucket name.
+ **Storage classes of the source objects:** Like Amazon S3, some cloud providers support an archive tier that requires a restore before being able to access the archived objects. For example, objects in the Azure Blob archive tier must be retrieved for standard access prior to a data transfer. Objects in the Google Cloud Storage archive tier can be accessed immediately and do not require restore, but there are retrieval costs associated with direct archive tier access. Review your cross-cloud storage class documentation to determine access requirements and retrieval fees prior to beginning your data transfer. For more information about restoring archived objects in Amazon S3, see [Restoring an archived object](https://docs.aws.amazon.com/AmazonS3/latest/userguide/restoring-objects.html) in the *Amazon Simple Storage Service User Guide*.
+ **Object storage access:** Transferring data between third-party cloud providers requires access to the other cloud's object storage in the form of authentication keys. For example, to provide access to Google Cloud Storage, you configure a DataSync object storage location that connects to the [Google Cloud Storage XML API](https://cloud.google.com/storage/docs/xml-api/overview) and authenticates using a [Hash-based Message Authentication Code (HMAC) key](https://docs.aws.amazon.com/datasync/latest/userguide/tutorial_transfer-google-cloud-storage.html#transfer-google-cloud-storage-create-hmac-key) for your service account. For Azure Blob storage, you configure a dedicated [Azure Blob DataSync location](https://docs.aws.amazon.com/datasync/latest/userguide/creating-azure-blob-location.html#creating-azure-blob-location-how-to) that authenticates using [SAS tokens](https://docs.aws.amazon.com/datasync/latest/userguide/creating-azure-blob-location.html#azure-blob-access). DataSync uses AWS Secrets Manager to securely store your object storage credentials. For more information, see [Securing storage location credentials](https://docs.aws.amazon.com/datasync/latest/userguide/location-credentials.html).
+ **Object tag support:**
  + Unlike Amazon S3, not all cloud providers support [object tags](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-tagging.html). DataSync tasks can fail while attempting to read tags from the source location if the cloud provider does not support object tags through the Amazon S3 API, or if the credentials you provide are insufficient to retrieve the tags. DataSync provides a task option to turn off [reading and copying object tags](https://docs.aws.amazon.com/datasync/latest/userguide/API_Options.html#DataSync-Type-Options-ObjectTags) during a transfer if object tags are not supported, or you don't want to retain the tags. Review your cloud provider documentation to determine if object tags are supported, and verify your transfer task's object tag settings before initiating the transfer.
  + You can use the Amazon S3 API to check whether a cloud provider will return a `get-object-tagging` request. For more information, see [get-object-tagging](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-object-tagging.html) in the *AWS CLI Command Reference*.

    A cloud provider that supports object tags will return a response similar to the following example:

    ```
    aws s3api get-object-tagging --bucket BUCKET_NAME --endpoint- url=https://BUCKET_ENDPOINT --key prefix/file1
                                        
    {
    
        "TagSet": []
    
    }
    ```

    A cloud provider that doesn’t support `get-object-tagging` will return the following message:

    ```
    aws s3api get-object-tagging --bucket BUCKET_NAME --endpoint- url=https://BUCKET_ENDPOINT --key prefix/file1
    
    An error occurred (OperationNotSupported) when calling the GetObjectTagging operation: The operation is not supported for this resource
    ```
+ **Associated costs for requests and data egress:** Transferring data from cloud object storage has [request and egress costs](https://docs.aws.amazon.com/datasync/latest/userguide/creating-other-cloud-object-location.html#other-cloud-considerations-costs) associated with reading data and data transfer out. Request charges vary between cloud providers and between storage classes where applicable. Consult your cloud provider documentation regarding specific costs for requests relative to the storage class you plan to read from. For an overview of request charges that DataSync makes for data transfers, see [Evaluating S3 request costs when using DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html#create-s3-location-s3-requests) and [AWS DataSync pricing](https://aws.amazon.com/datasync/pricing/). Transferring data out of specific cloud providers results in egress charges. Data transfer costs vary between cloud providers and are also dependent on the region where the data is stored.
+ **Object storage request rates:** Cloud providers have various performance and request rate characteristics for their object storage platforms. Review your other cloud provider's request rates and determine where the request limits are applied. Plan ahead for highly parallelized transfers consisting of multiple agents, where specific partitioning or performance increases might be required.

  Amazon S3 has documented request rates that you can build your solution around. Amazon S3 request rates are per partitioned prefix and are scalable across multiple prefixes. For more information, see [Best practices design patterns: optimizing Amazon S3 performance](https://docs.aws.amazon.com/AmazonS3/latest/userguide/optimizing-performance.html) in the *Amazon Simple Storage Service User Guide*.