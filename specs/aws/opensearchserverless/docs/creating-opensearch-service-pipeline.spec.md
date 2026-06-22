---
id: "@specs/aws/opensearchserverless/docs/creating-opensearch-service-pipeline"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Migrating data between domains and collections"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Migrating data between domains and collections

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/creating-opensearch-service-pipeline
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Migrating data between domains and collections using Amazon OpenSearch Ingestion
<a name="creating-opensearch-service-pipeline"></a>

You can use OpenSearch Ingestion pipelines to migrate data between Amazon OpenSearch Service domains or OpenSearch Serverless VPC collections. To do so, you set up a pipeline in which you configure one domain or collection as the source, and another domain or collection as the sink. This effectively migrates your data from one domain or collection to the other.

To migrate data, you must have the following resources:
+ A source OpenSearch Service domain or OpenSearch Serverless VPC collection. This domain or collection contains the data that you want to migrate. If you're using a domain, it must be running OpenSearch version 1.0 or later, or Elasticsearch version 7.4 or later. The domain must also have an access policy that grants the appropriate permissions to your pipeline role.
+ A separate domain or VPC collection that you want to migrate your data to. This domain or collection will act as the pipeline *sink*.
+ An pipeline role that OpenSearch Ingestion will use to read and write to your collection or domain. You include the Amazon Resource Name (ARN) of this role in your pipeline configuration. For more information, see the following resources:
  + [Granting Amazon OpenSearch Ingestion pipelines access to domains](pipeline-domain-access.md)
  + [Granting Amazon OpenSearch Ingestion pipelines access to collections](pipeline-collection-access.md)

**Topics**
+ [Limitations](#Limitations-domain-collection)
+ [OpenSearch Service as a source](#opensearch-source)
+ [Specifying multiple OpenSearch Service domain sinks](#multiple-domains)
+ [Migrating data to an OpenSearch Serverless VPC collection](#pipeline-collection)

## Limitations
<a name="Limitations-domain-collection"></a>

The following limitations apply when you designate OpenSearch Service domains or OpenSearch Serverless collections as sinks:
+ A pipeline can't write to more than one VPC domain.
+ Migrating data to or from OpenSearch Serverless collections that use VPC access is supported. Public collections may also work in some configurations; however, VPC-based collections are recommended for production use.
+ You can't specify a combination of VPC and public domains in a single pipeline configuration.
+ You can have a maximum of 20 non-pipeline sinks within a single pipeline configuration.
+ You can specify sinks from a maximum of three different AWS Regions in a single pipeline configuration.
+ A pipeline with multiple sinks might experience a reduction in processing speed over time if any of the sinks are down for too long, or are not provisioned with enough capacity to receive incoming data.

## OpenSearch Service as a source
<a name="opensearch-source"></a>

The domain or collection that you specify as the source is where the data is migrated *from*. 

### Creating a pipeline role in IAM
<a name="source-IAM"></a>

To create your OpenSearch Ingestion pipeline, you must first create a pipeline role to grant read and write access between domains or collections. To do this, perform the following steps:

1. Create a new permissions policy in IAM to attach to the pipeline role. Make sure you allow permissions to read from the source and write to the sink. For more information on setting IAM pipeline permissions for OpenSearch Service domains, see [Granting Amazon OpenSearch Ingestion pipelines access to domains](pipeline-domain-access.md) and [Granting Amazon OpenSearch Ingestion pipelines access to collections](pipeline-collection-access.md).

1. Specify the following permissions within the pipeline role to read from the source:

------
#### [ JSON ]

****  

   ```
   {
      "Version":"2012-10-17",		 	 	 
      "Statement":[
         {
            "Effect":"Allow",
            "Action":"es:ESHttpGet",
            "Resource":[
               "arn:aws:es:{{us-east-1}}:{{111122223333}}:domain/{{domain-name}}/",
               "arn:aws:es:{{us-east-1}}:{{111122223333}}:domain/{{domain-name}}/_cat/indices",
               "arn:aws:es:{{us-east-1}}:{{111122223333}}:domain/{{domain-name}}/_search",
               "arn:aws:es:{{us-east-1}}:{{111122223333}}:domain/{{domain-name}}/_search/scroll",
               "arn:aws:es:{{us-east-1}}:{{111122223333}}:domain/{{domain-name}}/*/_search"
            ]
         },
         {
            "Effect":"Allow",
            "Action":"es:ESHttpPost",
            "Resource":[
               "arn:aws:es:{{us-east-1}}:{{111122223333}}:domain/{{domain-name}}/*/_search/point_in_time",
               "arn:aws:es:{{us-east-1}}:{{111122223333}}:domain/{{domain-name}}/*/_search/scroll"
            ]
         },
         {
            "Effect":"Allow",
            "Action":"es:ESHttpDelete",
            "Resource":[
               "arn:aws:es:{{us-east-1}}:{{111122223333}}:domain/{{domain-name}}/_search/point_in_time",
               "arn:aws:es:{{us-east-1}}:{{111122223333}}:domain/{{domain-name}}/_search/scroll"
            ]
         }
      ]
   }
   ```

------

### Creating a pipeline
<a name="create"></a>

After you attach the policy to the pipeline role, use the **AWSOpenSearchDataMigrationPipeline** migration blueprint to create the pipeline. This blueprint includes a default configuration for migrating data between OpenSearch Service domains or collections. For more information, see [Working with blueprints](pipeline-blueprint.md). 

**Note**  
OpenSearch Ingestion uses your source domain version and distribution to determine what mechanism to use for migration. Some versions support the `point_in_time` option. OpenSearch Serverless uses the `search_after` option because it doesn't support `scroll`. Note that OpenSearch Serverless does support `point_in_time` (PIT) operations; however, the pipeline uses `search_after` for compatibility across all source types.

New indexes might be in the process of being created during the migration process, or documents might be updating while migration is in progress. Because of this, you might need to perform either a single scan or multiple scans of your domain index data to pick up new or updated data. 

Specify the number of scans to run by configuring the `index_read_count` and `interval` in the pipeline configuration. The following example shows how to perform multiple scans:

```
scheduling:
    interval: "PT2H"
    index_read_count: 3
    start_time: "2023-06-02T22:01:30.00Z"
```

OpenSearch Ingestion uses the following configuration to ensure that your data is written to the same index and maintains the same document ID:

```
index: "${getMetadata(\"opensearch-index\")}"
document_id: "${getMetadata(\"opensearch-document_id\")}"
```

## Specifying multiple OpenSearch Service domain sinks
<a name="multiple-domains"></a>

You can specify multiple public OpenSearch Service domains as destinations for your data. You can use this capability to perform conditional routing or replicate incoming data into multiple OpenSearch Service domains. You can specify up to 10 different public OpenSearch Service domains as sinks.

In the following example, incoming data is conditionally routed to different OpenSearch Service domains:

```
...
  route:
    - 2xx_status: "/response >= 200 and /response < 300"
    - 5xx_status: "/response >= 500 and /response < 600"
  sink:
    - opensearch:
        hosts: [ "https://search-{{response-2xx}}.{{{{region}}}}.es.amazonaws.com" ]
        aws:
          region: "{{us-east-1}}"
        index: "response-2xx"
        routes:
          - 2xx_status
    - opensearch:
        hosts: [ "https://search-{{response-5xx}}.{{region}}.es.amazonaws.com" ]
        aws:
          region: "{{us-east-1}}"
        index: "response-5xx"
        routes:
          - 5xx_status
```

## Migrating data to an OpenSearch Serverless VPC collection
<a name="pipeline-collection"></a>

You can use OpenSearch Ingestion to migrate data from a source OpenSearch Service domain or OpenSearch Serverless collection to a VPC collection sink. You must provide a network access policy within the pipeline configuration. For more information about data ingestion into OpenSearch Serverless VPC collections, see [Tutorial: Ingesting data into a collection using Amazon OpenSearch Ingestion](osis-serverless-get-started.md).

**To migrate data to a VPC collection**

1. Create an OpenSearch Serverless collection. For instructions, see [Tutorial: Ingesting data into a collection using Amazon OpenSearch Ingestion](osis-serverless-get-started.md).

1. Create a network policy for the collection that specifies VPC access to both the collection endpoint and the Dashboards endpoint. For instructions, see [Network access for Amazon OpenSearch Serverless](serverless-network.md). 

1. Create the pipeline role if you don't already have one. For instructions, see [Pipeline role](pipeline-security-overview.md#pipeline-security-sink).

1. Create the pipeline. For instructions, see [Working with blueprints](pipeline-blueprint.md).