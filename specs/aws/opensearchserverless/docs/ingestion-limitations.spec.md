---
id: "@specs/aws/opensearchserverless/docs/ingestion-limitations"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Limitations"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Limitations

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/ingestion-limitations
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Limitations of Amazon OpenSearch Ingestion
<a name="ingestion-limitations"></a>

OpenSearch Ingestion has the following limitations:
+ You can only ingest data into domains running OpenSearch 1.0 or later, or Elasticsearch 6.8 or later. If you're using the [OTel trace](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/otel-trace/) source, we recommend using Elasticsearch 7.9 or later so that you can use the [OpenSearch Dashboards plugin](https://opensearch.org/docs/latest/observability-plugin/trace/ta-dashboards/).
+ If a pipeline is writing to an OpenSearch Service domain that's within a VPC, the pipeline must be created in the same AWS Region as the domain.
+ You can only configure a single data source within a pipeline definition.
+ You can't specify [self-managed OpenSearch clusters](https://opensearch.org/docs/latest/about/#clusters-and-nodes) as sinks.
+ You can't specify a [custom endpoint](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/customendpoint.html) as a sink. You can still write to a domain that has custom endpoints enabled, but you must specify its standard endpoint.
+ You can't specify resources within [opt-in Regions](https://docs.aws.amazon.com//controltower/latest/userguide/opt-in-region-considerations.html) as sources or sinks.
+ There are some constraints on the parameters that you can include in a pipeline configuration. For more information, see [Configuration requirements and constraints](pipeline-config-reference.md#ingestion-parameters).