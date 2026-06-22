---
id: "@specs/aws/kafka/docs/list-clusters-cli"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS List clusters using the AWS CLI"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# List clusters using the AWS CLI

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/list-clusters-cli
> **target_lang:** meta — documentation tier. ALL sections preserved.



# List clusters using the AWS CLI
<a name="list-clusters-cli"></a>

To get a bootstrap broker for an Amazon MSK cluster, you need the cluster Amazon Resource Name (ARN). If you don't have the ARN for your cluster, you can find it by listing all clusters. See [Get the bootstrap brokers for an Amazon MSK cluster](msk-get-bootstrap-brokers.md).

```
aws kafka list-clusters
```