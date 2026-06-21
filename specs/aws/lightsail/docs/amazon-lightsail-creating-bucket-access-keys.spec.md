---
id: "@specs/aws/lightsail/docs/amazon-lightsail-creating-bucket-access-keys"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Create access keys"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Create access keys

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/amazon-lightsail-creating-bucket-access-keys
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Create Lightsail object storage bucket access keys
<a name="amazon-lightsail-creating-bucket-access-keys"></a>

You can use access keys to create a set of credentials that grant full access to a bucket and its objects. Access keys consist of an access key ID and a secret access key as a set. The secret access key is visible only when you create it. When you configure access keys on your software or plugin, it can have full read and write access to a bucket using the AWS APIs, and AWS SDKs. You can also configure access keys on the AWS CLI.

**Important**  
Although you can have two access keys per bucket, we recommend that you only create one bucket access key at a time. We also recommend that you periodically rotate your keys and take inventory of your existing keys. If your secret access key is copied, lost, or becomes compromised, you should delete your access key and create a new one. For more information on the best practices for rotating your bucket access keys, see [Rotate bucket access keys](amazon-lightsail-bucket-security-best-practices.md#bucket-security-best-practices-rotate-bucket-access-keys).

For more information about permission options, see [Bucket permissions](amazon-lightsail-understanding-bucket-permissions.md). For more information about buckets, see [Object storage](buckets-in-amazon-lightsail.md).

## Create access keys for a bucket
<a name="create-bucket-access-keys"></a>

Complete the following procedure to create access keys for a bucket.

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Storage**.

1. Choose the name of the bucket for which you want to configure access permissions.

1. Choose the **Permissions** tab.

   The **Access keys** section of the page displays the existing access keys for the bucket, if any.

1. Choose **Create access key** to create a new access key for the bucket.

1. In the prompt that appears, choose **Yes, create** to confirm that you want to create a new access key. Otherwise, choose **No, cancel**.

1. In the success prompt that appears, make a note of the access key ID.

1. Choose **Show secret access key** to view the secret access key, and make a note of it. The secret access key will not be shown again.
**Important**  
Store your access key ID and secret access key in a secure location. If it becomes compromised, you should delete it and create a new one. For more information, see [Delete access keys for a Lightsail object storage bucket](amazon-lightsail-deleting-bucket-access-keys.md).

1. Choose **Continue** to finish.

   The new access key is listed in the **Access keys** section of the page. If your access key becomes compromised, or lost, delete it and create a new one.
**Note**  
The **Last used** column displayed next to each access key identifies when the key was last used. A dash is displayed when the key has not been used. Expand the access key node to view the service and AWS Region where the key was last used.