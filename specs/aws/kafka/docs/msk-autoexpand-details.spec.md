---
id: "@specs/aws/kafka/docs/msk-autoexpand-details"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Auto-scaling policies"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Auto-scaling policies

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/msk-autoexpand-details
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Auto-scaling policy details for Amazon MSK
<a name="msk-autoexpand-details"></a>

An auto-scaling policy defines the following parameters for your cluster:
+ **Storage Utilization Target**: The storage utilization threshold that Amazon MSK uses to trigger an auto-scaling operation. You can set the utilization target between 10% and 80% of the current storage capacity. We recommend that you set the Storage Utilization Target between 50% and 60%.
+ **Maximum Storage Capacity**: The maximum scaling limit that Amazon MSK can set for your broker storage. You can set the maximum storage capacity up to 16 TiB per broker. For more information, see [Amazon MSK quota](limits.md).

When Amazon MSK detects that your `Maximum Disk Utilization` metric is equal to or greater than the `Storage Utilization Target` setting, it increases your storage capacity by an amount equal to the larger of two numbers: 10 GiB or 10% of current storage. For example, if you have 1000 GiB, that amount is 100 GiB. The service checks your storage utilization every minute. Further scaling operations continue to increase storage by an amount equal to the larger of two numbers: 10 GiB or 10% of current storage.

To determine if auto-scaling operations have occurred, use the [ ListClusterOperations](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-operations.html#ListClusterOperations) operation.