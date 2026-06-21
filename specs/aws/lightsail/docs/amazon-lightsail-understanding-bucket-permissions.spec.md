---
id: "@specs/aws/lightsail/docs/amazon-lightsail-understanding-bucket-permissions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Bucket permissions"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Bucket permissions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/amazon-lightsail-understanding-bucket-permissions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Control access to Lightsail buckets and objects
<a name="amazon-lightsail-understanding-bucket-permissions"></a>

By default, all Amazon Lightsail object storage resources—buckets and objects—are private. This means that only the bucket owner, the Lightsail account that created it, can access the bucket and its objects. The bucket owner can optionally grant access to others. You can grant access to a bucket and its objects in the following ways:
+ **Read-only access** – The following options control read-only access to a bucket and its objects through the bucket's URL (for example, `https://amzn-s3-demo-bucket.us-east-1.amazonaws.com/media/sailbot.jpg`).
  + **Bucket access permissions** – Use bucket access permissions to grant access to all objects in a bucket for anyone on the internet. For more information, see [Bucket access permissions](#bucket-access-permissions) later in this guide.
  + **Individual object access permissions** – Use individual object access permissions to grant access to an individual object in a bucket for anyone on the internet. For more information, see [Individual object access permissions](#individual-bucket-object-access-permissions) later in this guide.
  + **Cross-account access** – Use cross-account access to grant access to all objects in a bucket for other AWS accounts. For more information, see [Cross-account access](#cross-account-access) later in this guide.
+ **Read and write access** – The following options control full read and write access to a bucket and its objects. Use these options with the AWS Command Line Interface (AWS CLI), AWS APIs, and AWS SDKs.
  + **Access keys** – Use access keys to grant access to applications or plugins. For more information, see [Access keys](#bucket-access-keys) later in this guide.
  + **Resource access** – Use resource access to grant access to a Lightsail instance. For more information, see [Resource access](#bucket-resource-access) later in this guide.
+ **Amazon Simple Storage Service block public access** – Use the Amazon Simple Storage Service (Amazon S3) account-level block public access feature to centrally limit public access to buckets in Amazon S3 and in Lightsail. Block public access can make all Amazon S3 and Lightsail buckets private regardless of the individual bucket and object permissions that might have been configured. For more information, see [Amazon S3 block public access](#s3-block-public-access) later in this guide.

For more information about buckets, see [Object storage](buckets-in-amazon-lightsail.md). For more information about security best practices, see [Security Best Practices for object storage](amazon-lightsail-bucket-security-best-practices.md).

## Bucket access permissions
<a name="bucket-access-permissions"></a>

Use bucket access permissions to control public (unauthenticated) read-only access to objects in a bucket. You can choose one of the following options when configuring bucket access permissions:
+ **All objects are private** – All objects in the bucket are readable only by you or anyone you give access to. This option does not allow for individual objects to be made public (read-only).
+ **Individual objects can be made public (read-only)** – Objects in the bucket are readable only by you or anyone you give access to, unless you specify an individual object as public (read-only). This option allows for individual objects to be made public (read-only). For more information, see [Individual object access permissions](#individual-bucket-object-access-permissions) later in this guide.
+ **All objects are public (read-only)** – All objects in the bucket are readable by anyone on the internet. All objects in the bucket become readable by anyone on the internet through the URL of the bucket (for example, `https://amzn-s3-demo-bucket.us-east-1.amazonaws.com/media/sailbot.jpg`) when you choose this option.

For more information about configuring bucket access permissions, see [Configure bucket access permissions](amazon-lightsail-configuring-bucket-permissions.md).

## Individual object access permissions
<a name="individual-bucket-object-access-permissions"></a>

Use individual object access permissions to control public (unauthenticated) read-only access to individual objects in a bucket. Individual object access permissions can be configured only when the [Bucket access permissions](#bucket-access-permissions) of a bucket allow for individual objects to be made public (read-only). You can choose one of the following options when configuring access permissions for an individual object:
+ **Private** – The object is readable only by you or anyone you give access to.
+ **Public (read-only)** – The object is readable by anyone on the internet. The individual object becomes readable by anyone on the internet through the URL of the bucket (for example, `https://amzn-s3-demo-bucket.us-east-1.amazonaws.com/media/sailbot.jpg`).

For more information about configuring individual object access permissions, see [Configure access permissions for individual objects in a bucket](amazon-lightsail-configuring-individual-object-access.md).

## Cross-account access
<a name="cross-account-access"></a>

Use cross-account access to grant authenticated read-only access to all objects in a bucket for other AWS accounts and their users. Cross-account access is ideal if you want to share objects with another AWS account. When you grant cross-account access to another AWS account, users in that account have read-only access to objects in a bucket through the URL of the bucket (for example, `https://amzn-s3-demo-bucket.us-east-1.amazonaws.com/media/sailbot.jpg`). You can give access to a maximum of 10 AWS accounts.

For more information about configuring cross-account access, see [Configure cross-account access for a bucket](amazon-lightsail-configuring-bucket-cross-account-access.md).

## Access keys
<a name="bucket-access-keys"></a>

Use access keys to create a set of credentials that grant full read and write access to a bucket and its objects. Access keys consist of an access key ID and a secret access key as a set. You can have a maximum of two access keys per bucket. You can configure access keys on your application so that it can access your bucket and its objects using the AWS APIs, and AWS SDKs. You can also configure access keys on the AWS CLI.

For more information about creating access keys, see [Create access keys for a bucket](amazon-lightsail-creating-bucket-access-keys.md).

## Resource access
<a name="bucket-resource-access"></a>

Use resource access to grant full read and write access to a bucket and its objects for Lightsail instances. With resource access, you don't have to manage credentials like access keys. To grant access to an instance, attach the instance to a bucket in the same AWS Region. To deny access, detach the instance from the bucket. Resource access is ideal if you're configuring an application on your instance to programmatically upload and access files on your bucket. One such use-case is to configure a WordPress instance to store media files on a bucket. For more information, see [Tutorial: Connect a bucket to your WordPress instance](amazon-lightsail-connecting-buckets-to-wordpress.md) and [Tutorial: Use a bucket with a content delivery network distribution](amazon-lightsail-using-distributions-with-buckets.md).

For more information about configuring resource access, see [Configure resource access for a bucket](amazon-lightsail-configuring-bucket-resource-access.md).

## Amazon S3 block public access
<a name="s3-block-public-access"></a>

Use the Amazon S3 block public access feature to centrally limit public access to buckets in Amazon S3 and in Lightsail. Block public access can make all Amazon S3 and Lightsail buckets private regardless of the individual bucket and object permissions that might have been configured. You can use the Amazon S3 console, AWS CLI, AWS SDKs, and REST API to configure block public access settings for all buckets in your account, including those in the Lightsail object storage service. For more information, see [Block public access for buckets](amazon-lightsail-block-public-access-for-buckets.md).