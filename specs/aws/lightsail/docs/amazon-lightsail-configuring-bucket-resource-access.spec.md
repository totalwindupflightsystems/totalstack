---
id: "@specs/aws/lightsail/docs/amazon-lightsail-configuring-bucket-resource-access"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Bucket resource access"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Bucket resource access

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/amazon-lightsail-configuring-bucket-resource-access
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Control access to Lightsail buckets for instances
<a name="amazon-lightsail-configuring-bucket-resource-access"></a>

Attach an Amazon Lightsail instance to a Lightsail bucket to give it full programmatic access to the bucket and its objects. When you attach instances to buckets, you don't have to manage credentials like access keys. The instances and buckets that you attach must be in the same AWS Region. You cannot attach instances to buckets that are in a different Region.

Resource access is ideal if you're configuring software or a plugin on your instance to upload files directly to your bucket. For example, if you want to configure a WordPress instance to store media files on a bucket. For more information, see [Tutorial: Connect a bucket to your WordPress instance](amazon-lightsail-connecting-buckets-to-wordpress.md#amazon-lightsail-connecting-buckets-to-wordpress.title).

For more information about permission options, see [Bucket permissions](amazon-lightsail-understanding-bucket-permissions.md). For more information about security best practices, see [Security Best Practices for object storage](amazon-lightsail-bucket-security-best-practices.md). For more information about buckets, see [Object storage](buckets-in-amazon-lightsail.md).

## Configure resource access for a bucket
<a name="configure-bucket-resource-access"></a>

Complete the following procedure to configure resource access for a bucket.

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Storage**.

1. Choose the name of the bucket for which you want to configure resource access.

1. Choose the **Permissions** tab.

   The **Resource access** section of the page displays the instances currently attached to the bucket, if any.

1. Choose **Attach instance** to attach an instance to the bucket.

1. In the **Select an instance** dropdown menu, select the instance that you want to attach to the bucket.
**Note**  
You can attach instances that are in a running or stopped state only. Additionally, you can attach only instances that are in the same AWS Region as the bucket.

1. Choose **Attach** to attach the instance. Otherwise, choose **Cancel**.

   The instance has full access to the bucket and its objects after it's attached. You can configure software or a plugin on your instance to programmatically upload and access files on your bucket. For example, if you want to configure a WordPress instance to store media files on a bucket. For more information, see [Tutorial: Connect a bucket to your WordPress instance](amazon-lightsail-connecting-buckets-to-wordpress.md).