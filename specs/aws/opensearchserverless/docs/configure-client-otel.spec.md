---
id: "@specs/aws/opensearchserverless/docs/configure-client-otel"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS OpenTelemetry Collector"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# OpenTelemetry Collector

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/configure-client-otel
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Using an OpenSearch Ingestion pipeline with OpenTelemetry Collector
<a name="configure-client-otel"></a>

You can use the [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/) to ingest logs, traces, and metrics into OpenSearch Ingestion pipelines. A single pipeline can be used to ingest all logs, traces, and metrics to different indices on a domain or collection. You can also use pipelines to ingest only logs, traces, or metrics individually. 

**Topics**
+ [Prerequisites](#otel-prereqs)
+ [Step 1: Configure the pipeline role](#otel-pipeline-role)
+ [Step 2: Create the pipeline](#create-otel-pipeline)
+ [Cross-account Connectivity](#x-account-connectivity)
+ [Limitations](#otel-limitations)
+ [Recommended CloudWatch Alarms for OpenTelemetry sources](#otel-pipeline-metrics)

## Prerequisites
<a name="otel-prereqs"></a>

While setting up the [OpenTelemetry configuration file](https://opentelemetry.io/docs/collector/configuration/), you must configure the following in order for ingestion to occur: 
+ The ingestion role needs the `osis:Ingest` permission to interact with the pipeline. For more information, see [Ingestion role](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/pipeline-security-overview.html#pipeline-security-same-account). 
+ The endpoint value must include your pipeline endpoint. For example, `https://pipeline-endpoint.us-east-1.osis.amazonaws.com.`
+ The service value must be `osis`.
+ The compression option for the OTLP/HTTP Exporter must match the compression option on the pipeline's selected source.

```
extensions:
    sigv4auth:
        region: "region"
        service: "osis"

exporters:
    otlphttp:
        logs_endpoint: "https://pipeline-endpoint.us-east-1.osis.amazonaws.com/v1/logs"
        metrics_endpoint: "https://pipeline-endpoint.us-east-1.osis.amazonaws.com/v1/metrics"
        traces_endpoint: "https://pipeline-endpoint.us-east-1.osis.amazonaws.com/v1/traces"
        auth:
            authenticator: sigv4auth
        compression: none

service:
    extensions: [sigv4auth]
    pipelines:
        traces:
        receivers: [jaeger]
        exporters: [otlphttp]
```

## Step 1: Configure the pipeline role
<a name="otel-pipeline-role"></a>

 After setting up the OpenTelemetry collector configuration, [ set up the pipeline role](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/pipeline-security-overview.html#pipeline-security-sink) that you want to use in your pipeline configuration. There are not specific permissions that the pipeline role needs for the OTLP source, only permissions to grant pipelines access to the OpenSearch domain or collection. 

## Step 2: Create the pipeline
<a name="create-otel-pipeline"></a>

 You can then configure an OpenSearch Ingestion pipeline like the following, which specifies OTLP as the source. You can also configure OpenTelemetry logs, metrics, and traces as individual sources. 

OTLP source pipeline configuration:

```
version: 2
otlp-pipeline:
    source:
        otlp:
            logs_path: /otlp-pipeline/v1/logs
            traces_path: /otlp-pipeline/v1/traces
            metrics_path: /otlp-pipeline/v1/metrics
    sink:
        - opensearch:
            hosts: ["https://search-mydomain.region.es.amazonaws.com"]
            index: "ss4o_metrics-otel-%{yyyy.MM.dd}"
            index_type: custom
            aws:
                region: "region"
```

OpenTelemetry Logs pipeline configuration:

```
version: 2
otel-logs-pipeline:
  source:
    otel_logs_source:
        path: /otel-logs-pipeline/v1/logs
  sink:
    - opensearch:
        hosts: ["https://search-mydomain.region.es.amazonaws.com"]
        index: "ss4o_metrics-otel-%{yyyy.MM.dd}"
        index_type: custom
        aws:
            region: "region"
```

OpenTelemetry Metrics pipeline configuration:

```
version: 2
otel-metrics-pipeline:
  source:
    otel_metrics_source:
        path: /otel-metrics-pipeline/v1/metrics
  sink:
    - opensearch:
        hosts: ["https://search-mydomain.region.es.amazonaws.com"]
        index: "ss4o_metrics-otel-%{yyyy.MM.dd}"
        index_type: custom
        aws:
            region: "region"
```

OpenTelemetry Traces pipeline configuration:

```
version: 2
otel-trace-pipeline:
  source:
    otel_trace_source:
        path: /otel-traces-pipeline/v1/traces
  sink:
    - opensearch:
        hosts: ["https://search-mydomain.region.es.amazonaws.com"]
        index: "ss4o_metrics-otel-%{yyyy.MM.dd}"
        index_type: custom
        aws:
            region: "region"
```

You can use a preconfigured blueprint to create this pipeline. For more information, see [Working with blueprints](pipeline-blueprint.md). 

## Cross-account Connectivity
<a name="x-account-connectivity"></a>

 OpenSearch Ingestion pipelines with OpenTelemetry sources have cross-account ingestion capability. Amazon OpenSearch Ingestion enables you to share pipelines across AWS accounts from a virtual private cloud (VPC) to a pipeline endpoint in a separate VPC. For more information, see [Configuring OpenSearch Ingestion pipelines for cross-account ingestion](cross-account-pipelines.md). 

## Limitations
<a name="otel-limitations"></a>

 The OpenSearch Ingestion pipeline cannot receive any requests greater than 20mb. This value is configured by the user in the `max_request_length` option. This option defaults to 10mb. 

## Recommended CloudWatch Alarms for OpenTelemetry sources
<a name="otel-pipeline-metrics"></a>

 The following CloudWatch metrics are recommended for monitoring the performance of your ingestion pipeline. These metrics can help you identify the amount of data processed from exports, the amount of events processed from streams, the errors in processing exports and stream events, and the number of documents written to the destination. You can setup CloudWatch alarms to perform an action when one of these metrics exceed a specified value for a specified amount of time. 

 The CloudWatch metrics for OTLP source are formatted as `{pipeline-name}.otlp.{logs | traces | metrics}.{metric-name}`. For example, `otel-pipeline.otlp.metrics.requestTimeouts.count`. 

 In the case of using an individual OpenTelemetry source, the metrics will be formatted as `{pipeline-name}.{source-name}.{metric-name}`. For example, `trace-pipeline.otel_trace_source.requestTimeouts.count`. 

All three OpenTelemetry data types will have the same metrics, but for brevity the metrics will only be listed in the below table for OTLP source log type data.


| Metric | Description | 
| --- |--- |
| otel-pipeline.BlockingBuffer.bufferUsage.value | Indicates how much of the buffer is being utilized. | 
|  otel-pipeline.otlp.logs.requestTimeouts.count  | The number of requests that have timed out. | 
|  otel-pipeline.otlp.logs.requestsReceived.count  | The number of requests received by the OpenTelemetry Collector. | 
|  otel-pipeline.otlp.logs.badRequests.count  | The number of malformed requests received by the OpenTelemetry Collector. | 
|  otel-pipeline.otlp.logs.requestsTooLarge.count  | The number of requests greater than the maximum of 20mb received by the OpenTelemetry Collector. | 
|  otel-pipeline.otlp.logs.internalServerError.count  | The number of HTTP 500 errors received from the OpenTelemetry Collector. | 
|  otel-pipeline.opensearch.bulkBadRequestErrors.count  | Count of errors during bulk requests due to malformed request. | 
|  otel-pipeline.opensearch.bulkRequestLatency.avg  | Average latency for bulk write requests made to OpenSearch. | 
|  otel-pipeline.opensearch.bulkRequestNotFoundErrors.count  | Number of bulk requests that failed because the target data could not be found. | 
|  otel-pipeline.opensearch.bulkRequestNumberOfRetries.count  | Number of retries by OpenSearch Ingestion pipelines to write OpenSearch cluster. | 
|  otel-pipeline.opensearch.bulkRequestSizeBytes.sum  | Total size in bytes of all bulk requests made to OpenSearch. | 
|  otel-pipeline.opensearch.documentErrors.count  | Number of errors when sending documents to OpenSearch. The documents causing the errors witll be sent to DLQ. | 
|  otel-pipeline.opensearch.documentsSuccess.count  | Number of documents successfully written to an OpenSearch cluster or collection. | 
|  otel-pipeline.opensearch.documentsSuccessFirstAttempt.count  | Number of documents successfully indexed in OpenSearch on the first attempt. | 
| `otel-pipeline.opensearch.documentsVersionConflictErrors.count` | Count of errors due to version conflicts in documents during processing. | 
| `otel-pipeline.opensearch.PipelineLatency.avg` | Average latency of OpenSearch Ingestion pipeline to process the data by reading from the source to writing to the destination. | 
|  otel-pipeline.opensearch.PipelineLatency.max  | Maximum latency of OpenSearch Ingestion pipeline to process the data by reading from the source to writing the destination. | 
|  otel-pipeline.opensearch.recordsIn.count  | Count of records successfully ingested into OpenSearch. This metric is essential for tracking the volume of data being processed and stored. | 
|  otel-pipeline.opensearch.s3.dlqS3RecordsFailed.count  | Number of records that failed to write to DLQ. | 
|  otel-pipeline.opensearch.s3.dlqS3RecordsSuccess.count  | Number of records that are written to DLQ. | 
|  otel-pipeline.opensearch.s3.dlqS3RequestLatency.count  | Count of latency measurements for requests to the Amazon S3 dead-letter queue. | 
|  otel-pipeline.opensearch.s3.dlqS3RequestLatency.sum  | Total latency for all requests to the Amazon S3 dead-letter queue | 
|  otel-pipeline.opensearch.s3.dlqS3RequestSizeBytes.sum  | Total size in bytes of all requests made to the Amazon S3 dead-letter queue. | 
|  otel-pipeline.recordsProcessed.count  | Total number of records processed in the pipeline, a key metric for overal throughput. | 
| `otel-pipeline.opensearch.bulkRequestInvalidInputErrors.count` | Count of bulk request errors in OpenSearch due to invalid input, crucial for monitoring data quality and operational issues. | 