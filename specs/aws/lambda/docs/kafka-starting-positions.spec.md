---
id: "@specs/aws/lambda/docs/kafka-starting-positions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Polling and stream positions"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Polling and stream positions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/kafka-starting-positions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Apache Kafka polling and stream starting positions in Lambda
<a name="kafka-starting-positions"></a>

The [ StartingPosition parameter](https://docs.aws.amazon.com/lambda/latest/api/API_CreateEventSourceMapping.html#lambda-CreateEventSourceMapping-request-StartingPosition) tells Lambda when to start reading messages from your Amazon MSK or self-managed Apache Kafka stream. There are three options to choose from:
+ **Latest** – Lambda starts reading just after the most recent record in the Kafka topic.
+ **Trim horizon** – Lambda starts reading from the last untrimmed record in the Kafka topic. This is also the oldest record in the topic.
+ **At timestamp** – Lambda starts reading from a position defined by a timestamp, in Unix time seconds. Use the [ StartingPositionTimestamp parameter](https://docs.aws.amazon.com/lambda/latest/api/API_CreateEventSourceMapping.html#lambda-CreateEventSourceMapping-request-StartingPositionTimestamp) to specify the timestamp.

Stream polling during an event source mapping create or update is eventually consistent:
+ During event source mapping creation, it may take several minutes to start polling events from the stream.
+ During event source mapping updates, it may take up to 90 seconds to stop and restart polling events from the stream.

This behavior means that if you specify `LATEST` as the starting position for the stream, the event source mapping could miss events during a create or update. To ensure that no events are missed, specify either `TRIM_HORIZON` or `AT_TIMESTAMP`.