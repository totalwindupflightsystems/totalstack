---
id: "@specs/aws/kafka/docs/zookeeper-security-tls"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Using TLS security with Apache ZooKeeper"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Using TLS security with Apache ZooKeeper

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/zookeeper-security-tls
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Using TLS security with Apache ZooKeeper
<a name="zookeeper-security-tls"></a>

You can use TLS security for encryption in transit between your clients and your Apache ZooKeeper nodes. To implement TLS security with your Apache ZooKeeper nodes, do the following:
+ Clusters must use Apache Kafka version 2.5.1 or later to use TLS security with Apache ZooKeeper.
+ Enable TLS security when you create or configure your cluster. Clusters created with Apache Kafka version 2.5.1 or later with TLS enabled automatically use TLS security with Apache ZooKeeper endpoints. For information about setting up TLS security, see [Get started with Amazon MSK encryption](msk-working-with-encryption.md).
+ Retrieve the TLS Apache ZooKeeper endpoints using the [DescribeCluster ](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn.html#DescribeCluster) operation.
+ Create an Apache ZooKeeper configuration file for use with the `kafka-configs.sh` and [https://kafka.apache.org/documentation/#security_authz_cli](https://kafka.apache.org/documentation/#security_authz_cli) tools, or with the ZooKeeper shell. With each tool, you use the `--zk-tls-config-file` parameter to specify your Apache ZooKeeper config.

  The following example shows a typical Apache ZooKeeper configuration file: 

  ```
  zookeeper.ssl.client.enable=true
  zookeeper.clientCnxnSocket=org.apache.zookeeper.ClientCnxnSocketNetty
  zookeeper.ssl.keystore.location=kafka.jks
  zookeeper.ssl.keystore.password=test1234
  zookeeper.ssl.truststore.location=truststore.jks
  zookeeper.ssl.truststore.password=test1234
  ```
+ For other commands (such as `kafka-topics`), you must use the `KAFKA_OPTS` environment variable to configure Apache ZooKeeper parameters. The following example shows how to configure the `KAFKA_OPTS` environment variable to pass Apache ZooKeeper parameters into other commands:

  ```
  export KAFKA_OPTS="
  -Dzookeeper.clientCnxnSocket=org.apache.zookeeper.ClientCnxnSocketNetty 
  -Dzookeeper.client.secure=true 
  -Dzookeeper.ssl.trustStore.location=/home/ec2-user/kafka.client.truststore.jks
  -Dzookeeper.ssl.trustStore.password=changeit"
  ```

  After you configure the `KAFKA_OPTS` environment variable, you can use CLI commands normally. The following example creates an Apache Kafka topic using the Apache ZooKeeper configuration from the `KAFKA_OPTS` environment variable:

  ```
  {{<path-to-your-kafka-installation>}}/bin/kafka-topics.sh --create --zookeeper {{ZooKeeperTLSConnectString}} --replication-factor 3 --partitions 1 --topic AWSKafkaTutorialTopic
  ```

**Note**  
The names of the parameters you use in your Apache ZooKeeper configuration file and those you use in your `KAFKA_OPTS` environment variable are not consistent. Pay attention to which names you use with which parameters in your configuration file and `KAFKA_OPTS` environment variable.

For more information about accessing your Apache ZooKeeper nodes with TLS, see [ KIP-515: Enable ZK client to use the new TLS supported authentication](https://cwiki.apache.org/confluence/display/KAFKA/KIP-515%3A+Enable+ZK+client+to+use+the+new+TLS+supported+authentication).