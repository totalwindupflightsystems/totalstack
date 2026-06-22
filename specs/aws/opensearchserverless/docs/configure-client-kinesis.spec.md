---
id: "@specs/aws/opensearchserverless/docs/configure-client-kinesis"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Amazon Kinesis Data Streams"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Amazon Kinesis Data Streams

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/configure-client-kinesis
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Use an OpenSearch Ingestion pipeline with Amazon Kinesis Data Streams
<a name="configure-client-kinesis"></a>

Use an OpenSearch Ingestion pipeline with Amazon Kinesis Data Streams to ingest stream records data from multiple streams into Amazon OpenSearch Service domains and collections. The OpenSearch Ingestion pipeline incorporates the streaming ingestion infrastructure to provide a high-scale, low latency way to continuously ingest stream records from Kinesis.

**Topics**
+ [Amazon Kinesis Data Streams as a source](#confluent-cloud-kinesis)
+ [Amazon Kinesis Data Streams cross account as a source](#kinesis-cross-account-source)

## Amazon Kinesis Data Streams as a source
<a name="confluent-cloud-kinesis"></a>

With the following procedure, you'll learn how to set up an OpenSearch Ingestion pipeline that uses Amazon Kinesis Data Streams as the data source. This section covers the necessary prerequisites, such as creating an OpenSearch Service domain or an OpenSearch Serverless Collection, and walking through the steps to configure the pipeline role and create the pipeline.

### Prerequisites
<a name="s3-prereqs"></a>

To set up your pipeline, you need one or more active Kinesis Data Streams. These streams must be either receiving records or ready to receive records from other sources. For more information, see [Overview of OpenSearch Ingestion](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/osis-getting-started-tutorials.html).

**To set up your pipeline**

1. 

**Create an OpenSearch Service domain or an OpenSearch Serverless collection**

   To create a domain or a collection, see [Getting started with OpenSearch Ingestion](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/osis-getting-started-tutorials.html).

   To create an IAM role with the correct permissions to access write data to the collection or domain, see [Resource-based policies](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ac.html#ac-types-resource).

1. 

**Configure the pipeline role with permissions**

   [Set up the pipeline role](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/pipeline-security-overview.html#pipeline-security-sink) that you want to use in your pipeline configuration and add the following permissions to it. Replace the {{placeholder values}} with your own information.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Sid": "allowReadFromStream",
               "Effect": "Allow",
               "Action": [
                   "kinesis:DescribeStream",
                   "kinesis:DescribeStreamConsumer",
                   "kinesis:DescribeStreamSummary",
                   "kinesis:GetRecords",
                   "kinesis:GetShardIterator",
                   "kinesis:ListShards",
                   "kinesis:ListStreams",
                   "kinesis:ListStreamConsumers",
                   "kinesis:RegisterStreamConsumer",
                   "kinesis:SubscribeToShard"
               ],
               "Resource": [
                   "arn:aws:kinesis:{{us-east-1}}:{{111122223333}}:stream/{{stream-name}}"
               ]
           }
       ]
   }
   ```

------

   If server-side encryption is enabled on the streams, the following AWS KMS policy allows to decrypt the records. Replace the {{placeholder values}} with your own information.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Sid": "allowDecryptionOfCustomManagedKey",
               "Effect": "Allow",
               "Action": [
                   "kms:Decrypt",
                   "kms:GenerateDataKey"
               ],
               "Resource": "arn:aws:kms:{{us-east-1}}:{{111122223333}}:key/{{key-id}}"
           }
       ]
   }
   ```

------

   In order for a pipeline to write data to a domain, the domain must have a [domain-level access policy](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ac.html#ac-types-resource) that allows the **sts\_role\_arn** pipeline role to access it.

   The following example is a domain access policy that allows the pipeline role created in the previous step (`pipeline-role`), to write data to the `ingestion-domain` domain. Replace the {{placeholder values}} with your own information.

   ```
   {
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": {
           "AWS": "arn:aws:iam::{{your-account-id}}:role/{{pipeline-role}}"
         },
         "Action": ["es:DescribeDomain", "es:ESHttp*"],
         "Resource": "arn:aws:es:{{AWS Region}}:{{account-id}}:domain/{{domain-name}}/*"
       }
     ]
   }
   ```

1. 

**Create the pipeline**

   Configure an OpenSearch Ingestion pipeline specifying **Kinesis-data-streams** as the source. You can locate a ready made blueprint available on the OpenSearch Ingestion Console for creating such a pipeline. (Optional) To create the pipeline using the AWS CLI, you can use a blueprint named "**`AWS-KinesisDataStreamsPipeline`**". Replace the {{placeholder values}} with your own information.

   ```
   version: "2"
   kinesis-pipeline:
     source:
       kinesis_data_streams:
         acknowledgments: true
         codec:
           # Based on whether kinesis records are aggregated or not, you could choose json, newline or ndjson codec for processing the records.
           # JSON codec supports parsing nested CloudWatch Events into individual log entries that will be written as documents into OpenSearch.
           # json:
             # key_name: "logEvents"
             # These keys contain the metadata sent by CloudWatch Subscription Filters
             # in addition to the individual log events:
             # include_keys: [ 'owner', 'logGroup', 'logStream' ]
           newline:
         streams:
           - stream_name: "{{stream name}}"
             # Enable this if ingestion should start from the start of the stream.
             # initial_position: "EARLIEST"
             # checkpoint_interval: "PT5M"
             # Compression will always be gzip for CloudWatch, but will vary for other sources:
             # compression: "gzip"
           - stream_name: "{{stream name}}"
             # Enable this if ingestion should start from the start of the stream.
             # initial_position: "EARLIEST"
             # checkpoint_interval: "PT5M"
             # Compression will always be gzip for CloudWatch, but will vary for other sources:
             # compression: "gzip"
   
           # buffer_timeout: "1s"
           # records_to_accumulate: 100
           # Change the consumer strategy to "polling". Default consumer strategy will use enhanced "fan-out" supported by KDS.
           # consumer_strategy: "polling"
           # if consumer strategy is set to "polling", enable the polling config below.
           # polling:
             # max_polling_records: 100
             # idle_time_between_reads: "250ms"
         aws:
           # Provide the Role ARN with access to Amazon Kinesis Data Streams. This role should have a trust relationship with osis-pipelines.amazonaws.com
           sts_role_arn: "{{arn:aws:iam::111122223333:role/Example-Role}}"
           # Provide the AWS Region of the Data Stream.
           region: "{{us-east-1}}"
   
     sink:
       - opensearch:
           # Provide an Amazon OpenSearch Serverless domain endpoint
           hosts: [ "{{https://search-mydomain-1a2a3a4a5a6a7a8a9a0a9a8a7a.us-east-1.es.amazonaws.com}}" ]
           index: "index_${getMetadata(\"stream_name\")}"
           # Ensure adding unique document id as a combination of the metadata attributes available.
           document_id: "${getMetadata(\"partition_key\")}_${getMetadata(\"sequence_number\")}_${getMetadata(\"sub_sequence_number\")}"
           aws:
             # Provide a Role ARN with access to the domain. This role should have a trust relationship with osis-pipelines.amazonaws.com
             sts_role_arn: "{{arn:aws:iam::111122223333:role/Example-Role}}"
             # Provide the AWS Region of the domain.
             region: "{{us-east-1}}"
             # Enable the 'serverless' flag if the sink is an Amazon OpenSearch Serverless collection
             serverless: false
             # serverless_options:
               # Specify a name here to create or update network policy for the serverless collection
               # network_policy_name: "network-policy-name"
           # Enable the 'distribution_version' setting if the OpenSearch Serverless domain is of version Elasticsearch 6.x
           # distribution_version: "es6"
           # Enable and switch the 'enable_request_compression' flag if the default compression setting is changed in the domain. See https://docs.aws.amazon.com/opensearch-service/latest/developerguide/gzip.html
           # enable_request_compression: true/false
           # Optional: Enable the S3 DLQ to capture any failed requests in an S3 bucket. Delete this entire block if you don't want a DLQ.
           dlq:
             s3:
               # Provide an S3 bucket
               bucket: "{{your-dlq-bucket-name}}"
               # Provide a key path prefix for the failed requests
               # key_path_prefix: "kinesis-pipeline/logs/dlq"
               # Provide the region of the bucket.
               region: "{{us-east-1}}"
               # Provide a Role ARN with access to the bucket. This role should have a trust relationship with osis-pipelines.amazonaws.com
               sts_role_arn: "{{arn:aws:iam::111122223333:role/Example-Role}}"
   ```

**Configuration options**  
For Kinesis configuration options, see [Configuration options](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/kinesis/#configuration-options) in the *OpenSearch* documentation.

**Available metadata attributes**
   + **stream\_name** – Name of the Kinesis Data Streams from where the record has been ingested
   + **partition\_key** – Partition key of the Kinesis Data Streams record which is being ingested
   + **sequence\_number** – Sequence number of the Kinesis Data Streams record which is being ingested
   + **sub\_sequence\_number** – Sub sequence number of the Kinesis Data Streams record which is being ingested

1. 

**(Optional) Configure recommended compute units (OCUs) for the Kinesis Data Streams pipeline**

   An OpenSearch Kinesis Data Streams source pipeline can also be configured to ingest stream records from more than one stream. For faster ingestion, we recommend you add an additional compute unit per new stream added.

### Data consistency
<a name="confluent-cloud-kinesis-private"></a>

OpenSearch Ingestion supports end-to-end acknowledgement to ensure data durability. When the pipeline reads stream records from Kinesis, it dynamically distributes the work of reading stream records based on the shards associated with the streams. Pipeline will automatically checkpoint streams when it receives an acknowledgement after ingesting all records in the OpenSearch domain or collection. This will avoid duplicate processing of stream records.

To create the index based on the stream name, define the index in the opensearch sink section as **"index\_${getMetadata(\\"stream\_name\\")}"**.

## Amazon Kinesis Data Streams cross account as a source
<a name="kinesis-cross-account-source"></a>

You can grant access across accounts with Amazon Kinesis Data Streams so that OpenSearch Ingestion pipelines can access Kinesis Data Streams in another account as source. Complete the following steps to enable cross-account access:

**Configure cross-account access**

1. 

**Set resource policy in the account which has the Kinesis stream**

   Replace the {{placeholder values}} with your own information.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Sid": "StreamReadStatementID",
               "Effect": "Allow",
               "Principal": {
                   "AWS": "arn:aws:iam::{{111122223333}}:role/Pipeline-Role"
               },
               "Action": [
                   "kinesis:DescribeStreamSummary",
                   "kinesis:GetRecords",
                   "kinesis:GetShardIterator",
                   "kinesis:ListShards"
               ],
               "Resource": "arn:aws:kinesis:{{us-east-1}}:{{444455556666}}:stream/stream-name"
           },
           {
               "Sid": "StreamEFOReadStatementID",
               "Effect": "Allow",
               "Principal": {
                   "AWS": "arn:aws:iam::{{111122223333}}:role/Pipeline-Role"
               },
               "Action": [
                   "kinesis:DescribeStreamSummary",
                   "kinesis:ListShards"
               ],
               "Resource": "arn:aws:kinesis:{{us-east-1}}:{{444455556666}}:stream/{{stream-name}}/consumer/{{consumer-name}}"
           }
       ]
   }
   ```

------

1. 

**(Optional) Setup Consumer and Consumer Resource Policy**

   This is an optional step and will only be required if you plan to use Enhanced Fanout Consumer strategy for reading stream records. For more information, see [Develop enhanced fan-out consumers with dedicated throughput](https://docs.aws.amazon.com/streams/latest/dev/enhanced-consumers.html).

   1. 

**Setup consumer**

      To reuse an existing consumer, you can skip this step. For more information, see [RegisterStreamConsumer](https://docs.aws.amazon.com/dms/latest/APIReference/API_RegisterStreamConsumer.html) in the *Amazon Kinesis Data Streams API Reference*.

      In the following example CLI command, replace the {{placeholder values}} with your own information.  
**Example : Example CLI command**  

      ```
      aws kinesis register-stream-consumer \
      --stream-arn "arn:aws:kinesis:{{AWS Region}}:{{account-id}}:stream/{{stream-name}}" \
      --consumer-name {{consumer-name}}
      ```

   1. 

**Setup Consumer Resource Policy**

      In the following statement, replace the {{placeholder values}} with your own information.

------
#### [ JSON ]

****  

      ```
      {
          "Version":"2012-10-17",		 	 	 
          "Statement": [
              {
                  "Sid": "ConsumerEFOReadStatementID",
                  "Effect": "Allow",
                  "Principal": {
                      "AWS": "{{arn:aws:iam::111122223333:role/Pipeline-Role}}"
                  },
                  "Action": [
                      "kinesis:DescribeStreamConsumer",
                      "kinesis:SubscribeToShard"
                  ],
                  "Resource": "arn:aws:kinesis:{{us-east-1}}:{{444455556666}}:stream/{{stream-1}}/consumer/{{consumer-name}}"
              }
          ]
      }
      ```

------

1. 

**Pipeline Configuration**

   For cross account ingestion, add the following attributes under `kinesis_data_streams` for each stream:
   + `stream_arn` - the arn of the stream belonging to the account where the stream exists
   + `consumer_arn` - this is an optional attribute and must be specified if the default enhanced fanout consumer strategy is chosen. Specify the actual consumer arn for this field. Replace the {{placeholder values}} with your own information.

   ```
   version: "2"
        kinesis-pipeline:
          source:
            kinesis_data_streams:
              acknowledgments: true
              codec:
                newline:
              streams:
                - stream_arn: "arn:aws:kinesis:{{region}}:{{stream-account-id}}:stream/{{stream-name}}"
                  consumer_arn: "{{consumer arn}}"
                  # Enable this if ingestion should start from the start of the stream.
                  # initial_position: "EARLIEST"
                  # checkpoint_interval: "PT5M"
                - stream_arn: "arn:aws:kinesis:{{region}}:{{stream-account-id}}:stream/{{stream-name}}"
                  consumer_arn: "{{consumer arn}}"
                   # initial_position: "EARLIEST"
        
                # buffer_timeout: "1s"
                # records_to_accumulate: 100
                # Enable the consumer strategy to "polling". Default consumer strategy will use enhanced "fan-out" supported by KDS.
                # consumer_strategy: "polling"
                # if consumer strategy is set to "polling", enable the polling config below.
                # polling:
                  # max_polling_records: 100
                  # idle_time_between_reads: "250ms"
              aws:
                # Provide the Role ARN with access to Kinesis. This role should have a trust relationship with osis-pipelines.amazonaws.com
                sts_role_arn: "arn:aws:iam::{{111122223333}}:role/{{Example-Role}}"
                # Provide the AWS Region of the domain.
                region: "{{us-east-1}}"
        
          sink:
            - opensearch:
                # Provide an OpenSearch Serverless domain endpoint
                hosts: [ "{{https://search-mydomain-1a2a3a4a5a6a7a8a9a0a9a8a7a.us-east-1.es.amazonaws.com}}" ]
                index: "index_${getMetadata(\"stream_name\")}"
                # Mapping for documentid based on partition key, shard sequence number and subsequence number metadata attributes
                document_id: "${getMetadata(\"partition_key\")}_${getMetadata(\"sequence_number\")}_${getMetadata(\"sub_sequence_number\")}"
                aws:
                  # Provide a Role ARN with access to the domain. This role should have a trust relationship with osis-pipelines.amazonaws.com
                  sts_role_arn: "arn:aws:iam::111122223333:role/{{Example-Role}}"
                  # Provide the AWS Region of the domain.
                  region: "{{us-east-1}}"
                  # Enable the 'serverless' flag if the sink is an OpenSearch Serverless collection
                  serverless: false
                    # serverless_options:
                    # Specify a name here to create or update network policy for the serverless collection
                  # network_policy_name: {{network-policy-name}}
                # Enable the 'distribution_version' setting if the OpenSearch Serverless domain is of version Elasticsearch 6.x
                # distribution_version: "es6"
                # Enable and switch the 'enable_request_compression' flag if the default compression setting is changed in the domain. See https://docs.aws.amazon.com/opensearch-service/latest/developerguide/gzip.html
                # enable_request_compression: true/false
                # Optional: Enable the S3 DLQ to capture any failed requests in an S3 bucket. Delete this entire block if you don't want a DLQ.
                dlq:
                  s3:
                    # Provide an Amazon S3 bucket
                    bucket: "{{your-dlq-bucket-name}}"
                    # Provide a key path prefix for the failed requests
                    # key_path_prefix: "{{alb-access-log-pipeline/logs/dlq}}"
                    # Provide the AWS Region of the bucket.
                    region: "{{us-east-1}}"
                    # Provide a Role ARN with access to the bucket. This role should have a trust relationship with osis-pipelines.amazonaws.com
                    sts_role_arn: "{{arn:aws:iam::111122223333:role/Example-Role}}"
   ```

1. 

**OSI Pipeline Role Kinesis Data Streams**

   1. 

**IAM Policy**

      Add the following policy to the pipeline role. Replace the {{placeholder values}} with your own information.

------
#### [ JSON ]

****  

      ```
      {
          "Version":"2012-10-17",		 	 	 
          "Statement": [
              {
                  "Effect": "Allow",
                  "Action": [
                      "kinesis:DescribeStreamConsumer",
                      "kinesis:SubscribeToShard"
                  ],
                  "Resource": [
                  "arn:aws:kinesis:{{us-east-1}}:{{111122223333}}:stream/my-stream"
                  ]
              },
              {
                  "Sid": "allowReadFromStream",
                  "Effect": "Allow",
                  "Action": [
                      "kinesis:DescribeStream",
                      "kinesis:DescribeStreamSummary",
                      "kinesis:GetRecords",
                      "kinesis:GetShardIterator",
                      "kinesis:ListShards",
                      "kinesis:ListStreams",
                      "kinesis:ListStreamConsumers",
                      "kinesis:RegisterStreamConsumer"
                  ],
                  "Resource": [
                      "arn:aws:kinesis:{{us-east-1}}:{{111122223333}}:stream/my-stream"
                  ]
              }
          ]
      }
      ```

------

   1. 

**Trust Policy**

      In order to ingest data from the stream account, you will need to establish a trust relationship between the pipeline ingestion role and the stream account. Add the following to the pipeline role. Replace the {{placeholder values}} with your own information.

------
#### [ JSON ]

****  

      ```
      {
        "Version":"2012-10-17",		 	 	 
        "Statement": [{
           "Effect": "Allow",
           "Principal": {
             "AWS": "{{arn:aws:iam::111122223333:root}}"
            },
           "Action": "sts:AssumeRole"
        }]
      }
      ```

------