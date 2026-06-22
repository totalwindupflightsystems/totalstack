---
id: "@specs/aws/kafka/docs/msk-autoexpand-setup-console"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Set up automatic scaling"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Set up automatic scaling

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/msk-autoexpand-setup-console
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Set up automatic scaling using the Amazon MSK AWS Management Console
<a name="msk-autoexpand-setup-console"></a>

This process describes how to use the Amazon MSK console to implement automatic scaling for storage.

1. Sign in to the AWS Management Console, and open the Amazon MSK console at [https://console.aws.amazon.com/msk/home?region=us-east-1\#/home/](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/).

1. In the list of clusters, choose your cluster. This takes you to a page that lists details about the cluster.

1. In the **Auto scaling for storage** section, choose **Configure**.

1. Create and name an auto-scaling policy. Specify the storage utilization target, the maximum storage capacity, and the target metric.

1. Choose `Save changes`.

When you save and enable the new policy, the policy becomes active for the cluster. Amazon MSK then expands the cluster's storage when the storage utilization target is reached.