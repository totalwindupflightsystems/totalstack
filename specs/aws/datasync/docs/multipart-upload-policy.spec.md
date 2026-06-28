---
id: "@specs/aws/datasync/docs/multipart-upload-policy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Troubleshooting S3 storage costs with DataSync"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Troubleshooting S3 storage costs with DataSync

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/multipart-upload-policy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Troubleshooting higher than expected S3 storage costs with DataSync
<a name="multipart-upload-policy"></a>

If your Amazon S3 storage costs are higher than you thought they would be following an AWS DataSync transfer, it might be due to one or more of the following reasons:
+ When transferring to or from S3 buckets, you incur costs related to S3 API requests made by DataSync.
+ DataSync uses the Amazon S3 multipart upload feature to upload objects to S3 buckets. This approach can result in unexpected storage charges for uploads that don't complete successfully.
+ DataSync copies object tags from source and destination objects when **Copy object tags** is enabled on the console or `ObjectTags` is set to `PRESERVE`. Copying of these object tags can incur S3 API request costs. 
+ Object versioning might be enabled on your S3 bucket. Object versioning results in Amazon S3 storing multiple copies of objects that have the same name.

**Actions to take**  
In these cases, you can take the following steps:
+ Make sure you understand how DataSync uses S3 requests and how they might be affecting your storage costs. For more information, see [Evaluating S3 request costs when using DataSync](create-s3-location.md#create-s3-location-s3-requests).
+ If the issue is related to multipart uploads, configure a policy for multipart uploads for your S3 bucket to clean up incomplete multipart uploads to reduce storage cost. For more information, see the AWS blog post [S3 Lifecycle Management Update - Support for Multipart Uploads and Delete Markers](https://aws.amazon.com/blogs/aws/s3-lifecycle-management-update-support-for-multipart-uploads-and-delete-markers/). 
+ If the issue is related to copying object tags and you don't need object tags, clear the **Copy object tags** checkbox in the DataSync console or set `ObjectTags` to `None` when creating, starting, or updating a task.
+ If the issue is related to object versioning, disable object versioning on your S3 bucket.

f you need additional help, contact [AWS Support Center](https://console.aws.amazon.com/support/home#/).