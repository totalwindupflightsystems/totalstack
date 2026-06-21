---
id: "@specs/aws/lightsail/docs/amazon-lightsail-configuring-individual-object-access"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Individual object access permissions"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Individual object access permissions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/amazon-lightsail-configuring-individual-object-access
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Grant public access to individual bucket objects in Amazon Lightsail
<a name="amazon-lightsail-configuring-individual-object-access"></a>

Use individual object access permissions to control public (unauthenticated) read-only access to individual objects in a bucket. You can make individual objects in a bucket private or public (read-only).

**Important**  
Individual object access permissions can be configured only when the access permission of a bucket is set to **Individual objects can be made public (read-only)**. For more information about bucket permission options, see [Bucket permissions](amazon-lightsail-understanding-bucket-permissions.md). For more information about buckets, see [Object storage](buckets-in-amazon-lightsail.md).

We recommend that you configure individual object access permissions only if you have a specific need to do so, such as making only some of the objects in your bucket public while keeping all other objects private. For example, some WordPress plugins require that your bucket allows individual objects to be made public. For more information, see [Tutorial: Connect a bucket to your WordPress instance](amazon-lightsail-connecting-buckets-to-wordpress.md) and [Tutorial: Use a bucket with a content delivery network distribution](amazon-lightsail-using-distributions-with-buckets.md).

For more information about permission options, see [Bucket permissions](amazon-lightsail-understanding-bucket-permissions.md). For more information about security best practices, see [Security Best Practices for object storage](amazon-lightsail-bucket-security-best-practices.md). For more information about buckets, see [Object storage](buckets-in-amazon-lightsail.md).

## Configure individual object access permissions
<a name="configure-individual-object-access-permissions"></a>

Complete the following procedure to configure access permissions for an individual object in a bucket. For an example IAM policy that grants a user the ability to manage a bucket in Lightsail, see , [IAM policy to manage buckets](amazon-lightsail-bucket-management-policies.md).

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Storage**.

1. Choose the name of the bucket for which you want to configure access permissions for an individual object.

1. Choose the **Objects** tab.

1. Add a check mark next to the object for which you want to configure an access permission.

   The object information pane displays the current access permissions for the object.

1. Choose **Edit** in the **Permissions** section of the object information pane to change the access permission for the object.
**Note**  
If the edit option is not available, then the access permission of your bucket does not allow for individual object access permissions to be configured. To configure individual object access permissions, the bucket access permission must be set to **Individual objects can be made public (read-only)**. For more information, see [Configure bucket access permissions](amazon-lightsail-configuring-bucket-permissions.md).

1. Choose one of the following options in the **Select a permission** dropdown menu:
   + **Private** – The object is readable only by you or anyone you give access to.
   + **Public (read-only)** – The object is readable by anyone in the world.

1. Choose **Save** to save the change. Otherwise, choose **Cancel**.

   The **Bucket access permission** setting of the bucket has the following effects on individual object access permissions:
   + If you change the bucket access permission to **All objects are private**, all objects in the bucket become private even if they were configured with a **Public (read-only)** individual object access permission. However, individual object access permissions that were configured are retained. For example, if you change the bucket access permission back to **Individual objects can be made public (read-only)**, all objects with a **Public (read-only)** individual access permission become publicly readable again.
   + If you change the bucket access permission to **All objects are public (read-only)**, all objects in the bucket become public (read-only), even if they were configured with a **Private** individual object access permission.

     For more information about bucket access permissions, see [Configure bucket access permissions](amazon-lightsail-configuring-bucket-permissions.md).