---
id: "@specs/aws/kafka/docs/msk-password-tutorial-connect"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Connecting to your cluster with sign-in credentials"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Connecting to your cluster with sign-in credentials

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/msk-password-tutorial-connect
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Connecting to your cluster with sign-in credentials
<a name="msk-password-tutorial-connect"></a>

After you create a secret and associate it with your cluster, you can connect your client to the cluster. The following procedure demonstrates how to connect a client to a cluster that uses SASL/SCRAM authentication. It also shows how to produce to and consume from an example topic.

**Topics**
+ [Connecting a client to cluster using SASL/SCRAM authentication](#w2aab9c13c29c17c13c11b9b7)
+ [Troubleshooting connection issues](#msk-password-tutorial-connect-troubleshooting)

## Connecting a client to cluster using SASL/SCRAM authentication
<a name="w2aab9c13c29c17c13c11b9b7"></a>

1. Run the following command on a machine that has AWS CLI installed. Replace {{clusterARN}} with the ARN of your cluster.

   ```
   aws kafka get-bootstrap-brokers --cluster-arn {{clusterARN}}
   ```

   From the JSON result of this command, save the value associated with the string named `BootstrapBrokerStringSaslScram`. You'll use this value in later steps.

1. On your client machine, create a JAAS configuration file that contains the user credentials stored in your secret. For example, for the user **alice**, create a file called `users_jaas.conf` with the following content.

   ```
   KafkaClient {
      org.apache.kafka.common.security.scram.ScramLoginModule required
      username="alice"
      password="alice-secret";
   };
   ```

1. Use the following command to export your JAAS config file as a `KAFKA_OPTS` environment parameter.

   ```
   export KAFKA_OPTS=-Djava.security.auth.login.config={{<path-to-jaas-file>}}/users_jaas.conf
   ```

1. Create a file named `kafka.client.truststore.jks` in a `/tmp` directory.

1. (Optional) Use the following command to copy the JDK key store file from your JVM `cacerts` folder into the `kafka.client.truststore.jks` file that you created in the previous step. Replace {{JDKFolder}} with the name of the JDK folder on your instance. For example, your JDK folder might be named `java-1.8.0-openjdk-1.8.0.201.b09-0.amzn2.x86_64`.

   ```
   cp /usr/lib/jvm/{{JDKFolder}}/lib/security/cacerts /tmp/kafka.client.truststore.jks
   ```

1. In the `bin` directory of your Apache Kafka installation, create a client properties file called `client_sasl.properties` with the following contents. This file defines the SASL mechanism and protocol.

   ```
   security.protocol=SASL_SSL
   sasl.mechanism=SCRAM-SHA-512
   ```

1. To create an example topic, run the following command. Replace {{BootstrapBrokerStringSaslScram}} with the bootstrap broker string that you obtained in step 1 of this topic.

   ```
   {{<path-to-your-kafka-installation>}}/bin/kafka-topics.sh --create --bootstrap-server {{BootstrapBrokerStringSaslScram}} --command-config {{<path-to-client-properties>}}/client_sasl.properties --replication-factor 3 --partitions 1 --topic ExampleTopicName
   ```

1. To produce to the example topic that you created, run the following command on your client machine. Replace {{BootstrapBrokerStringSaslScram}} with the bootstrap broker string that you retrieved in step 1 of this topic.

   ```
   {{<path-to-your-kafka-installation>}}/bin/kafka-console-producer.sh --broker-list {{BootstrapBrokerStringSaslScram}} --topic {{ExampleTopicName}} --producer.config client_sasl.properties
   ```

1. To consume from the topic you created, run the following command on your client machine. Replace {{BootstrapBrokerStringSaslScram}} with the bootstrap broker string that you obtained in step 1 of this topic.

   ```
   {{<path-to-your-kafka-installation>}}/bin/kafka-console-consumer.sh --bootstrap-server {{BootstrapBrokerStringSaslScram}} --topic {{ExampleTopicName}} --from-beginning --consumer.config client_sasl.properties
   ```

## Troubleshooting connection issues
<a name="msk-password-tutorial-connect-troubleshooting"></a>

When running Kafka client commands, you might encounter Java heap memory errors, especially when working with large topics or datasets. These errors occur because Kafka tools run as Java applications with default memory settings that might be insufficient for your workload.

To resolve `Out of Memory Java Heap` errors, you can increase the Java heap size by modifying the `KAFKA_OPTS` environment variable to include memory settings.

The following example sets the maximum heap size to 1GB (`-Xmx1G`). You can adjust this value based on your available system memory and requirements.

```
export KAFKA_OPTS="-Djava.security.auth.login.config={{<path-to-jaas-file>}}/users_jaas.conf -Xmx1G"
```

For consuming large topics, consider using time-based or offset-based parameters instead of `--from-beginning` to limit memory usage:

```
{{<path-to-your-kafka-installation>}}/bin/kafka-console-consumer.sh --bootstrap-server {{BootstrapBrokerStringSaslScram}} --topic {{ExampleTopicName}} --max-messages 1000 --consumer.config client_sasl.properties
```