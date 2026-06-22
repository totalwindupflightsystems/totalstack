---
id: "@specs/aws/opensearchserverless/docs/integrations-dynamodb"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Loading streaming data from Amazon DynamoDB"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Loading streaming data from Amazon DynamoDB

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/integrations-dynamodb
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Loading streaming data from Amazon DynamoDB
<a name="integrations-dynamodb"></a>

You can use AWS Lambda to send data to your OpenSearch Service domain from Amazon DynamoDB. New data that arrives in the database table triggers an event notification to Lambda, which then runs your custom code to perform the indexing.

## Prerequisites
<a name="integrations-dynamodb-prereq"></a>

Before proceeding, you must have the following resources.


| Prerequisite | Description | 
| --- | --- | 
| DynamoDB table | The table contains your source data. For more information, see [Basic Operations on DynamoDB Tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithTables.Basics.html) in the *Amazon DynamoDB Developer Guide*.<br />The table must reside in the same Region as your OpenSearch Service domain and have a stream set to **New image**. To learn more, see [Enabling a Stream](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html#Streams.Enabling). | 
| OpenSearch Service domain | The destination for data after your Lambda function processes it. For more information, see [Creating OpenSearch Service domains](createupdatedomains.md#createdomains). | 
| IAM role | This role must have basic OpenSearch Service, DynamoDB, and Lambda execution permissions, such as the following:  JSON   

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "es:ESHttpPost",
        "es:ESHttpPut",
        "dynamodb:DescribeStream",
        "dynamodb:GetRecords",
        "dynamodb:GetShardIterator",
        "dynamodb:ListStreams",
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "*"
    }
  ]
}
```    <br />The role must have the following trust relationship:  JSON   

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```    <br />To learn more, see [Creating IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html) in the *IAM User Guide*. | 

## Create the Lambda function
<a name="integrations-dynamodb-lambda"></a>

Follow the instructions in [Create the Lambda deployment package](integrations-s3-lambda.md#integrations-s3-lambda-deployment-package), but create a directory named `ddb-to-opensearch` and use the following code for `sample.py`:

```
import boto3
import requests
from requests_aws4auth import AWS4Auth

region = '' # e.g. us-east-1
service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

host = '' # the OpenSearch Service domain, e.g. https://search-mydomain.us-west-1.es.amazonaws.com
index = 'lambda-index'
datatype = '_doc'
url = host + '/' + index + '/' + datatype + '/'

headers = { "Content-Type": "application/json" }

def handler(event, context):
    count = 0
    for record in event['Records']:
        # Get the primary key for use as the OpenSearch ID
        id = record['dynamodb']['Keys']['id']['S']

        if record['eventName'] == 'REMOVE':
            r = requests.delete(url + id, auth=awsauth)
        else:
            document = record['dynamodb']['NewImage']
            r = requests.put(url + id, auth=awsauth, json=document, headers=headers)
        count += 1
    return str(count) + ' records processed.'
```

Edit the variables for `region` and `host`.

[Install pip](https://pip.pypa.io/en/stable/installation/) if you haven't already, then use the following commands to install your dependencies:

```
cd ddb-to-opensearch

pip install --target ./package requests
pip install --target ./package requests_aws4auth
```

Then follow the instructions in [Create the Lambda function](integrations-s3-lambda.md#integrations-s3-lambda-create), but specify the IAM role from [Prerequisites](#integrations-dynamodb-prereq) and the following settings for the trigger:
+ **Table**: your DynamoDB table
+ **Batch size**: 100
+ **Starting position**: Trim horizon

To learn more, see [Process New Items with DynamoDB Streams and Lambda](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.Lambda.Tutorial.html) in the *Amazon DynamoDB Developer Guide*.

At this point, you have a complete set of resources: a DynamoDB table for your source data, a DynamoDB stream of changes to the table, a function that runs after your source data changes and indexes those changes, and an OpenSearch Service domain for searching and visualization.

## Test the Lambda function
<a name="integrations-dynamodb-lambda-test"></a>

After you create the function, you can test it by adding a new item to the DynamoDB table using the AWS CLI:

```
aws dynamodb put-item --table-name test --item '{"director": {"S": "Kevin Costner"},"id": {"S": "00001"},"title": {"S": "The Postman"}}' --region {{us-west-1}}
```

Then use the OpenSearch Service console or OpenSearch Dashboards to verify that `lambda-index` contains a document. You can also use the following request:

```
GET https://{{domain-name}}/lambda-index/_doc/00001
{
    "_index": "lambda-index",
    "_type": "_doc",
    "_id": "00001",
    "_version": 1,
    "found": true,
    "_source": {
        "director": {
            "S": "Kevin Costner"
        },
        "id": {
            "S": "00001"
        },
        "title": {
            "S": "The Postman"
        }
    }
}
```