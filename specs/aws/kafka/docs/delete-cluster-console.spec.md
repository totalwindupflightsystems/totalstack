---
id: "@specs/aws/kafka/docs/delete-cluster-console"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Delete an Amazon MSK Provisioned cluster using the AWS Management Console"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Delete an Amazon MSK Provisioned cluster using the AWS Management Console

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/delete-cluster-console
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Delete an Amazon MSK Provisioned cluster using the AWS Management Console
<a name="delete-cluster-console"></a>

This process describes how to delete an Amazon MSK Provisioned cluster using the AWS Management Console. Before you delete a MSK cluster, ensure that you have a backup of any important data stored in the cluster and that there aren't any scheduled tasks dependant on the cluster. You can't undo a MSK cluster deletion.

1. Sign in to the AWS Management Console, and open the Amazon MSK console at [https://console.aws.amazon.com/msk/home?region=us-east-1\#/home/](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/).

1. Choose the MSK cluster that you want to delete by selecting the check box next to it.

1. Choose **Delete**, and then confirm deletion.