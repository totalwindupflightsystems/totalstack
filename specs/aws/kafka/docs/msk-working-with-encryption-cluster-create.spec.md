---
id: "@specs/aws/kafka/docs/msk-working-with-encryption-cluster-create"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Specify encryption settings when creating a Amazon MSK cluster"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Specify encryption settings when creating a Amazon MSK cluster

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/msk-working-with-encryption-cluster-create
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Specify encryption settings when creating a Amazon MSK cluster
<a name="msk-working-with-encryption-cluster-create"></a>

This process describes how to specify encryption settings when creating a Amazon MSK cluster.

**Specify encryption settings when creating a cluster**

1. Save the contents of the previous example in a file and give the file any name that you want. For example, call it `encryption-settings.json`.

1. Run the `create-cluster` command and use the `encryption-info` option to point to the file where you saved your configuration JSON. The following is an example. Replace {{{YOUR MSK VERSION}}} with a version that matches the Apache Kafka client version. For information on how to find your MSK cluster version, see [Determining your MSK cluster version](create-topic.md#find-msk-cluster-version). Be aware that using an Apache Kafka client version that is not the same as your MSK cluster version may lead to Apache Kafka data corruption, loss and down time.

   ```
   aws kafka create-cluster --cluster-name "ExampleClusterName" --broker-node-group-info file://brokernodegroupinfo.json --encryption-info file://encryptioninfo.json --kafka-version "{{{YOUR MSK VERSION}}}" --number-of-broker-nodes 3
   ```

   The following is an example of a successful response after running this command.

   ```
   {
       "ClusterArn": "arn:aws:kafka:us-east-1:123456789012:cluster/SecondTLSTest/abcdabcd-1234-abcd-1234-abcd123e8e8e",
       "ClusterName": "ExampleClusterName",
       "State": "CREATING"
   }
   ```