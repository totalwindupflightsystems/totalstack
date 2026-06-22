---
id: "@specs/aws/kafka/docs/msk-create-cluster-tiered-storage-console"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Create tiered storage cluster with console"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Create tiered storage cluster with console

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/msk-create-cluster-tiered-storage-console
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Create a Amazon MSK cluster with tiered storage with the AWS Management Console
<a name="msk-create-cluster-tiered-storage-console"></a>

This process describes how to create a tiered storage Amazon MSK cluster using the AWS Management Console.

1. Open the Amazon MSK console at [https://console.aws.amazon.com/msk/](https://console.aws.amazon.com/msk/).

1. Choose **Create cluster**.

1. Choose **Custom create** for tiered storage.

1. Specify a name for the cluster.

1. In the **Cluster type**, select **Provisioned**.

1. Choose an Amazon Kafka version that supports tiered storage for Amazon MSK to use to create the cluster. 

1. Specify a size of broker other than **kafka.t3.small**.

1. Select the number of brokers that you want Amazon MSK to create in each Availability Zone. The minimum is one broker per Availability Zone, and the maximum is 30 brokers per cluster.

1. Specify the number of zones that brokers are distributed across.

1. Specify the number of Apache Kafka brokers that are deployed per zone.

1. Select **Storage options**. This includes **Tiered storage and EBS storage** to enable tiered storage mode.

1. Follow the remaining steps in the cluster creation wizard. When complete, **Tiered storage and EBS storage** appears as the cluster storage mode in the **Review and create** view.

1. Select **Create cluster**.