---
id: "@specs/aws/kafka/docs/delete-cluster-cli"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Delete an Amazon MSK Provisioned cluster using the AWS CLI"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Delete an Amazon MSK Provisioned cluster using the AWS CLI

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/delete-cluster-cli
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Delete an Amazon MSK Provisioned cluster using the AWS CLI
<a name="delete-cluster-cli"></a>

This process describes how to delete an MSK Provisioned cluster using the AWS CLI. Before you delete a MSK cluster, ensure that you have a backup of any important data stored in the cluster and that there aren't any scheduled tasks dependant on the cluster. You can't undo a MSK cluster deletion.

Run the following command, replacing {{ClusterArn}} with the Amazon Resource Name (ARN) that you obtained when you created your cluster. If you don't have the ARN for your cluster, you can find it by listing all clusters. For more information, see [List Amazon MSK clusters](msk-list-clusters.md).

```
aws kafka delete-cluster --cluster-arn {{ClusterArn}}
```