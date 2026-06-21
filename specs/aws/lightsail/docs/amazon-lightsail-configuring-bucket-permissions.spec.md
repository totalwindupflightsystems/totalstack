---
id: "@specs/aws/lightsail/docs/amazon-lightsail-configuring-bucket-permissions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Configure access permissions"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Configure access permissions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/amazon-lightsail-configuring-bucket-permissions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Manage Lightsail bucket access permissions for enhanced security
<a name="amazon-lightsail-configuring-bucket-permissions"></a>

Use bucket access permissions to control public (unauthenticated) read-only access to objects in a bucket. You can make a bucket private or public (read-only). You can also make a bucket private, while having the option to make individual objects public (read-only).

**Important**  
When you make a bucket public (read-only), you make all objects in the bucket readable by anyone on the internet through the bucket's URL (for example, `https://amzn-s3-demo-bucket.us-east-1.amazonaws.com/media/sailbot.jpg`). Don't make a bucket public (read-only) if you don't want anyone on the internet to have access to your objects.

For more information about permission options, see [Bucket permissions](amazon-lightsail-understanding-bucket-permissions.md). For more information about security best practices, see [Security Best Practices for object storage](amazon-lightsail-bucket-security-best-practices.md). For more information about buckets, see [Object storage](buckets-in-amazon-lightsail.md).

**Important**  
Lightsail object storage resources take into account both Lightsail bucket access permissions and Amazon S3 account-level block public access configurations when allowing or denying public access. For more information, see [Block public access for buckets](amazon-lightsail-block-public-access-for-buckets.md). 

## Configure bucket access permissions
<a name="configure-bucket-access-permissions"></a>

Complete the following procedure to configure access permissions for a bucket.

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Storage**.

1. Choose the name of the bucket for which you want to configure access permissions.

1. Choose the **Permissions** tab.

   The **Bucket access permissions** section of the page displays the currently configured access permission for the bucket.

1. Choose **Change permission** to change the bucket access permissions.

1. Choose one of the following options:
   + **All objects are private** – All objects in the bucket are readable only by you or anyone you give access to.
   + **Individual objects can be made public (read-only)** – Objects in the bucket are readable only by you or anyone you give access to, unless you specify an individual object to be public (read-only). For more information about individual object access permissions, see [Configure access permissions for individual objects in a bucket](amazon-lightsail-configuring-individual-object-access.md).

     We recommend that you select the **Individual objects can be made public (read-only)** option only if you have a specific need to do so, such as making only some of the objects in your bucket public while keeping all other objects private. For example, some WordPress plugins require that your bucket allows individual objects to be made public. For more information, see [Tutorial: Connect a bucket to your WordPress instance](amazon-lightsail-connecting-buckets-to-wordpress.md) and [Tutorial: Use a bucket with a content delivery network distribution](amazon-lightsail-using-distributions-with-buckets.md).
   + **All objects are public (read-only)** – All objects in the bucket are readable by anyone on the internet.
**Important**  
When you make a bucket public (read-only), you make all objects in the bucket readable by anyone on the internet through the bucket's URL (for example, `https://amzn-s3-demo-bucket.us-east-1.amazonaws.com/media/sailbot.jpg`). Don't make a bucket public (read-only) if you don't want anyone on the internet to have access to your objects.

1. Choose **Save** to save the change. Otherwise, choose **Cancel**.

   The following changes are implemented depending on which bucket access permission you change to:
   + **All objects are private** - All objects in the bucket become private even if they were previously configured with a **Public (read-only)** individual object access permission.
   + **Individual objects can be made public (read-only)** - Objects that were previously configured with a **Public (read-only)** individual object access permission become public. You can now configure individual object access permissions for objects.
   + **All objects are public (read-only)** - All objects in the bucket become public (read-only) even if they were previously configured with a **Private** individual object access permission.

     For more information about individual object access permissions, see [Configure access permissions for individual objects in a bucket](amazon-lightsail-configuring-individual-object-access.md).