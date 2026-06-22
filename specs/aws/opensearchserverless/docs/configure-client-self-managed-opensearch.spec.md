---
id: "@specs/aws/opensearchserverless/docs/configure-client-self-managed-opensearch"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Self-managed OpenSearch clusters"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Self-managed OpenSearch clusters

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/configure-client-self-managed-opensearch
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Migrating data from self-managed OpenSearch clusters using Amazon OpenSearch Ingestion
<a name="configure-client-self-managed-opensearch"></a>

You can use an Amazon OpenSearch Ingestion pipeline with self-managed OpenSearch or Elasticsearch to migrate data to Amazon OpenSearch Service domains and OpenSearch Serverless collections. OpenSearch Ingestion supports both public and private network configurations for the migration of data from self-managed OpenSearch and Elasticsearch. 

## Migrating from public OpenSearch clusters
<a name="self-managaged-opensearch-public"></a>

You can use OpenSearch Ingestion pipelines to migrate data from a self-managed OpenSearch or Elasticsearch cluster with a public configuration, which means that the domain DNS name can be publicly resolved. To do so, set up an OpenSearch Ingestion pipeline with self-managed OpenSearch or Elasticsearch as the source and OpenSearch Service or OpenSearch Serverless as the destination. This effectively migrates your data from a self-managed source cluster to an AWS-managed destination domain or collection.

### Prerequisites
<a name="self-managaged-opensearch-public-prereqs"></a>

Before you create your OpenSearch Ingestion pipeline, perform the following steps:

1. Create a self-managed OpenSearch or Elastisearch cluster that contains the data you want to migrate and configure a public DNS name. For instructions, see [Create a cluster](https://opensearch.org/docs/latest/tuning-your-cluster/) in the OpenSearch documentation.

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
<a name="self-managed-opensearch-public-pipeline-role"></a>

After you have your OpenSearch pipeline prerequisites set up, [configure the pipeline role](pipeline-security-overview.md#pipeline-security-sink) that you want to use in your pipeline configuration, and add permission to write to an OpenSearch Service domain or OpenSearch Serverless collection, as well as permission to read secrets from Secrets Manager.

### Step 2: Create the pipeline
<a name="self-managed-opensearch-public-pipeline"></a>

You can then configure an OpenSearch Ingestion pipeline like the following, which specifies OpenSearch as the source. 

You can specify multiple OpenSearch Service domains as destinations for your data. This capability enables conditional routing or replication of incoming data into multiple OpenSearch Service domains.

You can also migrate data from a source OpenSearch or Elasticsearch cluster to an OpenSearch Serverless VPC collection. Ensure you provide a network access policy within the pipeline configuration.

```
version: "2"
opensearch-migration-pipeline:
  source:
    opensearch:
      acknowledgments: true
      host: [ "https://{{my-self-managed-cluster-name}}:{{9200}}" ]
      indices:
        include:
          - index_name_regex: "include-.*"
        exclude:
          - index_name_regex: '\..*'
      authentication:
        username: ${aws_secrets:secret:{{username}}}
        password: ${aws_secrets:secret:{{password}}}
        scheduling:
           interval: "PT2H"
           index_read_count: 3
           start_time: "2023-06-02T22:01:30.00Z"
  sink:
  - opensearch:
      hosts: ["{{https://search-mydomain.us-east-1.es.amazonaws.com}}"]
      aws:
          region: "{{us-east-1}}"
          #Uncomment the following lines if your destination is an OpenSearch Serverless collection
          #serverless: true
          # serverless_options:
          #     network_policy_name: "{{network-policy-name}}"
      index: "${getMetadata(\"{{opensearch-index}}\")}"
      document_id: "${getMetadata(\"{{opensearch-document_id}}\")}"
      enable_request_compression: true
      dlq:
        s3:
          bucket: "{{bucket-name}}"
          key_path_prefix: "apache-log-pipeline/logs/dlq"
          region: "{{us-east-1}}"
extension:
  aws:
    secrets:
      secret:
        secret_id: "{{my-opensearch-secret}}"
        region: "{{us-east-1}}"
        refresh_interval: PT1H
```

You can use a preconfigured blueprint to create this pipeline. For more information, see [Working with blueprints](pipeline-blueprint.md).

## Migrating data from OpenSearch clusters in a VPC
<a name="self-managaged-opensearch-private"></a>

You can also use OpenSearch Ingestion pipelines to migrate data from a self-managed OpenSearch or Elasticsearch cluster running in a VPC. To do so, set up an OpenSearch Ingestion pipeline with self-managed OpenSearch or Elasticsearch as the source and OpenSearch Service or OpenSearch Serverless as the destination. This effectively migrates your data from a self-managed source cluster to an AWS-managed destination domain or collection.

### Prerequisites
<a name="self-managaged-opensearch-private-prereqs"></a>

Before you create your OpenSearch Ingestion pipeline, perform the following steps:

1. Create a self-managed OpenSearch or Elastisearch cluster with a VPC network configuration that contains the data you want to migrate. 

1. Create an OpenSearch Service domain or OpenSearch Serverless collection where you want to migrate data to. For more information, see [Creating OpenSearch Service domains](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html#createdomains) and [Creating collections](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html#serverless-create).

1. Set up authentication on your self-managed cluster with AWS Secrets Manager. Enable secrets rotation by following the steps in [Rotate AWS Secrets Manager secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html).

1. Obtain the ID of the VPC that that has access to self-managed OpenSearch or Elasticsearch. Choose the /24 VPC CIDR block to be used by OpenSearch Ingestion.
**Note**  
If you're using the AWS Management Console to create your pipeline, you must also attach your OpenSearch Ingestion pipeline to your VPC in order to use self-managed OpenSearch or Elasticsearch. To do so, find the **Source network options** section, select the **Attach to VPC** checkbox, and choose your CIDR from one of the provided default options. The CIDR block must use a /24 prefix length. You can use any /24 CIDR from a private address space as defined in the [RFC 1918 Best Current Practice](https://datatracker.ietf.org/doc/html/rfc1918).  
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
           "arn:aws:es:{{us-east-1}}:{{111122223333}}:domain/{{example.com}}"
         ]
       }
     ]
   }
   ```

------

   To create an IAM role with the correct permissions to access write data to the collection or domain, see [Setting up roles and users in Amazon OpenSearch Ingestion](pipeline-security-overview.md).

### Step 1: Configure the pipeline role
<a name="self-managed-opensearch-private-pipeline-role"></a>

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

You must provide the above Amazon EC2 permissions on the IAM role that you use to create the OpenSearch Ingestion pipeline because the pipeline uses these permissions to create and delete a network interface in your VPC. The pipeline can only access the OpenSearch cluster through this network interface.

### Step 2: Create the pipeline
<a name="self-managed-opensearch-private-pipeline"></a>

You can then configure an OpenSearch Ingestion pipeline like the following, which specifies OpenSearch as the source. 

You can specify multiple OpenSearch Service domains as destinations for your data. This capability enables conditional routing or replication of incoming data into multiple OpenSearch Service domains.

You can also migrate data from a source OpenSearch or Elasticsearch cluster to an OpenSearch Serverless VPC collection. Ensure you provide a network access policy within the pipeline configuration.

```
version: "2"
opensearch-migration-pipeline:
  source:
    opensearch:
      acknowledgments: true
      host: [ "https://{{my-self-managed-cluster-name}}:{{9200}}" ]
      indices:
        include:
          - index_name_regex: "include-.*"
        exclude:
          - index_name_regex: '\..*'
      authentication:
        username: ${aws_secrets:secret:{{username}}}
        password: ${aws_secrets:secret:{{password}}}
        scheduling:
           interval: "PT2H"
           index_read_count: 3
           start_time: "2023-06-02T22:01:30.00Z"
  sink:
  - opensearch:
      hosts: ["{{https://search-mydomain.us-east-1.es.amazonaws.com}}"]
      aws:
          region: "{{us-east-1}}"
          #Uncomment the following lines if your destination is an OpenSearch Serverless collection
          #serverless: true
          # serverless_options:
          #     network_policy_name: "{{network-policy-name}}"
      index: "${getMetadata(\"{{opensearch-index}}\")}"
      document_id: "${getMetadata(\"{{opensearch-document_id}}\")}"
      enable_request_compression: true
      dlq:
        s3:
          bucket: "{{bucket-name}}"
          key_path_prefix: "apache-log-pipeline/logs/dlq"
          region: "{{us-east-1}}"
extension:
  aws:
    secrets:
      secret:
        secret_id: "{{my-opensearch-secret}}"
        region: "{{us-east-1}}"
        refresh_interval: PT1H
```

You can use a preconfigured blueprint to create this pipeline. For more information, see [Working with blueprints](pipeline-blueprint.md).