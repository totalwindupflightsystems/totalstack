---
id: "@specs/aws/opensearchserverless/docs/s3-opensearch-vector-bucket-integration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Import from Amazon S3 Vectors to OpenSearch Serverless"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Import from Amazon S3 Vectors to OpenSearch Serverless

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/s3-opensearch-vector-bucket-integration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Import from Amazon S3 Vectors to OpenSearch Serverless
<a name="s3-opensearch-vector-bucket-integration"></a>

Amazon S3 Vectors delivers the first cloud object store with native support to store and query vectors. S3 Vectors provides cost-effective, elastic, and durable vector storage that can be queried based on semantic meaning and similarity. It delivers sub-second query response times and up to 90% lower costs for uploading, storing, and querying vectors.

Amazon S3 Vectors introduces S3 vector buckets, which you can use to store, access, and query vector data without provisioning any infrastructure. Inside a vector bucket, you can organize your vector data within vector indexes. Your vector bucket can have multiple vector indexes, and each vector index can hold millions of vectors. For more information, see [Working with Amazon S3 Vectors and vector buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors.html) in the *Amazon S3 User Guide*. 

Each vector consists of:
+ A unique key
+ Vector data
+ Optional metadata in JSON format

Vector indexes support Euclidean and Cosine distance functions for similarity search operations.

**Note**  
The primary advantage of vector buckets is their ability to store massive datasets at extremely low cost while providing direct API access for vector operations.

For more information about Amazon S3 vector buckets, including how to create one, see [Working with Amazon S3 Vectors and vector buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors.html) in the *Amazon S3 User Guide*. For more information about integration with OpenSearch Service beyond what's described in this topic, see [Using S3 Vectors with OpenSearch Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-integrating-opensource.html)

You can use S3 Vectors with Amazon OpenSearch Service to lower the cost of vector storage when queries are less frequent, and then quickly move those datasets to OpenSearch as demands increase or to enhance search capabilities. 

OpenSearch Service integrates with Amazon S3 Vectors to provide enhanced performance and functionality beyond what Amazon S3 vector buckets offer by themselves. Consider this integration when you need:
+ Higher query throughput
+ Sub-second search latency
+ Advanced analytics capabilities like aggregations
+ Hybrid search combining text and vector data

This integration is particularly useful when multiple applications consume the same vector data with different performance requirements. You can have some applications interact directly with Amazon S3 vector buckets for cost-sensitive use cases, while others leverage OpenSearch integration for performance-critical operations.

## Integration architecture
<a name="vector-search-integration-architecture"></a>

The integration uses Amazon OpenSearch Ingestion (OSI) as the data pipeline between Amazon S3 vector indexes and Amazon OpenSearch Serverless vector collections. OpenSearch Ingestion automatically exports vector data from your specified vector index and ingests it into OpenSearch Serverless vector collections for high-performance search operations.

**Note**  
After export, your data is still present in the S3 vector index. You have two copies of the data.

Each vector index maps to a corresponding index in the OpenSearch Serverless collection. The integration:
+ Preserves vector dimensions
+ Retains metadata
+ Optimizes data structure for OpenSearch's vector search capabilities

After configuration, OpenSearch Ingestion begins the data export process by consuming vectors from the specified vector index using the Amazon S3 ListVectors API. The service processes vectors in parallel to optimize ingestion speed while respecting the scaling limits of both OpenSearch Ingestion and Amazon OpenSearch Serverless.

During ingestion, the service:
+ Transforms vector data to match the expected format for OpenSearch Service
+ Preserves essential information including vector values, metadata, and distance metrics
+ Handles failure scenarios through intelligent retry mechanisms
+ Places problematic records in an Amazon S3 bucket used as a dead letter queue for later analysis

The integration handles massive datasets efficiently, with performance depending on vector dimensions, dataset size, and configured scaling limits. OSI can scale up to 16 workers per pipeline, while OpenSearch Serverless automatically adjusts capacity based on ingestion demands. By default, OpenSearch increases the `maxSearch` OpenSearch Computational Unit (OCU) on the OpenSearch Serverless side to 100.

**Note**  
The integration prioritizes cost efficiency through:  
Automatic pipeline shutdown after export completion
OpenSearch Serverless collection scaling
Pay-per-use resource model

## Required IAM permissions
<a name="vector-search-iam-permissions"></a>

The integration requires careful configuration of IAM permissions to enable secure communication between services. OpenSearch Ingestion needs permissions to read from Amazon S3 vector indexes, write to OpenSearch Service vector collections, and manage associated security policies.

When you enable integration using the procedure later in this topic, you can choose one of the following options for permissions management:
+ Allow the system to automatically create a service role with the necessary permissions
+ Provide an existing role that meets the requirements

The automatically created role includes policies for:
+ Accessing Amazon S3 vector index APIs
+ Managing OpenSearch Service collection operations
+ Handling dead letter queue operations for failed ingestion attempts

If you choose to specify an existing role, verify that the role has the following IAM permissions:

**(Required)**: Data pipeline permissions between OpenSearch Ingestion and OpenSearch Serverless

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "allowAPIs",
            "Effect": "Allow",
            "Action": [ "aoss:APIAccessAll", "aoss:BatchGetCollection" ],
            "Resource": [ "arn:aws:aoss:*:{{111122223333}}:collection/{{collection-id}}" ]
        },
        {
            "Sid": "allowSecurityPolicy",
            "Effect": "Allow",
            "Action": [
                "aoss:CreateSecurityPolicy",
                "aoss:UpdateSecurityPolicy",
                "aoss:GetSecurityPolicy"
            ],
            "Resource": "*",
            "Condition":{
               "StringLike":{
                  "aoss:collection": [ "{{collection-name}}" ]
                },
               "StringEquals": {
                  "aws:ResourceAccount": [ "{{111122223333}}" ]
               }
            }
        }
    ]
}
```

------

**(Required)**: Data ingestion permissions between OpenSearch Ingestion and Amazon S3 dead-letter queue

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "s3Access",
            "Effect": "Allow",
            "Action": [
              "s3:PutObject"
            ],
            "Resource": [ "arn:aws:s3:::{{bucket}}/*" ]
        }
    ]
}
```

------

**(Required)**: Data ingestion permissions between OpenSearch Ingestion and Amazon S3 Vectors

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowS3VectorIndexAccess",
            "Effect": "Allow",
            "Action": [
               "s3vectors:ListVectors",
               "s3vectors:GetVectors"
            ],
            "Resource": [
                "arn:aws:s3vectors:{{us-east-1}}:{{111122223333}}:bucket/{{bucket-name}}/index/{{index-name}}"
            ]
        }
    ]
}
```

------

**(Required if AWS KMS encryption is enabled)**: Decryption permissions for communication between OpenSearch Ingestion and Amazon S3 Vectors

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "allowS3VectorDecryptionOfCustomManagedKey",
            "Effect": "Allow",
            "Action": [
                "kms:Decrypt"
            ],
            "Resource": [ "arn:aws:kms:{{us-east-1}}:{{111122223333}}:key/{{key-id}}" ],
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": "s3vectors.us-east-1.amazonaws.com",
                    "kms:EncryptionContext:aws:s3vectors:arn": [
                        "arn:aws:s3vectors:{{us-east-1}}:{{111122223333}}:bucket/example-bucket",
                        "arn:aws:s3vectors:{{us-east-1}}:{{111122223333}}:bucket/example-bucket/index/example-index"
                        ]
                 }
             }
        }
    ]
}
```

------

## Configuring Amazon S3 Vectors integration with OpenSearch
<a name="vector-search-configuring-integration"></a>

Use the following procedure to configure Amazon S3 Vectors integration with OpenSearch Serverless.

**Note**  
If you started the process of configuring integration from the Amazon S3 console by choosing the **Export to OpenSearch** option in the **Vector buckets** page, some of the steps in the following procedure aren't applicable, as noted in the procedure.

**To configure Amazon S3 Vectors integration with OpenSearch Serverless**

1. Open the **Import S3 vector index to OpenSearch vector engine** page in the Amazon OpenSearch Service console. The page automatically displays if you clicked **Export to OpenSearch** in the Amazon S3 console. If you are starting in the OpenSearch console, choose **Integration** in the left navigation and then choose **Import S3 vector index**.

1. In the **Source** section, if you started in the Amazon S3 console, verify that the name of vector index and its Amazon Resource Name (ARN) are already specified. If you started in the OpenSearch console, enter the index ARN in the **S3 vector index ARN** field.

1. In the **Service access** section, choose an option. If you choose an existing role, verify it has all required permissions for integration as described in [Required IAM permissions](#vector-search-iam-permissions).

1. (Optional) Expand **Additional settings**. For **Enable redundancy (active replicas)** we recommend leaving this option selected for production environments. When you create your first collection, OpenSearch Serverless instantiates two OCUs—one for indexing and one for search. To ensure high availability, it also launches a standby set of nodes in another Availability Zone. For development and testing purposes, you can disable the **Enable redundancy** setting for a collection, which eliminates the two standby replicas and only instantiates two OCUs. By default, the redundant active replicas are enabled, which means that a total of four OCUs are instantiated for the first collection in an account.

   For **Add customer-managed AWS KMS key for Amazon OpenSearch Serverless vector**, choose this option to encrypt data in the vector collection using a customer managed key. By default, OpenSearch uses an AWS managed key.

1. If you started this process by clicking the **Export to OpenSearch** option in the Amazon S3 console, the **Export details** section lists the steps OpenSearch will take next. When you're ready, choose **Export**.

   If you started this process in the OpenSearch Service console, the **Import details** section lists the steps OpenSearch will take next. When you're ready, choose **Import**.

   OpenSearch opens the history page to display all exports/imports of Amazon S3 vector indexes to OpenSearch Serverless indexes.

After successful ingestion, OSI automatically stops the pipeline to prevent unnecessary costs while maintaining exported data in OpenSearch. You can monitor integration progress through CloudWatch metrics and access detailed logs for troubleshooting.

The OpenSearch collection remains active and available for queries after initial ingestion is completed. You can perform:
+ Similarity searches
+ Aggregations
+ Analytics operations