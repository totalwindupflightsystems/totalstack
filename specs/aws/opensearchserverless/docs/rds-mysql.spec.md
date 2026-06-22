---
id: "@specs/aws/opensearchserverless/docs/rds-mysql"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RDS for MySQL"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# RDS for MySQL

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/rds-mysql
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RDS for MySQL
<a name="rds-mysql"></a>

Complete the following steps to configure an OpenSearch Ingestion pipeline with Amazon RDS for RDS for MySQL.

**Topics**
+ [RDS for MySQL prerequisites](#rds-mysql-prereqs)
+ [Step 1: Configure the pipeline role](#rds-mysql-pipeline-role)
+ [Step 2: Create the pipeline](#rds-mysql-pipeline)
+ [Data consistency](#rds-mysql-pipeline-consistency)
+ [Mapping data types](#rds-mysql-pipeline-mapping)
+ [Limitations](#rds-mysql-pipeline-limitations)
+ [Recommended CloudWatch Alarms](#aurora-mysql-pipeline-metrics)

## RDS for MySQL prerequisites
<a name="rds-mysql-prereqs"></a>

Before you create your OpenSearch Ingestion pipeline, perform the following steps:

1. Create a custom DB parameter group in Amazon RDS to configure binary logging and set the following parameters.

   ```
   binlog_format=ROW
   binlog_row_image=full
   binlog_row_metadata=FULL
   ```

   Additionally, make sure the `binlog_row_value_options` parameter is not set to `PARTIAL_JSON`.

   For more information, see [Configuring RDS for MySQL binary logging](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.MySQL.BinaryFormat.html).

1. [Select or create an RDS for MySQL DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateDBInstance.html) and associate the parameter group created in the previous step with the DB instance.

1. Verify that automated backups are enabled on the database. For more information, see [Enabling automated backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.Enabling.html). 

1. Configure binary log retention with enough time for replication to occur, for example 24 hours. For more information, see [Setting and showing binary log configuration](https://docs.aws.amazon.com//AmazonRDS/latest/UserGuide/mysql-stored-proc-configuring.html) in the *Amazon RDS User Guide*.

1. Set up username and password authentication on your Amazon RDS instance using [password management with Amazon RDS and AWS Secrets Manager](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-secrets-manager.html). You can also create a username/password combination by [creating a Secrets Manager secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html).

1. If you use the full initial snapshot feature, create an AWS KMS key and an IAM role for exporting data from Amazon RDS to Amazon S3.

   The IAM role should have the following permission policy:

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Sid": "ExportPolicy",
               "Effect": "Allow",
               "Action": [
                   "s3:PutObject*",
                   "s3:ListBucket",
                   "s3:GetObject*",
                   "s3:DeleteObject*",
                   "s3:GetBucketLocation"
               ],
               "Resource": [
                   "arn:aws:s3:::{{s3-bucket-used-in-pipeline}}",
                   "arn:aws:s3:::{{s3-bucket-used-in-pipeline}}/*"
               ]
           }
       ]
   }
   ```

------

   The role should also have the following trust relationships:

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Principal": {
                   "Service": "export.rds.amazonaws.com"
               },
               "Action": "sts:AssumeRole"
           }
       ]
   }
   ```

------

1. Select or create an OpenSearch Service domain or OpenSearch Serverless collection. For more information, see [Creating OpenSearch Service domains](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html#createdomains) and [Creating collections](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html#serverless-create).

1. Attach a [resource-based policy](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ac.html#ac-types-resource) to your domain or a [data access policy](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-data-access.html) to your collection. These access policies allow OpenSearch Ingestion to write data from your Amazon RDS DB instance to your domain or collection.

## Step 1: Configure the pipeline role
<a name="rds-mysql-pipeline-role"></a>

After you have your Amazon RDS pipeline prerequisites set up, [configure the pipeline role](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/pipeline-security-overview.html#pipeline-security-sink) to use in your pipeline configuration. Also add the following permissions for Amazon RDS source to the role:

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
    {
    "Sid": "allowReadingFromS3Buckets",
    "Effect": "Allow",
    "Action": [
    "s3:GetObject",
    "s3:DeleteObject",
    "s3:GetBucketLocation",
    "s3:ListBucket",
    "s3:PutObject"
    ],
    "Resource": [
    "arn:aws:s3:::{{s3_bucket}}",
    "arn:aws:s3:::{{s3_bucket}}/*"
    ]
    },
    {
    "Sid": "allowNetworkInterfacesActions",
    "Effect": "Allow",
    "Action": [
    "ec2:AttachNetworkInterface",
    "ec2:CreateNetworkInterface",
    "ec2:CreateNetworkInterfacePermission",
    "ec2:DeleteNetworkInterface",
    "ec2:DeleteNetworkInterfacePermission",
    "ec2:DetachNetworkInterface",
    "ec2:DescribeNetworkInterfaces"
    ],
    "Resource": [
    "arn:aws:ec2:*:{{111122223333}}:network-interface/*",
    "arn:aws:ec2:*:{{111122223333}}:subnet/*",
    "arn:aws:ec2:*:{{111122223333}}:security-group/*"
    ]
    },
    {
    "Sid": "allowDescribeEC2",
    "Effect": "Allow",
    "Action": [
    "ec2:Describe*"
    ],
    "Resource": "*"
    },
    {
    "Sid": "allowTagCreation",
    "Effect": "Allow",
    "Action": [
    "ec2:CreateTags"
    ],
    "Resource": "arn:aws:ec2:*:{{111122223333}}:network-interface/*",
    "Condition": {
    "StringEquals": {
    "aws:RequestTag/OSISManaged": "true"
    }
    }
    },
    {
    "Sid": "AllowDescribeInstances",
    "Effect": "Allow",
    "Action": [
    "rds:DescribeDBInstances"
    ],
    "Resource": [
    "arn:aws:rds:{{us-east-2}}:{{111122223333}}:db:*"
    ]
    },
    {
    "Sid": "AllowSnapshots",
    "Effect": "Allow",
    "Action": [
    "rds:DescribeDBSnapshots",
    "rds:CreateDBSnapshot",
    "rds:AddTagsToResource"
    ],
    "Resource": [
    "arn:aws:rds:{{us-east-2}}:{{111122223333}}:db:{{DB-id}}",
    "arn:aws:rds:{{us-east-2}}:{{111122223333}}:snapshot:{{DB-id}}*"
    ]
    },
    {
    "Sid": "AllowExport",
    "Effect": "Allow",
    "Action": [
    "rds:StartExportTask"
    ],
    "Resource": [
    "arn:aws:rds:{{us-east-2}}:{{111122223333}}:snapshot:{{DB-id}}*"
    ]
    },
    {
    "Sid": "AllowDescribeExports",
    "Effect": "Allow",
    "Action": [
    "rds:DescribeExportTasks"
    ],
    "Resource": "*",
    "Condition": {
    "StringEquals": {
    "aws:RequestedRegion": "{{us-east-2}}",
    "aws:ResourceAccount": "{{111122223333}}"
    }
    }
    },
    {
    "Sid": "AllowAccessToKmsForExport",
    "Effect": "Allow",
    "Action": [
    "kms:Decrypt",
    "kms:Encrypt",
    "kms:DescribeKey",
    "kms:RetireGrant",
    "kms:CreateGrant",
    "kms:ReEncrypt*",
    "kms:GenerateDataKey*"
    ],
    "Resource": [
    "arn:aws:kms:{{us-east-2}}:{{111122223333}}:key/{{export-key-id}}"
    ]
    },
    {
    "Sid": "AllowPassingExportRole",
    "Effect": "Allow",
    "Action": "iam:PassRole",
    "Resource": [
    "arn:aws:iam::{{111122223333}}:role/{{export-role}}"
    ]
    },
    {
    "Sid": "SecretsManagerReadAccess",
    "Effect": "Allow",
    "Action": [
    "secretsmanager:GetSecretValue"
    ],
    "Resource": [
    "arn:aws:secretsmanager:*:{{111122223333}}:secret:*"
    ]
    }
    ]
    }
```

------

## Step 2: Create the pipeline
<a name="rds-mysql-pipeline"></a>

Configure an OpenSearch Ingestion pipeline similar to the following. The example pipeline specifies an Amazon RDS instance as the source. 

```
version: "2"
rds-mysql-pipeline:
  source:
    rds:
      db_identifier: "{{instance-id}}"
      engine: mysql
      database: "{{database-name}}"
      tables:
        include:
          - "{{table1}}"
          - "{{table2}}"
      s3_bucket: "{{bucket-name}}"
      s3_region: "{{bucket-region}}"
      s3_prefix: "{{prefix-name}}"
      export:
        kms_key_id: "{{kms-key-id}}"
        iam_role_arn: "{{export-role-arn}}"
      stream: true
      aws:
        sts_role_arn: "arn:aws:iam::{{account-id}}:role/{{pipeline-role}}"
        region: "us-east-1"
      authentication:
        username: ${{aws_secrets:secret:username}}
        password: ${{aws_secrets:secret:password}}
  sink:
    - opensearch:
        hosts: ["https://search-mydomain.us-east-1.es.amazonaws.com"]
        index: "${getMetadata(\"table_name\")}"
        index_type: custom
        document_id: "${getMetadata(\"primary_key\")}"
        action: "${getMetadata(\"opensearch_action\")}"
        document_version: "${getMetadata(\"document_version\")}"
        document_version_type: "external"
        aws:
          sts_role_arn: "arn:aws:iam::{{account-id}}:role/{{pipeline-role}}"
          region: "us-east-1"
extension:
  aws:
    secrets:
      secret:
        secret_id: "{{rds-secret-id}}"
        region: "us-east-1"
        sts_role_arn: "arn:aws:iam::{{account-id}}:role/{{pipeline-role}}"
        refresh_interval: PT1H
```

You can use a preconfigured Amazon RDS blueprint to create this pipeline. For more information, see [Working with blueprints](pipeline-blueprint.md).

To use Amazon Aurora as a source, you need to configure VPC access for the pipeline. The VPC you choose should be the same VPC your Amazon Aurora source uses. Then choose one or more subnets and one or more VPC security groups. Note that the pipeline needs network access to a Aurora MySQL database, so you should also verify that your Aurora cluster is configured with a VPC security group that allows inbound traffic from the pipeline's VPC security group to the database port. For more information, see [Controlling access with security groups](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Overview.RDSSecurityGroups.html).

If you're using the AWS Management Console to create your pipeline, you must also attach your pipeline to your VPC in order to use Amazon Aurora as a source. To do this, find the **Network configuration** section, choose **Attach to VPC**, and choose your CIDR from one of the provided default options, or select your own. The CIDR block must use a /24 prefix length. You can use any /24 CIDR from a private address space as defined in the [RFC 1918 Best Current Practice](https://datatracker.ietf.org/doc/html/rfc1918).

To provide a custom CIDR, select **Other** from the dropdown menu. To avoid a collision in IP addresses between OpenSearch Ingestion and Amazon RDS, ensure that the Amazon RDS VPC CIDR is different from the CIDR for OpenSearch Ingestion.

For more information, see [Configuring VPC access for a pipeline](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/pipeline-security.html#pipeline-vpc-configure).

## Data consistency
<a name="rds-mysql-pipeline-consistency"></a>

The pipeline ensures data consistency by continuously polling or receiving changes from the Amazon RDS instance and updating the corresponding documents in the OpenSearch index.

OpenSearch Ingestion supports end-to-end acknowledgement to ensure data durability. When a pipeline reads snapshots or streams, it dynamically creates partitions for parallel processing. The pipeline marks a partition as complete when it receives an acknowledgement after ingesting all records in the OpenSearch domain or collection. If you want to ingest into an OpenSearch Serverless search collection, you can generate a document ID in the pipeline. If you want to ingest into an OpenSearch Serverless time series collection, note that the pipeline doesn't generate a document ID, so you must omit `document_id: "${getMetadata(\"primary_key\")}"` in your pipeline sink configuration. 

An OpenSearch Ingestion pipeline also maps incoming event actions into corresponding bulk indexing actions to help ingest documents. This keeps data consistent, so that every data change in Amazon RDS is reconciled with the corresponding document changes in OpenSearch.

## Mapping data types
<a name="rds-mysql-pipeline-mapping"></a>

OpenSearch Ingestion pipeline maps MySQL data types to representations that are suitable for OpenSearch Service domains or collections to consume. If no mapping template is defined in OpenSearch, OpenSearch automatically determines field types with [dynamic mapping](https://docs.opensearch.org/latest/field-types/#dynamic-mapping) based on the first sent document. You can also explicitly define the field types that work best for you in OpenSearch through a mapping template. 

The table below lists MySQL data types and corresponding OpenSearch field types. The *Default OpenSearch Field Type* column shows the corresponding field type in OpenSearch if no explicit mapping is defined. In this case, OpenSearch automatically determines field types with dynamic mapping. The *Recommended OpenSearch Field Type* column is the corresponding field type that is recommended to explicitly specify in a mapping template. These field types are more closely aligned with the data types in MySQL and can usually enable better search features available in OpenSearch.


| MySQL Data Type | Default OpenSearch Field Type | Recommended OpenSearch Field Type | 
| --- | --- | --- | 
| BIGINT | long | long | 
| BIGINT UNSIGNED | long | unsigned long | 
| BIT | long | byte, short, integer, or long depending on number of bits | 
| DECIMAL | text | double or keyword | 
| DOUBLE | float | double | 
| FLOAT | float | float | 
| INT | long | integer | 
| INT UNSIGNED | long | long | 
| MEDIUMINT | long | integer | 
| MEDIUMINT UNSIGNED | long | integer | 
| NUMERIC | text | double or keyword | 
| SMALLINT | long | short | 
| SMALLINT UNSIGNED | long | integer | 
| TINYINT | long | byte | 
| TINYINT UNSIGNED | long | short | 
| BINARY | text | binary | 
| BLOB | text | binary | 
| CHAR | text | text | 
| ENUM | text | keyword | 
| LONGBLOB | text | binary | 
| LONGTEXT | text | text | 
| MEDIUMBLOB | text | binary | 
| MEDIUMTEXT | text | text | 
| SET | text | keyword | 
| TEXT | text | text | 
| TINYBLOB | text | binary | 
| TINYTEXT | text | text | 
| VARBINARY | text | binary | 
| VARCHAR | text | text | 
| DATE | long (in epoch milliseconds) | date | 
| DATETIME | long (in epoch milliseconds) | date | 
| TIME | long (in epoch milliseconds) | date | 
| TIMESTAMP | long (in epoch milliseconds) | date | 
| YEAR | long (in epoch milliseconds) | date | 
| GEOMETRY | text (in WKT format) | geo\_shape | 
| GEOMETRYCOLLECTION | text (in WKT format) | geo\_shape | 
| LINESTRING | text (in WKT format) | geo\_shape | 
| MULTILINESTRING | text (in WKT format) | geo\_shape | 
| MULTIPOINT | text (in WKT format) | geo\_shape | 
| MULTIPOLYGON | text (in WKT format) | geo\_shape | 
| POINT | text (in WKT format) | geo\_point or geo\_shape | 
| POLYGON | text (in WKT format) | geo\_shape | 
| JSON | text | object | 

We recommend that you configure the dead-letter queue (DLQ) in your OpenSearch Ingestion pipeline. If you've configured the queue, OpenSearch Service sends all failed documents that can't be ingested due to dynamic mapping failures to the queue.

If automatic mappings fail, you can use `template_type` and `template_content` in your pipeline configuration to define explicit mapping rules. Alternatively, you can create mapping templates directly in your search domain or collection before you start the pipeline.

## Limitations
<a name="rds-mysql-pipeline-limitations"></a>

Consider the following limitations when you set up an OpenSearch Ingestion pipeline for RDS for MySQL:
+ The integration only supports one MySQL database per pipeline.
+ The integration does not currently support cross-region data ingestion; your Amazon RDS instance and OpenSearch domain must be in the same AWS Region.
+ The integration does not currently support cross-account data ingestion; your Amazon RDS instance and OpenSearch Ingestion pipeline must be in the same AWS account. 
+ Ensure that the Amazon RDS instance has authentication enabled using Secrets Manager, which is the only supported authentication mechanism.
+ The existing pipeline configuration can't be updated to ingest data from a different database and/or a different table. To update the database and/or table name of a pipeline, you have to create a new pipeline.
+ Data Definition Language (DDL) statements are generally not supported. Data consistency will not be maintained if:
  + Primary keys are changed (add/delete/rename).
  + Tables are dropped/truncated.
  + Column names or data types are changed.
+ If the MySQL tables to sync don't have primary keys defined, data consistency are not guaranteed. You will need to define custom `document_id` option in OpenSearch sink configuration properly to be able to sync updates/deletes to OpenSearch.
+ Foreign key references with cascading delete actions are not supported and can result in data inconsistency between RDS for MySQL and OpenSearch.
+ Amazon RDS multi-availability zone DB clusters are not supported.
+ Supported versions: MySQL version 8.0 and higher.

## Recommended CloudWatch Alarms
<a name="aurora-mysql-pipeline-metrics"></a>

The following CloudWatch metrics are recommended for monitoring the performance of your ingestion pipeline. These metrics can help you identify the amount of data processed from exports, the number of events processed from streams, the errors in processing exports and stream events, and the number of documents written to the destination. You can setup CloudWatch alarms to perform an action when one of these metrics exceed a specified value for a specified amount of time.


| Metric | Description | 
| --- | --- | 
| {{pipeline-name}}.rds.credentialsChanged | This metric indicates how often AWS secrets are rotated. | 
| {{pipeline-name}}.rds.executorRefreshErrors | This metric indicates failures to refresh AWS secrets. | 
| {{pipeline-name}}.rds.exportRecordsTotal | This metric indicates the number of records exported from Amazon Aurora. | 
| {{pipeline-name}}.rds.exportRecordsProcessed | This metric indicates the number of records processed by OpenSearch Ingestion pipeline. | 
| {{pipeline-name}}.rds.exportRecordProcessingErrors | This metric indicates number of processing errors in an OpenSearch Ingestion pipeline while reading the data from an Amazon Aurora cluster. | 
| {{pipeline-name}}.rds.exportRecordsSuccessTotal | This metric indicates the total number of export records processed successfully. | 
| {{pipeline-name}}.rds.exportRecordsFailedTotal | This metric indicates the total number of export records that failed to process. | 
| {{pipeline-name}}.rds.bytesReceived | This metrics indicates the total number of bytes received by an OpenSearch Ingestion pipeline. | 
| {{pipeline-name}}.rds.bytesProcessed | This metrics indicates the total number of bytes processed by an OpenSearch Ingestion pipeline. | 
| {{pipeline-name}}.rds.streamRecordsSuccessTotal | This metric indicates the number of records successfully processed from the stream. | 
| {{pipeline-name}}.rds.streamRecordsFailedTotal | This metrics indicates the total number of records failed to process from the stream. | 