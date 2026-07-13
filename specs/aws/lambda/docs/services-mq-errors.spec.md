---
id: "@specs/aws/lambda/docs/services-mq-errors"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Troubleshoot"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Troubleshoot

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/services-mq-errors
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Troubleshoot Amazon MQ event source mapping errors
<a name="services-mq-errors"></a>

When a Lambda function encounters an unrecoverable error, your Amazon MQ consumer stops processing records. Any other consumers can continue processing, provided that they do not encounter the same error. To determine the potential cause of a stopped consumer, check the `StateTransitionReason` field in the return details of your `EventSourceMapping` for one of the following codes:

**`ESM_CONFIG_NOT_VALID`**  
The event source mapping configuration is not valid.

**`EVENT_SOURCE_AUTHN_ERROR`**  
Lambda failed to authenticate the event source.

**`EVENT_SOURCE_AUTHZ_ERROR`**  
Lambda does not have the required permissions to access the event source.

**`FUNCTION_CONFIG_NOT_VALID`**  
The function's configuration is not valid.

Records also go unprocessed if Lambda drops them due to their size. The size limit for Lambda records is 6 MB. To redeliver messages upon function error, you can use a dead-letter queue (DLQ). For more information, see [Message Redelivery and DLQ Handling](https://activemq.apache.org/message-redelivery-and-dlq-handling) on the Apache ActiveMQ website and [Reliability Guide](https://www.rabbitmq.com/reliability.html) on the RabbitMQ website.

**Note**  
Lambda does not support custom redelivery policies. Instead, Lambda uses a policy with the default values from the [Redelivery Policy](https://activemq.apache.org/redelivery-policy) page on the Apache ActiveMQ website, with `maximumRedeliveries` set to 6.