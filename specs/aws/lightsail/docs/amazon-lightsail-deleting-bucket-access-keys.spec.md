---
id: "@specs/aws/lightsail/docs/amazon-lightsail-deleting-bucket-access-keys"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Delete access keys"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Delete access keys

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/amazon-lightsail-deleting-bucket-access-keys
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Delete access keys for a Lightsail object storage bucket
<a name="amazon-lightsail-deleting-bucket-access-keys"></a>

Access keys are a set of credentials that grant full access to a bucket and its objects. Access keys consist of an access key ID and a secret access key as a set. If your secret access key is copied, is lost, or becomes compromised, you should delete your access key.

## Delete access keys for a bucket
<a name="delete-bucket-access-keys"></a>

You can use the following procedure to delete a bucket access key.

**Warning**  
After you delete an access key, it's gone forever and can't be restored. You can only replace it with a new access key.

**To delete an existing Lightsail object storage bucket access key**

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Storage**.

1. Choose the name of the bucket for which you want to delete an access key.

1. Choose the **Permissions** tab.

1. Under **Access keys**, choose the remove icon for the access key that you want to delete.  
![Displays how to delete an access key for a Lightsail object storage bucket.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-bucket-access-keys-delete.png)

1. Choose **Yes, delete** to proceed with deleting the access key.

Once the existing key is deleted, you can create a new access key and configure it for your software or plugin. For more information, see [Rotate bucket access keys](amazon-lightsail-bucket-security-best-practices.md#bucket-security-best-practices-rotate-bucket-access-keys).