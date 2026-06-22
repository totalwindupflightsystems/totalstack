---
id: "@specs/aws/kafka/docs/msk-update-tiered-storage-console"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Update tiered storage using console"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Update tiered storage using console

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/msk-update-tiered-storage-console
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Update tiered storage on an existing Amazon MSK cluster using the console
<a name="msk-update-tiered-storage-console"></a>

This process describes how to updated a tiered storage Amazon MSK cluster using the AWS Management Console.

Make sure the current Apache Kafka version of your MSK cluster is 2.8.2.tiered. Refer to [updating the Apache Kafka version](https://docs.aws.amazon.com/msk/latest/developerguide/version-upgrades.html) if you need to upgrade your MSK cluster to 2.8.2.tiered version.

**Note**  
You can enable tiered storage only if your cluster's log.cleanup.policy is set to `delete`, as compacted topics are not supported on tiered storage. Later, you can configure an individual topic's log.cleanup.policy to `compact` if tiered storage is not enabled on that particular topic. See [Topic-level configuration](https://docs.aws.amazon.com//msk/latest/developerguide/msk-configuration-properties.html#msk-topic-confinguration) for more details on supported configuration attributes.

1. Open the Amazon MSK console at [https://console.aws.amazon.com/msk/](https://console.aws.amazon.com/msk/).

1. Go to the cluster summary page and choose **Properties**.

1. Go to the **Storage** section and choose **Edit cluster storage mode**.

1. Choose **Tiered storage and EBS storage** and **Save changes**.