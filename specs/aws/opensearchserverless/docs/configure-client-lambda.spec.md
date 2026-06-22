---
id: "@specs/aws/opensearchserverless/docs/configure-client-lambda"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AWS Lambda"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# AWS Lambda

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/configure-client-lambda
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Using an OpenSearch Ingestion pipeline with AWS Lambda
<a name="configure-client-lambda"></a>

Use the [AWS Lambda processor](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/aws-lambda/) to enrich data from any source or destination supported by OpenSearch Ingestion using custom code. With the Lambda processor, you can apply your own data transformations or enrichments and then return the processed events back to your pipeline for further processing. This processor enables customized data processing and gives you full control over how data is manipulated before it moves through the pipeline.

**Note**  
The payload size limit for a single event processed by a Lambda processor is 5 MB. Additionally, the Lambda processor only supports responses in JSON array format.

## Prerequisites
<a name="configure-clients-lambda-prereqs"></a>

Before you create a pipeline with a Lambda processor, create the following resources:
+ An AWS Lambda function that enriches and transforms your source data. For instructions, see [Create your first Lambda function](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html).
+ An OpenSearch Service domain or OpenSearch Serverless collection that will be the pipeline sink. For more information, see [Creating OpenSearch Service domains](createupdatedomains.md#createdomains) and [Creating collections](serverless-create.md).
+ A pipeline role that includes permissions to write to the domain or collection sink. For more information, see [Pipeline role](pipeline-security-overview.md#pipeline-security-sink).

  The pipeline role also needs an attached permissions policy that allows it to invoke the Lambda function specified in the pipeline configuration. For example: 

------
#### [ JSON ]

****  

  ```
  {
      "Version":"2012-10-17",		 	 	 
      "Statement": [
          {
              "Sid": "allowinvokeFunction",
              "Effect": "Allow",
              "Action": [
                  "lambda:invokeFunction",
                  "lambda:InvokeAsync",
                  "lambda:ListFunctions"
              ],
              "Resource": "arn:aws:lambda:{{us-east-1}}:{{111122223333}}:function:{{function-name}}"
              
          }
      ]
  }
  ```

------

## Create a pipeline
<a name="configure-clients-security-lake-pipeline-role"></a>

To use AWS Lambda as a processor, configure an OpenSearch Ingestion pipeline and specify `aws_lambda` as a processor. You can also use the **AWS Lambda custom enrichment** blueprint to create the pipeline. For more information, see [Working with blueprints](pipeline-blueprint.md).

The following example pipeline receives data from an HTTP source, enriches it using a date processor and the AWS Lambda processor, and ingests the processed data to an OpenSearch domain.

```
version: "2"
lambda-processor-pipeline:
  source:
    http:
      path: "/${pipelineName}/logs"
  processor:
      - date:
        destination: "@timestamp"
        from_time_received: true
    - aws_lambda:
        function_name: "my-lambda-function"

        tags_on_failure: ["lambda_failure"]
        batch:
            key_name: "events"
        aws:
          region: {{region}}
  sink:
    - opensearch:
        hosts: [ "https://search-{{mydomain}}.{{us-east-1}}es.amazonaws.com" ]
        index: "table-index"
        aws:
          region: "{{region}}"
          serverless: false
```

The following example AWS Lambda function transforms incoming data by adding a new key-value pair (`"transformed": "true"`) to each element in the provided array of events, and then sends back the modified version.

```
import json

def lambda_handler(event, context):
    input_array = event.get('events', [])
    output = []
    for input in input_array:
        input["transformed"] = "true";
        output.append(input)

    return output
```

## Batching
<a name="configure-clients-lambda-batching"></a>

Pipelines send batched events to the Lambda processor, and dynamically adjusts the batch size to ensure it stays below the 5 MB limit.

The following is an example of a pipeline batch:

```
batch:
    key_name: "events"

input_arrary = event.get('events', [])
```

**Note**  
When you create a pipeline, make sure the `key_name` option in the Lambda processor configuration matches the event key in the Lambda handler.

## Conditional filtering
<a name="configure-clients-lambda-conditional-filtering"></a>

Conditional filtering allows you to control when your AWS Lambda processor invokes the Lambda function based on specific conditions in event data. This is particularly useful when you want to selectively process certain types of events while ignoring others.

The following example configuration uses conditional filtering:

```
processors:
  - aws_lambda:
      function_name: "my-lambda-function"
      aws:
        region: "region"
      lambda_when: "/sourceIp == 10.10.10.10"
```