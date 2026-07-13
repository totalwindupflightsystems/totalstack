---
id: "@specs/aws/lambda/docs/kafka-retry-configurations"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Retry configurations"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Retry configurations

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/kafka-retry-configurations
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Configuring error handling controls for Kafka event sources
<a name="kafka-retry-configurations"></a>

You can configure how Lambda handles errors and retries for your Kafka event source mappings. These configurations help you control how Lambda processes failed records and manages retry behavior.

## Available retry configurations
<a name="kafka-retry-options"></a>

The following retry configurations are available for both Amazon MSK and self-managed Kafka event sources:
+ **Maximum retry attempts** – The maximum number of times Lambda retries when your function returns an error. This doesn't count the initial invocation attempt. The default is -1 (infinite). When you configure both infinite retries and an [on-failure destination](kafka-on-failure-destination.md), Lambda automatically applies a maximum of 10 retry attempts.
+ **Maximum record age** – The maximum age of a record that Lambda sends to your function. The default is -1 (infinite).
+ **Split batch on error** – When your function returns an error, split the batch into two smaller batches and retry each separately. This helps isolate problematic records.
+ **Partial batch response** – Allow your function to return information about which records in a batch failed processing, so Lambda can retry only the failed records.

## Configuring error handling controls (console)
<a name="kafka-retry-console"></a>

You can configure retry behavior when creating or updating a Kafka event source mapping in the Lambda console.

**To configure retry behavior for a Kafka event source (console)**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Choose your function name.

1. Do one of the following:
   + To add a new Kafka trigger, under **Function overview**, choose **Add trigger**.
   + To modify an existing Kafka trigger, choose the trigger and then choose **Edit**.

1. Under **Event poller configuration**, select provisioned mode to configure error handling controls:

   1. For **Retry attempts**, enter the maximum number of retry attempts (0-10000, or -1 for infinite).

   1. For **Maximum record age**, enter the maximum age in seconds (60-604800, or -1 for infinite).

   1. To enable batch splitting when errors occur, select **Split batch on error**.

   1. To enable partial batch response, select **ReportBatchItemFailures**.

1. Choose **Add** or **Save**.

## Configuring retry behavior (AWS CLI)
<a name="kafka-retry-cli"></a>

Use the following AWS CLI commands to configure retry behavior for your Kafka event source mappings.

### Creating an event source mapping with retry configurations
<a name="kafka-retry-cli-create"></a>

The following example creates a self-managed Kafka event source mapping with error handling controls:

```
aws lambda create-event-source-mapping \
  --function-name my-kafka-function \
  --topics my-kafka-topic \
  --source-access-configuration Type=SASL_SCRAM_512_AUTH,URI=arn:aws:secretsmanager:us-east-1:111122223333:secret:MyBrokerSecretName \
  --self-managed-event-source '{"Endpoints":{"KAFKA_BOOTSTRAP_SERVERS":["abc.xyz.com:9092"]}}' \
  --starting-position LATEST \
  --provisioned-poller-config MinimumPollers=1,MaximumPollers=1 \
  --maximum-retry-attempts 3 \
  --maximum-record-age-in-seconds 3600 \
  --bisect-batch-on-function-error \
  --function-response-types "ReportBatchItemFailures"
```

For Amazon MSK event sources:

```
aws lambda create-event-source-mapping \
  --event-source-arn arn:aws:kafka:us-east-1:111122223333:cluster/my-cluster/fc2f5bdf-fd1b-45ad-85dd-15b4a5a6247e-2 \
  --topics AWSMSKKafkaTopic \
  --starting-position LATEST \
  --function-name my-kafka-function \
  --source-access-configurations '[{"Type": "SASL_SCRAM_512_AUTH","URI": "arn:aws:secretsmanager:us-east-1:111122223333:secret:my-secret"}]' \
  --provisioned-poller-config MinimumPollers=1,MaximumPollers=1 \
  --maximum-retry-attempts 3 \
  --maximum-record-age-in-seconds 3600 \
  --bisect-batch-on-function-error \
  --function-response-types "ReportBatchItemFailures"
```

### Updating retry configurations
<a name="kafka-retry-cli-update"></a>

Use the `update-event-source-mapping` command to modify retry configurations for an existing event source mapping:

```
aws lambda update-event-source-mapping \
  --uuid 12345678-1234-1234-1234-123456789012 \
  --maximum-retry-attempts 5 \
  --maximum-record-age-in-seconds 7200 \
  --bisect-batch-on-function-error \
  --function-response-types "ReportBatchItemFailures"
```

## PartialBatchResponse
<a name="kafka-partial-batch-response"></a>

Partial batch response, also known as ReportBatchItemFailures, is a key feature for error handling in Lambda's integration with Kafka sources. Without this feature, when an error occurs in one of the items in a batch, it results in reprocessing all messages in that batch. With partial batch response enabled and implemented, the handler returns identifiers only for the failed messages, allowing Lambda to retry just those specific items. This provides greater control over how batches containing failed messages are processed.

To report batch errors, you will use this JSON schema:

```
{
  "batchItemFailures": [
    {
      "itemIdentifier": {
        "partition": "topic-partition_number",
        "offset": 100
      }
    },
    ...
  ]
}
```

**Important**  
If you return an empty valid JSON or null, the event source mapping will consider a batch as successfully processed. Any invalid topic-partition\_number or offset returned that was not present in the invoked event will be treated as failure and entire batch will be retried.

The following code examples show how to implement partial batch response for Lambda functions that receive events from Kafka sources. The function reports the batch item failures in the response, signaling to Lambda to retry those messages later.

Here is a Python Lambda handler implementation that shows this approach:

```
import base64
from typing import Any, Dict, List

def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, List[Dict[str, Dict[str, Any]]]]:
    failures: List[Dict[str, Dict[str, Any]]] = []
    records_dict = event.get("records", {})
    
    for topic_partition, records_list in records_dict.items():
        for record in records_list:
            topic = record.get("topic")
            partition = record.get("partition")
            offset = record.get("offset")
            value_b64 = record.get("value")
            
            try:
                data = base64.b64decode(value_b64).decode("utf-8")
                process_message(data)
            except Exception as exc:
                print(f"Failed to process record topic={topic} partition={partition} offset={offset}: {exc}")
                item_identifier: Dict[str, Any] = {
                    "partition": f"{topic}-{partition}",
                    "offset": int(offset) if offset is not None else None,
                }
                failures.append({"itemIdentifier": item_identifier})
    
    return {"batchItemFailures": failures}

def process_message(data: str) -> None:
    # Your business logic for a single message
    pass
```

Here is a Node.js version:

```
const { Buffer } = require("buffer");

const handler = async (event) => {
  const failures = [];
  
  for (let topicPartition in event.records) {
    const records = event.records[topicPartition];
    
    for (const record of records) {
      const topic = record.topic;
      const partition = record.partition;
      const offset = record.offset;
      const valueBase64 = record.value;
      const data = Buffer.from(valueBase64, "base64").toString("utf8");
      
      try {
        await processMessage(data);
      } catch (error) {
        console.error("Failed to process record", { topic, partition, offset, error });
        const itemIdentifier = {
          "partition": `${topic}-${partition}`,
          "offset": Number(offset),
        };
        failures.push({ itemIdentifier });
      }
    }
  }
  
  return { batchItemFailures: failures };
};

async function processMessage(payload) {
  // Your business logic for a single message
}

module.exports = { handler };
```

Here is a Java version:

```
import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;

import java.util.ArrayList;
import java.util.Base64;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class KafkaBatchHandler implements RequestHandler<Map<String, Object>, Map<String, Object>> {

    @SuppressWarnings("unchecked")
    @Override
    public Map<String, Object> handleRequest(Map<String, Object> event, Context context) {
        List<Map<String, Object>> failures = new ArrayList<>();
        Map<String, List<Map<String, Object>>> records =
                (Map<String, List<Map<String, Object>>>) event.getOrDefault("records", Map.of());

        for (Map.Entry<String, List<Map<String, Object>>> entry : records.entrySet()) {
            for (Map<String, Object> record : entry.getValue()) {
                String topic = (String) record.get("topic");
                Object partition = record.get("partition");
                Object offset = record.get("offset");
                String valueBase64 = (String) record.get("value");

                try {
                    String data = new String(Base64.getDecoder().decode(valueBase64), "UTF-8");
                    processMessage(data);
                } catch (Exception e) {
                    System.err.printf("Failed to process record topic=%s partition=%s offset=%s: %s%n",
                            topic, partition, offset, e.getMessage());
                    Map<String, Object> itemIdentifier = new HashMap<>();
                    itemIdentifier.put("partition", topic + "-" + partition);
                    itemIdentifier.put("offset", offset instanceof Number ? ((Number) offset).longValue() : null);
                    Map<String, Object> failure = new HashMap<>();
                    failure.put("itemIdentifier", itemIdentifier);
                    failures.add(failure);
                }
            }
        }

        Map<String, Object> response = new HashMap<>();
        response.put("batchItemFailures", failures);
        return response;
    }

    private void processMessage(String data) {
        // Your business logic for a single message
    }
}
```