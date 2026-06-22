---
id: "@specs/aws/kafka/docs/get-bootstrap-console"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Get the bootstrap brokers using the AWS Management Console"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Get the bootstrap brokers using the AWS Management Console

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/get-bootstrap-console
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Get the bootstrap brokers using the AWS Management Console
<a name="get-bootstrap-console"></a>

This process describes how to get bootstrap brokers for a cluster using the AWS Management Console. The term* bootstrap brokers* refers to a list of brokers that an Apache Kafka client can use as a starting point to connect to the cluster. This list doesn't necessarily include all of the brokers in a cluster.

1. Sign in to the AWS Management Console, and open the Amazon MSK console at [https://console.aws.amazon.com/msk/home?region=us-east-1\#/home/](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/).

1. The table shows all the clusters for the current region under this account. Choose the name of a cluster to view its description.

1. On the **Cluster summary** page, choose **View client information**. This shows you the bootstrap brokers, as well as the Apache ZooKeeper connection string.