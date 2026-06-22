---
id: "@specs/aws/kafka/docs/msk-connect-default-offset-storage-topic"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Use the default offset storage topic"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Use the default offset storage topic

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/msk-connect-default-offset-storage-topic
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Use the default offset storage topic
<a name="msk-connect-default-offset-storage-topic"></a>

By default, Amazon MSK Connect generates a new offset storage topic on your Kafka cluster for each connector that you create. MSK constructs the default topic name using parts of the connector ARN. For example, `__amazon_msk_connect_offsets_my-mskc-connector_12345678-09e7-4abc-8be8-c657f7e4ff32-2`. 