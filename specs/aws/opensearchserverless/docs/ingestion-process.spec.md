---
id: "@specs/aws/opensearchserverless/docs/ingestion-process"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Key concepts"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Key concepts

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/ingestion-process
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Key concepts in Amazon OpenSearch Ingestion
<a name="ingestion-process"></a>

Before you start using OpenSearch Ingestion, it's helpful to understand these key concepts.

**Pipeline**  
From an OpenSearch Ingestion perspective, a *pipeline* refers to a single provisioned data collector that you create within OpenSearch Service. You can think of it as the entire YAML configuration file, which includes one or more sub-pipelines. For steps to create an ingestion pipeline, see [Creating pipelines](creating-pipeline.md#create-pipeline).

**Sub-pipeline**  
You define sub-pipelines *within* a YAML configuration file. Each sub-pipeline is a combination of a source, a buffer, zero or more processors, and one or more sinks. You can define multiple sub-pipelines in a single YAML file, each with unique sources, processors, and sinks. To aid in monitoring with CloudWatch and other services, we recommend that you specify a pipeline name that's distinct from all of its sub-pipelines.  
You can string multiple sub-pipelines together within a single YAML file, so that the source for one sub-pipeline is another sub-pipeline, and its sink is a third sub-pipeline. For an example, see [Using an OpenSearch Ingestion pipeline with OpenTelemetry Collector](configure-client-otel.md).

**Source**  
The input component of a sub-pipeline. It defines the mechanism through which a pipeline consumes records. The source can consume events either by receiving them over HTTPS, or by reading from external endpoints such as Amazon S3. There are two types of sources: *push-based* and *pull-based*. Push-based sources, such as [HTTP](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/http-source/) and [OTel logs](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/otel-logs-source/), stream records to ingestion endpoints. Pull-based sources, such as [OTel trace](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/otel-trace/) and [S3](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/s3/), pull data from the source.

**Processors**  
Intermediate processing units that can filter, transform, and enrich records into a desired format before publishing them to the sink. The processor is an optional component of a pipeline. If you don't define a processor, records are published in the format defined in the source. You can have more than one processor. A pipeline runs processors in the order that you define them.

**Sink**  
The output component of a sub-pipeline. It defines one or more destinations that a sub-pipeline publishes records to. OpenSearch Ingestion supports OpenSearch Service domains as sinks. It also supports sub-pipelines as sinks. This means that you can string together multiple sub-pipelines within a single OpenSearch Ingestion pipeline (YAML file). Self-managed OpenSearch clusters aren't supported as sinks.

**Buffer**  
The part of a processor that acts as the layer between the source and the sink. You can't manually configure a buffer within your pipeline. OpenSearch Ingestion uses a default buffer configuration.

**Route**  
The part of a processor that allows pipeline authors to only send events that match certain conditions to different sinks.

A valid sub-pipeline definition must contain a source and a sink. For more information about each of these pipeline elements, see the [configuration reference](pipeline-config-reference.md#ingestion-parameters). 