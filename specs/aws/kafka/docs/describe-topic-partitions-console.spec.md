---
id: "@specs/aws/kafka/docs/describe-topic-partitions-console"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS View partition information using the AWS Management Console"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# View partition information using the AWS Management Console

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/describe-topic-partitions-console
> **target_lang:** meta — documentation tier. ALL sections preserved.



# View partition information using the AWS Management Console
<a name="describe-topic-partitions-console"></a>

1. Sign in to the AWS Management Console, and open the Amazon MSK console at [https://console.aws.amazon.com/msk/home?region=us-east-1\#/home/](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/).

1. In the list of clusters, choose the name of the cluster that contains the topic.

1. On the cluster details page, choose the **Topics** tab.

1. In the list of topics, choose the name of the topic for which you want to view partition information.

1. On the topic details page, the partition information is displayed, showing the partition number, leader broker, replicas, and in-sync replicas for each partition.