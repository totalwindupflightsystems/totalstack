---
id: "@specs/aws/opensearchserverless/docs/configure-client-self-managed-kafka"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Self-managed Kafka"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Self-managed Kafka

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/configure-client-self-managed-kafka
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Using an OpenSearch Ingestion pipeline with Kafka
<a name="configure-client-self-managed-kafka"></a>

You can use the [Kafka](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/kafka/) plugin to stream data from self-managed Kafka clusters to Amazon OpenSearch Service domains and OpenSearch Serverless collections. OpenSearch Ingestion supports connections from Kafka clusters configured with either public or private (VPC) networking. This topic outlines the prerequisites and steps to set up an ingestion pipeline, including configuring network settings and authentication methods such as mutual TLS (mTLS), SASL/SCRAM, or IAM.

## Migrating data from public Kafka clusters
<a name="self-managaged-kafka-public"></a>

You can use OpenSearch Ingestion pipelines to migrate data from a public self-managed Kafka cluster, which means that the domain DNS name can be publicly resolved. To do so, set up an OpenSearch Ingestion pipeline with self-managed Kafka as the source and OpenSearch Service or OpenSearch Serverless as the destination. This processes your streaming data from a self-managed source cluster to an AWS-managed destination domain or collection. 

### Prerequisites
<a name="self-managaged-kafka-public-prereqs"></a>

Before you create your OpenSearch Ingestion pipeline, perform the following steps:

1. Create a self-managed Kafka cluster with a public network configuration. The cluster should contain the data you want to ingest into OpenSearch Service.

1. Create an OpenSearch Service domain or OpenSearch Serverless collection where you want to migrate data to. For more information, see [Creating OpenSearch Service domains](createupdatedomains.md#createdomains) and [Creating collections](serverless-create.md).

1. Set up authentication on your self-managed cluster with AWS Secrets Manager. Enable secrets rotation by following the steps in [Rotate AWS Secrets Manager secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html).

1. Attach a [resource-based policy](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ac.html#ac-types-resource) to your domain or a [data access policy](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-data-access.html) to your collection. These access policies allow OpenSearch Ingestion to write data from your self-managed cluster to your domain or collection. 

   The following sample domain access policy allows the pipeline role, which you create in the next step, to write data to a domain. Make sure that you update the `resource` with your own ARN. 

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
           "AWS": "arn:aws:iam::{{444455556666}}:role/{{pipeline-role}}"
         },
         "Action": [
           "es:DescribeDomain",
           "es:ESHttp*"
         ],
         "Resource": [
           "arn:aws:es:{{us-east-1}}:{{111122223333}}:domain/{{domain-name}}"
         ]
       }
     ]
   }
   ```

------

   To create an IAM role with the correct permissions to access write data to the collection or domain, see [Setting up roles and users in Amazon OpenSearch Ingestion](pipeline-security-overview.md).

### Step 1: Configure the pipeline role
<a name="self-managed-kafka-public-pipeline-role"></a>

After you have your Kafka pipeline prerequisites set up, [configure the pipeline role](pipeline-security-overview.md#pipeline-security-sink) that you want to use in your pipeline configuration, and add permission to write to an OpenSearch Service domain or OpenSearch Serverless collection, as well as permission to read secrets from Secrets Manager.

### Step 2: Create the pipeline
<a name="self-managed-kafka-public-pipeline"></a>

You can then configure an OpenSearch Ingestion pipeline like the following, which specifies Kafka as the source. 

You can specify multiple OpenSearch Service domains as destinations for your data. This capability enables conditional routing or replication of incoming data into multiple OpenSearch Service domains.

You can also migrate data from a source Confluent Kafka cluster to an OpenSearch Serverless VPC collection. Ensure you provide a network access policy within the pipeline configuration. You can use a Confluent schema registry to define a Confluent schema.

```
version: "2"
kafka-pipeline:
  source:
    kafka:
      encryption:
        type: "ssl"
      topics:
        - name: "{{topic-name}}"
          group_id: "{{group-id}}"
      bootstrap_servers:
        - "{{bootstrap-server}}.{{us-east-1}}.aws.private.confluent.cloud:9092"
      authentication:
        sasl:
          plain:
            username: ${aws_secrets:confluent-kafka-secret:{{username}}}
            password: ${aws_secrets:confluent-kafka-secret:{{password}}}
      schema:
        type: confluent
        registry_url: https://{{my-registry}}.{{us-east-1}}.aws.confluent.cloud
        api_key: "${{aws_secrets:schema-secret:{{schema_registry_api_key}}}}"
        api_secret: "${{aws_secrets:schema-secret:{{schema_registry_api_secret}}}}"
        basic_auth_credentials_source: "USER_INFO"
  sink:
  - opensearch:
      hosts: ["{{https://search-mydomain.us-east-1.es.amazonaws.com}}"]
      aws:
          region: "{{us-east-1}}"
      index: "{{confluent-index}}"
extension:
  aws:
    secrets:
      confluent-kafka-secret:
        secret_id: "{{my-kafka-secret}}"
        region: "{{us-east-1}}"
      schema-secret:
        secret_id: "{{my-self-managed-kafka-schema}}"
        region: "{{us-east-1}}"
```

You can use a preconfigured blueprint to create this pipeline. For more information, see [Working with blueprints](pipeline-blueprint.md).

### Migrating data from Kafka clusters in a VPC
<a name="self-managaged-kafka-private"></a>

You can also use OpenSearch Ingestion pipelines to migrate data from a self-managed Kafka cluster running in a VPC. To do so, set up an OpenSearch Ingestion pipeline with self-managed Kafka as the source and OpenSearch Service or OpenSearch Serverless as the destination. This processes your streaming data from a self-managed source cluster to an AWS-managed destination domain or collection.

#### Prerequisites
<a name="self-managaged-kafka-private-prereqs"></a>

Before you create your OpenSearch Ingestion pipeline, perform the following steps:

1. Create a self-managed Kafka cluster with a VPC network configuration that contains the data you want to ingest into OpenSearch Service. 

1. Create an OpenSearch Service domain or OpenSearch Serverless collection where you want to migrate data to. For more information, see [Creating OpenSearch Service domains](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html#createdomains) and [Creating collections](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html#serverless-create).

1. Set up authentication on your self-managed cluster with AWS Secrets Manager. Enable secrets rotation by following the steps in [Rotate AWS Secrets Manager secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html).

1. Obtain the ID of the VPC that that has access to self-managed Kafka. Choose the VPC CIDR to be used by OpenSearch Ingestion.
**Note**  
If you're using the AWS Management Console to create your pipeline, you must also attach your OpenSearch Ingestion pipeline to your VPC in order to use self-managed Kafka. To do so, find the **Network configuration** section, select the **Attach to VPC** checkbox, and choose your CIDR from one of the provided default options, or select your own. You can use any CIDR from a private address space as defined in the [RFC 1918 Best Current Practice](https://datatracker.ietf.org/doc/html/rfc1918).  
To provide a custom CIDR, select **Other** from the dropdown menu. To avoid a collision in IP addresses between OpenSearch Ingestion and self-managed OpenSearch, ensure that the self-managed OpenSearch VPC CIDR is different from the CIDR for OpenSearch Ingestion.

1. Attach a [resource-based policy](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ac.html#ac-types-resource) to your domain or a [data access policy](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-data-access.html) to your collection. These access policies allow OpenSearch Ingestion to write data from your self-managed cluster to your domain or collection. 

   The following sample domain access policy allows the pipeline role, which you create in the next step, to write data to a domain. Make sure that you update the `resource` with your own ARN. 

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
           "AWS": "arn:aws:iam::{{444455556666}}:role/{{pipeline-role}}"
         },
         "Action": [
           "es:DescribeDomain",
           "es:ESHttp*"
         ],
         "Resource": [
           "arn:aws:es:{{us-east-1}}:{{111122223333}}:domain/{{domain-name}}"
         ]
       }
     ]
   }
   ```

------

   To create an IAM role with the correct permissions to access write data to the collection or domain, see [Setting up roles and users in Amazon OpenSearch Ingestion](pipeline-security-overview.md).

#### Step 1: Configure the pipeline role
<a name="self-managed-kafka-private-pipeline-role"></a>

After you have your pipeline prerequisites set up, [configure the pipeline role](pipeline-security-overview.md#pipeline-security-sink) that you want to use in your pipeline configuration, and add the following permissions in the role:

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "SecretsManagerReadAccess",
            "Effect": "Allow",
            "Action": [
                "secretsmanager:GetSecretValue"
            ],
            "Resource": ["arn:aws:secretsmanager:{{us-east-1}}:{{111122223333}}:secret:{{secret-name}}"]
        },
        {
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
                "arn:aws:ec2:*:*:network-interface/*",
                "arn:aws:ec2:*:*:subnet/*",
                "arn:aws:ec2:*:*:security-group/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeDhcpOptions",
                "ec2:DescribeRouteTables",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeSubnets",
                "ec2:DescribeVpcs",
                "ec2:Describe*"
            ],
            "Resource": "*"
        },
        { 
            "Effect": "Allow",
            "Action": [ 
                "ec2:CreateTags"
            ],
            "Resource": "arn:aws:ec2:*:*:network-interface/*",
            "Condition": { 
               "StringEquals": 
                    {
                        "aws:RequestTag/OSISManaged": "true"
                    } 
            } 
        }
    ]
}
```

------

You must provide the above Amazon EC2 permissions on the IAM role that you use to create the OpenSearch Ingestion pipeline because the pipeline uses these permissions to create and delete a network interface in your VPC. The pipeline can only access the Kafka cluster through this network interface.

#### Step 2: Create the pipeline
<a name="self-managed-kafka-private-pipeline"></a>

You can then configure an OpenSearch Ingestion pipeline like the following, which specifies Kafka as the source.

You can specify multiple OpenSearch Service domains as destinations for your data. This capability enables conditional routing or replication of incoming data into multiple OpenSearch Service domains.

You can also migrate data from a source Confluent Kafka cluster to an OpenSearch Serverless VPC collection. Ensure you provide a network access policy within the pipeline configuration. You can use a Confluent schema registry to define a Confluent schema.

```
 version: "2"
kafka-pipeline:
  source:
    kafka:
      encryption:
        type: "ssl"
      topics:
        - name: "{{topic-name}}"
          group_id: "{{group-id}}"
      bootstrap_servers:
        - "{{bootstrap-server}}.{{us-east-1}}.aws.private.confluent.cloud:9092"
      authentication:
        sasl:
          plain:
            username: ${aws_secrets:confluent-kafka-secret:{{username}}}
            password: ${aws_secrets:confluent-kafka-secret:{{password}}}
      schema:
        type: confluent
        registry_url: https://{{my-registry}}.{{us-east-1}}.aws.confluent.cloud
        api_key: "${{aws_secrets:schema-secret:{{schema_registry_api_key}}}}"
        api_secret: "${{aws_secrets:schema-secret:{{schema_registry_api_secret}}}}"
        basic_auth_credentials_source: "USER_INFO"
  sink:
  - opensearch:
      hosts: ["{{https://search-mydomain.us-east-1.es.amazonaws.com}}"]
      aws:
          region: "{{us-east-1}}"
      index: "{{confluent-index}}"
extension:
  aws:
    secrets:
      confluent-kafka-secret:
        secret_id: "{{my-kafka-secret}}"
        region: "{{us-east-1}}"
      schema-secret:
        secret_id: "{{my-self-managed-kafka-schema}}"
        region: "{{us-east-1}}"
```

You can use a preconfigured blueprint to create this pipeline. For more information, see [Working with blueprints](pipeline-blueprint.md).