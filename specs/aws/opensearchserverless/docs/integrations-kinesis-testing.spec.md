---
id: "@specs/aws/opensearchserverless/docs/integrations-kinesis-testing"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Test the Lambda Function"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Test the Lambda Function

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/integrations-kinesis-testing
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Test the Lambda Function
<a name="integrations-kinesis-testing"></a>

After you create the function, you can test it by adding a new record to the data stream using the AWS CLI:

```
aws kinesis put-record --stream-name test --data "My test data." --partition-key partitionKey1 --region {{us-west-1}}
```

Then use the OpenSearch Service console or OpenSearch Dashboards to verify that `lambda-kine-index` contains a document. You can also use the following request:

```
GET https://{{domain-name}}/lambda-kine-index/_search
{
  "hits" : [
    {
      "_index": "lambda-kine-index",
      "_type": "_doc",
      "_id": "shardId-000000000000:49583511615762699495012960821421456686529436680496087042",
      "_score": 1,
      "_source": {
        "timestamp": 1523648740.051,
        "message": "My test data.",
        "id": "shardId-000000000000:49583511615762699495012960821421456686529436680496087042"
      }
    }
  ]
}
```