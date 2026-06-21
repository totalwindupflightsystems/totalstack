---
id: "@specs/aws/lightsail/docs/amazon-lightsail-configuring-bucket-cross-account-access"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Cross-account access"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Cross-account access

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/amazon-lightsail-configuring-bucket-cross-account-access
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Grant read-only access to Lightsail buckets across AWS accounts
<a name="amazon-lightsail-configuring-bucket-cross-account-access"></a>

Use cross-account access to grant read-only access to all objects in a bucket for other AWS accounts and their users. Cross-account access is ideal if you want to share objects with another AWS account. When you grant cross-account access to another AWS account, users in that account have read-only access to objects in a bucket through the URL of the bucket and objects (for example, `https://amzn-s3-demo-bucket.us-east-1.amazonaws.com/media/sailbot.jpg`). You can give bucket access to a maximum of 10 AWS accounts.

For more information about permission options, see [Bucket permissions](amazon-lightsail-understanding-bucket-permissions.md). For more information about security best practices, see [Security Best Practices for object storage](amazon-lightsail-bucket-security-best-practices.md). For more information about buckets, see [Object storage](buckets-in-amazon-lightsail.md).

## Configure cross-account access for a bucket
<a name="configure-bucket-cross-account-access"></a>

Complete the following procedure to configure cross-account access for a bucket.

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Storage**.

1. Choose the name of the bucket for which you want to configure cross-account access.

1. Choose the **Permissions** tab.

   The **Cross-account access** section of the page displays the AWS account IDs that are currently configured to access the bucket, if any.

1. Choose **Add cross-account access** to grant access to the bucket for another AWS account.

1. Enter the ID of the AWS account for which you want to grant access in the **Account ID** text box.

1. Choose **Save** to grant access. Otherwise, choose **Cancel**.

   The AWS account ID you added is listed in the **Cross-account access** section of the page. To remove cross-account access for an AWS account, choose the delete (trash can) icon next to the AWS account ID that you want to remove.