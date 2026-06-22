---
id: "@specs/aws/kafka/docs/delete-cluster-api"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Delete an Amazon MSK Provisioned cluster using the API"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Delete an Amazon MSK Provisioned cluster using the API

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/delete-cluster-api
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Delete an Amazon MSK Provisioned cluster using the API
<a name="delete-cluster-api"></a>

The Amazon MSK API allows you to programmatically create and manage your MSK Provisioned cluster as part of automated infrastructure provisioning or deployment scripts. This process describes how to delete an Amazon MSK Provisioned cluster using the Amazon MSK API. Before you delete a Amazon MSK cluster, ensure that you have a backup of any important data stored in the cluster and that there aren't any scheduled tasks dependant on the cluster. You can't undo a MSK cluster deletion.

To delete a cluster using the API, see [DeleteCluster](https://docs.aws.amazon.com//msk/1.0/apireference/clusters-clusterarn.html#DeleteCluster).