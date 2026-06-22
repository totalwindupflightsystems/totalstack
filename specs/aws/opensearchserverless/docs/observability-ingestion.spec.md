---
id: "@specs/aws/opensearchserverless/docs/observability-ingestion"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Ingesting application telemetry"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Ingesting application telemetry

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/observability-ingestion
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Ingesting application telemetry
<a name="observability-ingestion"></a>

To use observability features in Amazon OpenSearch Service, you need to ingest application traces, logs, and metrics. This page covers configuring the OpenTelemetry Collector and OpenSearch Ingestion pipelines to process and route telemetry data to OpenSearch and Amazon Managed Service for Prometheus.

## Configuring the OpenTelemetry Collector
<a name="observability-ingestion-otel"></a>

The OpenTelemetry (OTel) Collector is the entry point for all application telemetry. It receives data through OTLP and routes traces and logs to OpenSearch Ingestion while sending metrics to Prometheus.

You can configure the OTel Collector using one of the following approaches:

The OTel Collector exports traces and logs to an OpenSearch Ingestion endpoint using SigV4 authentication, and metrics to Amazon Managed Service for Prometheus using the Prometheus remote write exporter. OpenSearch Ingestion handles processing, enrichment, and routing to OpenSearch.

### OTel Collector configuration with OpenSearch Ingestion
<a name="observability-ingestion-otel-osis"></a>

The following example configuration uses SigV4 authentication to export traces and logs to an OpenSearch Ingestion endpoint, and metrics to Prometheus:

```
extensions:
  sigv4auth:
    region: {{us-west-2}}
    service: osis

exporters:
  otlphttp/osis-traces:
    traces_endpoint: ${OSIS_ENDPOINT}/v1/traces
    auth: { authenticator: sigv4auth }
    compression: none
  otlphttp/osis-logs:
    logs_endpoint: ${OSIS_ENDPOINT}/v1/logs
    auth: { authenticator: sigv4auth }
    compression: none
  # Amazon Managed Service for Prometheus via Prometheus Remote Write with SigV4 auth
  prometheusremotewrite/amp:
    endpoint: "https://aps-workspaces.{{region}}.amazonaws.com/workspaces/{{workspace-id}}/api/v1/remote_write"
    auth:
      authenticator: sigv4auth

service:
  extensions: [sigv4auth]
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch]
      exporters: [otlphttp/osis-traces]
    logs:
      receivers: [otlp]
      processors: [batch]
      exporters: [otlphttp/osis-logs]
    metrics:
      receivers: [otlp]
      processors: [batch]
      exporters: [prometheusremotewrite/amp]
```

**Note**  
The IAM principal sending data needs `osis:Ingest` and `aps:RemoteWrite` permission on the pipeline ARN.

## Configuring OpenSearch Ingestion pipelines
<a name="observability-ingestion-pipelines"></a>

OpenSearch Ingestion (or self-managed Data Prepper) receives telemetry from the OTel Collector and processes it for application performance monitoring (APM).

### Pipeline architecture
<a name="observability-ingestion-pipeline-arch"></a>

The pipeline processes telemetry data in the following stages:

1. The entry pipeline receives all telemetry and routes logs and traces to separate sub-pipelines.

1. The log pipeline writes log data to OpenSearch using the `log-analytics-plain` index type.

1. The trace pipeline distributes spans to the raw storage pipeline and the service map pipeline.

1. The raw trace pipeline processes spans with the `otel_traces` processor and stores them in the `trace-analytics-plain-raw` index type.

1. The service map pipeline uses the `otel_apm_service_map` processor to generate topology and RED (Rate, Errors, Duration) metrics. It writes to OpenSearch and to Prometheus through remote write.

### Pipeline configuration
<a name="observability-ingestion-pipeline-config"></a>

The following example shows a complete pipeline configuration for OpenSearch Ingestion that covers all observability signal types – logs, traces, and metrics. You can include all pipelines or only the ones relevant to your use case. Replace the {{placeholder}} values with your own information.

```
version: '2'

# Main OTLP pipeline - receives all telemetry and routes by signal type
otlp-pipeline:
  source:
    otlp:
      logs_path: '/{{pipeline-name}}/v1/logs'
      traces_path: '/{{pipeline-name}}/v1/traces'
      metrics_path: '/{{pipeline-name}}/v1/metrics'
  route:
    - logs: 'getEventType() == "LOG"'
    - traces: 'getEventType() == "TRACE"'
    - metrics: 'getEventType() == "METRIC"'
  processor: []
  sink:
    - pipeline:
        name: otel-logs-pipeline
        routes:
          - logs
    - pipeline:
        name: otel-traces-pipeline
        routes:
          - traces
    - pipeline:
        name: otel-metrics-pipeline
        routes:
          - metrics

# Log processing pipeline
otel-logs-pipeline:
  source:
    pipeline:
      name: otlp-pipeline
  processor:
    - copy_values:
        entries:
          - from_key: "time"
            to_key: "@timestamp"
  sink:
    - opensearch:
        hosts:
          - 'https://{{opensearch-endpoint}}'
        index_type: log-analytics-plain
        aws:
          serverless: false
          region: '{{region}}'
          sts_role_arn: "arn:aws:iam::{{account-id}}:role/{{pipeline-role}}"

# Trace fan-out pipeline
otel-traces-pipeline:
  source:
    pipeline:
      name: otlp-pipeline
  processor: []
  sink:
    - pipeline:
        name: traces-raw-pipeline
        routes: []
    - pipeline:
        name: service-map-pipeline
        routes: []

# Raw trace storage pipeline
traces-raw-pipeline:
  source:
    pipeline:
      name: otel-traces-pipeline
  processor:
    - otel_traces:
  sink:
    - opensearch:
        hosts:
          - 'https://{{opensearch-endpoint}}'
        index_type: trace-analytics-plain-raw
        aws:
          serverless: false
          region: '{{region}}'
          sts_role_arn: "arn:aws:iam::{{account-id}}:role/{{pipeline-role}}"

# Service map generation pipeline (APM)
service-map-pipeline:
  source:
    pipeline:
      name: otel-traces-pipeline
  processor:
    - otel_apm_service_map:
        group_by_attributes:
          - telemetry.sdk.language # Add any resource attribute to group by
        window_duration: 30s
  route:
    - otel_apm_service_map_route: 'getEventType() == "SERVICE_MAP"'
    - service_processed_metrics: 'getEventType() == "METRIC"'
  sink:
    - opensearch:
        hosts:
          - 'https://{{opensearch-endpoint}}'
        aws:
          serverless: false
          region: '{{region}}'
          sts_role_arn: "arn:aws:iam::{{account-id}}:role/{{pipeline-role}}"
        routes:
          - otel_apm_service_map_route
        index_type: otel-v2-apm-service-map
    - prometheus:
        url: 'https://aps-workspaces.{{region}}.amazonaws.com/workspaces/{{workspace-id}}/api/v1/remote_write'
        aws:
          region: '{{region}}'
        routes:
          - service_processed_metrics

# Metrics processing pipeline
otel-metrics-pipeline:
  source:
    pipeline:
      name: otlp-pipeline
  processor:
    - otel_metrics:
  sink:
    - prometheus:
        url: 'https://aps-workspaces.{{region}}.amazonaws.com/workspaces/{{workspace-id}}/api/v1/remote_write'
        aws:
          region: '{{region}}'
```

## Verifying ingestion
<a name="observability-ingestion-verify"></a>

After you configure the OTel Collector and pipelines, verify that telemetry data is flowing correctly.
+ **Verify OpenSearch indexes** – Confirm that the following indexes exist in your domain: `otel-v1-apm-span-*`, `otel-v2-apm-service-map`, and `logs-otel-v1-*`.
+ **Verify Prometheus targets** – Confirm that the Prometheus remote write target is receiving metrics from the service map pipeline.
+ **Verify in OpenSearch UI** – Navigate to **Observability**, then **Application Monitoring** to confirm that your services appear.

## Next steps
<a name="observability-ingestion-next"></a>

After you verify that telemetry data is ingested, explore the following topics:
+ [Application monitoring](observability-app-monitoring.md) – Monitor application health with service maps and RED metrics.
+ [Discover traces](observability-analyze-traces.md) – Discover and analyze distributed traces.
+ [Discover logs](observability-analyze-logs.md) – Discover and query application logs.
+ [Discover metrics](observability-metrics.md) – Discover and query Prometheus metrics using PromQL.