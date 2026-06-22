---
id: "@specs/aws/opensearchserverless/docs/integrations-fh"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Loading streaming data from Amazon Data Firehose"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Loading streaming data from Amazon Data Firehose

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/integrations-fh
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Loading streaming data from Amazon Data Firehose
<a name="integrations-fh"></a>

Firehose supports OpenSearch Service as a delivery destination. For instructions about how to load streaming data into OpenSearch Service, see [Creating a Kinesis Data Firehose Delivery Stream](https://docs.aws.amazon.com/firehose/latest/dev/basic-create.html) and [Choose OpenSearch Service for Your Destination](https://docs.aws.amazon.com/firehose/latest/dev/create-destination.html#create-destination-elasticsearch) in the *Amazon Data Firehose Developer Guide*.

Before you load data into OpenSearch Service, you might need to perform transforms on the data. To learn more about using Lambda functions to perform this task, see [Amazon Kinesis Data Firehose Data Transformation](https://docs.aws.amazon.com/firehose/latest/dev/data-transformation.html) in the same guide.

As you configure a delivery stream, Firehose features a "one-click" IAM role that gives it the resource access it needs to send data to OpenSearch Service, back up data on Amazon S3, and transform data using Lambda. Because of the complexity involved in creating such a role manually, we recommend using the provided role.