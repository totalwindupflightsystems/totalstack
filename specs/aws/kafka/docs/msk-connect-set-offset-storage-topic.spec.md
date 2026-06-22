---
id: "@specs/aws/kafka/docs/msk-connect-set-offset-storage-topic"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Use custom offset storage topic"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Use custom offset storage topic

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/msk-connect-set-offset-storage-topic
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Use custom offset storage topic
<a name="msk-connect-set-offset-storage-topic"></a>

To provide offset continuity between source connectors, you can use an offset storage topic of your choice instead of the default topic. Specifying an offset storage topic helps you accomplish tasks like creating a source connector that resumes reading from the last offset of a previous connector.

To specify an offset storage topic, you supply a value for the `offset.storage.topic` property in your worker configuration before you create a connector. If you want to reuse the offset storage topic to consume offsets from a previously created connector, you must give the new connector the same name as the old connector. If you create a custom offset storage topic, you must set [https://kafka.apache.org/27/documentation.html#topicconfigs_cleanup.policy](https://kafka.apache.org/27/documentation.html#topicconfigs_cleanup.policy) to `compact` in your topic configuration.

**Note**  
If you specify an offset storage topic when you create a *sink* connector, MSK Connect creates the topic if it does not already exist. However, the topic will not be used to store connector offsets.   
Sink connector offsets are instead managed using the Kafka consumer group protocol. Each sink connector creates a group named `connect-{CONNECTOR_NAME}`. As long as the consumer group exists, any successive sink connectors that you create with the same `CONNECTOR_NAME` value will continue from the last committed offset.

**Important**  
If you want to update an existing connector configuration while maintaining offset continuity, use the UpdateConnector API. For more information, see [Update a connector](mkc-update-connector.md).

**Example : Specifying an offset storage topic when recreating a source connector**  
If you need to delete and recreate a connector while maintaining offset continuity, you can specify an offset storage topic in your worker configuration. For example, suppose you have a change data capture (CDC) connector and you want to recreate it without losing your place in the CDC stream. The following steps demonstrate how to accomplish this task.  

1. On your client machine, run the following command to find the name of your connector's offset storage topic. Replace `{{<bootstrapBrokerString>}}` with your cluster's bootstrap broker string. For instructions on getting your bootstrap broker string, see [Get the bootstrap brokers for an Amazon MSK cluster](msk-get-bootstrap-brokers.md).

   ```
   {{<path-to-your-kafka-installation>}}/bin/kafka-topics.sh --list --bootstrap-server {{<bootstrapBrokerString>}}
   ```

   The following output shows a list of all cluster topics, including any default internal connector topics. In this example, the existing CDC connector uses the [default offset storage topic](msk-connect-default-offset-storage-topic.md) created by MSK Connect. This is why the offset storage topic is called `__amazon_msk_connect_offsets_my-mskc-connector_12345678-09e7-4abc-8be8-c657f7e4ff32-2`.

   ```
   __consumer_offsets
   __amazon_msk_canary
   __amazon_msk_connect_configs_my-mskc-connector_12345678-09e7-4abc-8be8-c657f7e4ff32-2
   __amazon_msk_connect_offsets_my-mskc-connector_12345678-09e7-4abc-8be8-c657f7e4ff32-2
   __amazon_msk_connect_status_my-mskc-connector_12345678-09e7-4abc-8be8-c657f7e4ff32-2
   my-msk-topic-1
   my-msk-topic-2
   ```

1. Open the Amazon MSK console at [https://console.aws.amazon.com/msk/](https://console.aws.amazon.com/msk).

1. Choose your connector from the **Connectors** list. Copy and save the contents of the **Connector configuration** field so that you can modify it and use it to create the new connector.

1. Choose **Delete** to delete the connector. Then enter the connector name in the text input field to confirm deletion.

1. Create a custom worker configuration with values that fit your scenario. For instructions, see [Create a custom worker configuration](msk-connect-create-custom-worker-config.md).

   In your worker configuration, you must specify the name of the offset storage topic that you previously retrieved as the value for `offset.storage.topic` like in the following configuration. 

   ```
   config.providers.secretManager.param.aws.region=eu-west-3
   key.converter=<org.apache.kafka.connect.storage.StringConverter>
   value.converter=<org.apache.kafka.connect.storage.StringConverter>
   config.providers.secretManager.class=com.github.jcustenborder.kafka.config.aws.SecretsManagerConfigProvider
   config.providers=secretManager
   offset.storage.topic={{__amazon_msk_connect_offsets_my-mskc-connector_12345678-09e7-4abc-8be8-c657f7e4ff32-2}}
   ```

1. 
**Important**  
You must give your new connector the same name as the old connector.

   Create a new connector using the worker configuration that you set up in the previous step. For instructions, see [Create a connector](mkc-create-connector-intro.md).