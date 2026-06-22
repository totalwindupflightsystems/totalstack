---
id: "@specs/aws/opensearchserverless/docs/observability-get-started"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Get started"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Get started

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/observability-get-started
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Get started
<a name="observability-get-started"></a>

Get your observability stack running on AWS and start sending telemetry data in minutes.

## Quick start
<a name="observability-get-started-quick"></a>

The fastest way to deploy an end-to-end observability stack on AWS is the CLI installer. It creates the following resources:
+ An Amazon OpenSearch Service domain
+ An Amazon Managed Service for Prometheus workspace
+ An Amazon OpenSearch Ingestion pipeline
+ An OpenSearch UI application with an observability workspace

Optionally, the installer launches an EC2 instance with the OpenTelemetry Demo for sample telemetry.

Run the following command to start the installation:

```
bash -c "$(curl -fsSL https://raw.githubusercontent.com/opensearch-project/observability-stack/main/install.sh)" -- --deployment-target=aws
```

The installation takes approximately 15 minutes.

## CDK deployment
<a name="observability-get-started-cdk"></a>

For infrastructure-as-code, use AWS CDK. The CDK deployment creates two stacks:


| Stack | What it creates | Deploy time | 
| --- | --- | --- | 
| ObsInfra | OpenSearch domain, Amazon Managed Service for Prometheus workspace, direct query data source, pipeline IAM role | \~17 min | 
| ObservabilityStack | Fine-grained access control mapping, OpenSearch Ingestion pipeline, OpenSearch UI application, dashboard initialization, demo workload (optional) | \~6 min | 

Run the following commands to deploy:

```
cd aws/cdk
npm install
cdk deploy --all
```

For more information, see the [CDK deployment README](https://github.com/opensearch-project/observability-stack/tree/main/aws/cdk) on GitHub.

## Sending telemetry
<a name="observability-get-started-send"></a>

Both deployment methods create an OpenSearch Ingestion endpoint that accepts OTLP data. Configure your OTel Collector to export using SigV4 authentication:

```
extensions:
  sigv4auth:
    region: us-west-2
    service: osis

exporters:
  otlphttp/logs:
    logs_endpoint: ${OSIS_ENDPOINT}/v1/logs
    auth: { authenticator: sigv4auth }
    compression: none
  otlphttp/traces:
    traces_endpoint: ${OSIS_ENDPOINT}/v1/traces
    auth: { authenticator: sigv4auth }
    compression: none
  otlphttp/metrics:
    metrics_endpoint: ${OSIS_ENDPOINT}/v1/metrics
    auth: { authenticator: sigv4auth }
    compression: none
```

**Note**  
The IAM principal sending data needs `osis:Ingest` and `aps:RemoteWrite` permission on the pipeline ARN.

## Learn more
<a name="observability-get-started-learn-more"></a>

Use the following resources to learn more about sending telemetry data:
+ [OpenTelemetry instrumentation guides (per-language)](https://observability.opensearch.org/docs/send-data/applications/)
+ [Infrastructure monitoring (AWS, Docker, Kubernetes, Prometheus)](https://observability.opensearch.org/docs/send-data/infrastructure/)
+ [OTel Collector configuration](https://observability.opensearch.org/docs/send-data/opentelemetry/collector/)
+ [Data pipeline and batching](https://observability.opensearch.org/docs/send-data/data-pipeline/)
+ [Overview of Amazon OpenSearch Ingestion](ingestion.md) in this guide