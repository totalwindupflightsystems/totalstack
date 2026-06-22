---
id: "@specs/aws/opensearchserverless/docs/integrations-kinesis-lambda"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Create the Lambda function"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Create the Lambda function

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/integrations-kinesis-lambda
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Create the Lambda function
<a name="integrations-kinesis-lambda"></a>

Follow the instructions in [Create the Lambda deployment package](integrations-s3-lambda.md#integrations-s3-lambda-deployment-package), but create a directory named `kinesis-to-opensearch` and use the following code for `sample.py`:

```
import base64
import boto3
import json
import requests
from requests_aws4auth import AWS4Auth

region = '' # e.g. us-west-1
service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

host = '' # the OpenSearch Service domain, e.g. https://search-mydomain.us-west-1.es.amazonaws.com
index = 'lambda-kine-index'
datatype = '_doc'
url = host + '/' + index + '/' + datatype + '/'

headers = { "Content-Type": "application/json" }

def handler(event, context):
    count = 0
    for record in event['Records']:
        id = record['eventID']
        timestamp = record['kinesis']['approximateArrivalTimestamp']

        # Kinesis data is base64-encoded, so decode here
        message = base64.b64decode(record['kinesis']['data'])

        # Create the JSON document
        document = { "id": id, "timestamp": timestamp, "message": message }
        # Index the document
        r = requests.put(url + id, auth=awsauth, json=document, headers=headers)
        count += 1
    return 'Processed ' + str(count) + ' items.'
```

Edit the variables for `region` and `host`.

[Install pip](https://pip.pypa.io/en/stable/installation/) if you haven't already, then use the following commands to install your dependencies:

```
cd kinesis-to-opensearch

pip install --target ./package requests
pip install --target ./package requests_aws4auth
```

Then follow the instructions in [Create the Lambda function](integrations-s3-lambda.md#integrations-s3-lambda-create), but specify the IAM role from [Prerequisites](integrations-kinesis.md#integrations-kinesis-lambda-prereq) and the following settings for the trigger:
+ **Kinesis stream**: your Kinesis stream
+ **Batch size**: 100
+ **Starting position**: Trim horizon

To learn more, see [What is Amazon Kinesis Data Streams?](https://docs.aws.amazon.com/streams/latest/dev/working-with-kinesis.html) in the *Amazon Kinesis Data Streams Developer Guide*.

At this point, you have a complete set of resources: a Kinesis data stream, a function that runs after the stream receives new data and indexes that data, and an OpenSearch Service domain for searching and visualization.