---
id: "@specs/aws/lightsail/docs/object-storage-s3-actions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS API actions for Lightsail objects"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# API actions for Lightsail objects

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/object-storage-s3-actions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# API actions for Lightsail objects
<a name="object-storage-s3-actions"></a>

Use the following API actions for Amazon Simple Storage Service (Amazon S3) to manage buckets and objects in the Amazon Lightsail object storage service. Choose the name of an API action to view the documentation for it in the *Amazon S3 API reference*. For more information about buckets in Lightsail, see [Store and manage data with Lightsail object storage buckets](buckets-in-amazon-lightsail.md).

**Uploading files to buckets**
+ [PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html) - Adds a file to a bucket. For more information, see [Uploading files to a bucket in Amazon Lightsail](amazon-lightsail-uploading-files-to-a-bucket.md).

**Uploading objects to buckets using multipart upload**
+ [CreateMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateMultipartUpload.html) - Initiates a multipart upload and returns an upload ID. For more information, see [Uploading files to a bucket using multipart upload in Amazon Lightsail](amazon-lightsail-uploading-files-to-a-bucket-using-multipart-upload.md).
+ [UploadPart](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPart.html) - Uploads a part in a specific multipart upload. For more information, see [Uploading files to a bucket using multipart upload in Amazon Lightsail](amazon-lightsail-uploading-files-to-a-bucket-using-multipart-upload.md).
+ [ListParts](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListParts.html) - Lists the parts that have been uploaded for a specific multipart upload. For more information, see [Uploading files to a bucket using multipart upload in Amazon Lightsail](amazon-lightsail-uploading-files-to-a-bucket-using-multipart-upload.md).
+ [CompleteMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CompleteMultipartUpload.html) - Completes a multipart upload by assembling previously uploaded parts. For more information, see [Uploading files to a bucket using multipart upload in Amazon Lightsail](amazon-lightsail-uploading-files-to-a-bucket-using-multipart-upload.md).
+ [ListMultipartUploads](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListMultipartUploads.html) - Lists all in-progress multipart uploads for a bucket. For more information, see [Uploading files to a bucket using multipart upload in Amazon Lightsail](amazon-lightsail-uploading-files-to-a-bucket-using-multipart-upload.md).
+ [AbortMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_AbortMultipartUpload.html) - Stops a multipart upload. For more information, see [Uploading files to a bucket using multipart upload in Amazon Lightsail](amazon-lightsail-uploading-files-to-a-bucket-using-multipart-upload.md).

**Listing objects and object details**
+ [ListObjectsV2](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectsV2.html) - Returns a list of the objects (up to 1,000 in each request) in a bucket. For more information, see [Viewing objects in a bucket in Amazon Lightsail](amazon-lightsail-viewing-objects-in-a-bucket.md).
+ [HeadObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadObject.html) - Returns metadata from an object without returning the object itself. This action is useful if you're only interested in an object's metadata. For more information, see [Viewing objects in a bucket in Amazon Lightsail](amazon-lightsail-viewing-objects-in-a-bucket.md).
+ [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html) - Downloads an object from a bucket. For more information, see [Downloading objects from a bucket in Amazon Lightsail](amazon-lightsail-downloading-bucket-objects.md).
+ [GetObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectTagging.html) - Returns the tags of an object. For more information, see [Tagging objects in a bucket in Amazon Lightsail](amazon-lightsail-tagging-bucket-objects.md).
+ [ListObjectVersions](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectVersions.html) - Returns metadata about all versions of objects in a bucket. For more information, see [Enabling and suspending object versioning in a bucket in Amazon Lightsail](amazon-lightsail-managing-bucket-object-versioning.md).

**Copying and moving objects**
+ [CopyObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html) - Creates a copy of an object. For more information, see [Copying or moving objects in a bucket in Amazon Lightsail](amazon-lightsail-copying-moving-bucket-objects.md).

**Editing individual object permissions**
+ [PutObjectAcl](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectAcl.html) - Sets the access control list (ACL) permissions for an object, which is how you can control the access permissions for an individual object. For more information, see [Configuring access permissions for individual objects in a bucket in Amazon Lightsail](amazon-lightsail-configuring-individual-object-access.md).
+ [GetObjectAcl](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAcl.html) - Returns the access control list (ACL) set for an object, which controls the access permissions for the individual object. For more information, see [Configuring access permissions for individual objects in a bucket in Amazon Lightsail](amazon-lightsail-configuring-individual-object-access.md).

**Editing object tags**
+ [PutObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectTagging.html) - Sets the supplied tag to an object. For more information, see [Tagging objects in a bucket in Amazon Lightsail](amazon-lightsail-tagging-bucket-objects.md).

**Listing and restoring object versions**
+ [ListObjectVersions](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectVersions.html) - Returns metadata about all versions of objects in a bucket. For more information, see [Enabling and suspending object versioning in a bucket in Amazon Lightsail](amazon-lightsail-managing-bucket-object-versioning.md) and [Restoring previous versions of objects in a bucket in Amazon Lightsail](amazon-lightsail-restoring-bucket-object-versions.md).
+ [CopyObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html) - Creates a copy of an object in a bucket, including previous versions of an object. To restore an object version, use the `CopyObject` action to copy a previous version of an object and make it the latest version. For more information, see [Restoring previous versions of objects in a bucket in Amazon Lightsail](amazon-lightsail-restoring-bucket-object-versions.md).
+ [DeleteObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObject.html) - Deletes an object from a bucket, including previous versions of an object. For more information, see [Deleting objects in a bucket in Amazon Lightsail](amazon-lightsail-deleting-bucket-objects.md).

**Deleting objects**
+ [DeleteObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObject.html) - Deletes an object from a bucket. For more information, see [Deleting objects in a bucket in Amazon Lightsail](amazon-lightsail-deleting-bucket-objects.md).
+ [DeleteObjects](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjects.html) - Deletes multiple objects from a bucket using a single request. For more information, see [Deleting objects in a bucket in Amazon Lightsail](amazon-lightsail-deleting-bucket-objects.md).