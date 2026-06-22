---
id: "@specs/aws/kafka/docs/serverless-config"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Configuration properties"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Configuration properties

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/serverless-config
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Configuration properties for MSK Serverless clusters
<a name="serverless-config"></a>

Amazon MSK sets broker configuration properties for serverless clusters. You can't change these broker configuration property settings. However, you can set or modify the following topic-level configuration properties. All other topic-level configuration properties are not configurable.


****  

| Configuration property | Default | Editable | Maximum allowed value | 
| --- | --- | --- | --- | 
| [cleanup.policy](https://kafka.apache.org/documentation/#topicconfigs_cleanup.policy) | Delete | Yes, but only at topic creation time |  | 
| [compression.type](https://kafka.apache.org/documentation/#topicconfigs_compression.type) | Producer | Yes |  | 
| [max.message.bytes](https://kafka.apache.org/documentation/#topicconfigs_max.message.bytes) | 1048588 | Yes | 8388608 (8MiB) | 
|  [message.timestamp.difference.max.ms](https://kafka.apache.org/documentation/#topicconfigs_message.timestamp.difference.max.ms)  | long.max | Yes |  | 
| [message.timestamp.type](https://kafka.apache.org/documentation/#topicconfigs_message.timestamp.type) | CreateTime | Yes |  | 
| [retention.bytes](https://kafka.apache.org/documentation/#topicconfigs_retention.bytes) | 250 GiB | Yes | Unlimited; set it to -1 for unlimited retention | 
| [retention.ms](https://kafka.apache.org/documentation/#topicconfigs_retention.ms) | 7 days | Yes | Unlimited; set it to -1 for unlimited retention | 

To set or modify these topic-level configuration properties, you can use Apache Kafka command line tools. See [3.2 Topic-level Configs](https://kafka.apache.org/documentation/#topicconfigs) in the official Apache Kafka documentation for more information and examples of how to set them.

**Note**  
You can't modify the segment.bytes configuration for topics in MSK Serverless. However, a Kafka Streams application might attempt to create an internal topic with a segment.bytes configuration value, which is different from what MSK Serverless will allow. For information about configuring Kafka Streams with MSK Serverless, see [Using Kafka Streams with MSK Serverless](use-kafka-streams-express-brokers-msk-serverless.md).

When using the Apache Kafka command line tools with Amazon MSK Serverless, make sure you completed steps 1-4 in the *To set up Apache Kafka client tools on the client machine* section of the [Amazon MSK Serverless Getting Started documentation](https://docs.aws.amazon.com/msk/latest/developerguide/create-serverless-cluster-client.html). Additionally, you must include the `--command-config client.properties` parameter in your commands.

For example, the following command can be used to modify the retention.bytes topic configuration property to set unlimited retention:

```
{{<path-to-your-kafka-client-installation>}}/bin/kafka-configs.sh —bootstrap-server {{<bootstrap_server_string>}} —command-config client.properties --entity-type topics --entity-name {{<topic_name>}} --alter --add-config retention.bytes=-1
```

In this example, replace {{<bootstrap server string>}} with the bootstrap server endpoint for your Amazon MSK Serverless cluster, and {{<topic\_name>}} with the name of the topic you want to modify.

The `--command-config client.properties` parameter ensures that the Kafka command line tool uses the appropriate configuration settings to communicate with your Amazon MSK Serverless cluster.