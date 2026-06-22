---
id: "@specs/aws/opensearchserverless/docs/configure-client-prometheus"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Amazon Managed Service for Prometheus"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Amazon Managed Service for Prometheus

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/configure-client-prometheus
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Using an OpenSearch Ingestion pipeline with Amazon Managed Service for Prometheus
<a name="configure-client-prometheus"></a>

You can use Amazon Managed Service for Prometheus as a destination for your OpenSearch Ingestion pipeline to store metrics in time series format. The Prometheus sink allows you to send OpenTelemetry metrics or other time series data from your pipeline to an Amazon Managed Service for Prometheus workspace for monitoring, alerting, and analysis.

The `prometheus` sink plugin enables OpenSearch Ingestion pipelines to write metrics data to Amazon Managed Service for Prometheus workspaces using the Prometheus remote write protocol. This integration allows you to:
+ Store time series metrics data in Amazon Managed Service for Prometheus
+ Monitor and alert on metrics using Amazon Managed Service for Prometheus and Amazon Managed Grafana
+ Route metrics to multiple destinations simultaneously (for example, OpenSearch and Amazon Managed Service for Prometheus)
+ Process OpenTelemetry metrics from external agents or generate metrics within the pipeline

**Topics**
+ [Prerequisites](#prometheus-prereqs)
+ [Step 1: Configure the pipeline role](#prometheus-pipeline-role)
+ [Step 2: Create the pipeline](#prometheus-pipeline)
+ [Monitoring and troubleshooting](#prometheus-monitoring)
+ [Limitations](#prometheus-limitations)
+ [Best practices](#prometheus-best-practices)

## Prerequisites
<a name="prometheus-prereqs"></a>

Before you configure the Prometheus sink, ensure you have the following:
+ **Amazon Managed Service for Prometheus workspace**: Create a workspace in the same AWS account and AWS Region as your OpenSearch Ingestion pipeline. For instructions, see [Creating a workspace](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-onboard-create-workspace.html) in the *Amazon Managed Service for Prometheus User Guide*.
+ **IAM permissions**: Configure an IAM role with permissions to write to Amazon Managed Service for Prometheus. For more information, see [Step 1: Configure the pipeline role](#prometheus-pipeline-role).

## Step 1: Configure the pipeline role
<a name="prometheus-pipeline-role"></a>

The Prometheus sink automatically inherits the [pipeline role's](pipeline-security-overview.md#pipeline-security-sink) IAM permissions for authentication, so no additional role configuration (like `sts_role_arn`) is required in the sink settings.

The following sample policy shows the required permissions for using Amazon Managed Service for Prometheus as a sink:

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "AMPRemoteWrite",
      "Effect": "Allow",
      "Action": [
        "aps:RemoteWrite"
      ],
      "Resource": "arn:aws:aps:{{region}}:{{account-id}}:workspace/{{workspace-id}}"
    }
  ]
}
```

Replace the following placeholders:
+ `{{region}}`: Your AWS Region (for example, `us-east-1`)
+ `{{account-id}}`: Your AWS account ID
+ `{{workspace-id}}`: Your Amazon Managed Service for Prometheus workspace ID

You must attach these permissions to your pipeline role.

Ensure your pipeline role has a trust relationship that allows OpenSearch Ingestion to assume it:

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "osis-pipelines.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

## Step 2: Create the pipeline
<a name="prometheus-pipeline"></a>

After you've set up your permissions, you can configure an OpenSearch Ingestion pipeline to use Amazon Managed Service for Prometheus as a sink.

### Basic configuration
<a name="prometheus-basic-config"></a>

The following example shows a minimal Prometheus sink configuration:

```
version: "2"
sink:
  - prometheus:
      url: "https://aps-workspaces.{{region}}.amazonaws.com/workspaces/{{workspace-id}}/api/v1/remote_write"
      aws:
        region: "{{region}}"
```

You must specify the `url` option within the `prometheus` sink configuration, which is the Amazon Managed Service for Prometheus remote write endpoint. To format the URL, locate your workspace ID in the Amazon Managed Service for Prometheus console and construct the URL as follows: `https://aps-workspaces.{{region}}.amazonaws.com/workspaces/{{workspace-id}}/api/v1/remote_write`.

### Configuration options
<a name="prometheus-config-options"></a>

Use the following options to configure batching and flushing behavior for the Prometheus sink:


**Prometheus sink configuration options**  

| Option | Required | Type | Description | 
| --- | --- | --- | --- | 
| max\_events | No | Integer | The maximum number of events to accumulate before flushing to Prometheus. Default is 1000. | 
| max\_request\_size | No | Byte Count | The maximum size of the request payload before flushing. Default is 1mb. | 
| flush\_interval | No | Duration | The maximum amount of time to wait before flushing events. Default is 10s. Maximum allowed value is 60s. | 

### Example pipelines
<a name="prometheus-example-pipelines"></a>

**Example 1: OpenTelemetry metrics to Amazon Managed Service for Prometheus**

This pipeline receives OpenTelemetry metrics from an external agent and writes them to Amazon Managed Service for Prometheus:

```
version: "2"
source:
  otel_metrics_source:
    path: "/v1/metrics"
    output_format: otel

sink:
  - prometheus:
      url: "https://aps-workspaces.us-east-1.amazonaws.com/workspaces/ws-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/api/v1/remote_write"
      aws:
        region: "us-east-1"
```

**Example 2: Dual sink - OpenSearch and Amazon Managed Service for Prometheus**

This pipeline routes metrics to both OpenSearch and Amazon Managed Service for Prometheus:

```
version: "2"
source:
  otel_metrics_source:
    path: "/v1/metrics"
    output_format: otel

sink:
  - opensearch:
      hosts:
        - "https://search-{{domain-endpoint}}.{{us-east-1}}.es.amazonaws.com"
      index: "metrics-%{yyyy.MM.dd}"
      aws:
        region: "us-east-1"
        sts_role_arn: "arn:aws:iam::123456789012:role/OSI-Pipeline-Role"

  - prometheus:
      url: "https://aps-workspaces.us-east-1.amazonaws.com/workspaces/ws-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/api/v1/remote_write"
      aws:
        region: "us-east-1"
```

**Example 3: Metrics with filtering**

This pipeline filters metrics before sending to Amazon Managed Service for Prometheus:

```
version: "2"
source:
  otel_metrics_source:
    path: "/v1/metrics"
    output_format: otel

processor:
  - drop_events:
      drop_when: '/name != "http.server.duration" and /name != "http.client.duration"'

sink:
  - prometheus:
      url: "https://aps-workspaces.us-east-1.amazonaws.com/workspaces/ws-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/api/v1/remote_write"
      aws:
        region: "us-east-1"
```

You can use a preconfigured Amazon Managed Service for Prometheus blueprint to create these pipelines. For more information, see [Working with blueprints](pipeline-blueprint.md).

### Creating a pipeline with Amazon Managed Service for Prometheus sink
<a name="prometheus-create-pipeline"></a>

#### Using the AWS Console
<a name="prometheus-console"></a>

1. Navigate to the OpenSearch Service console.

1. Choose **Pipelines** under **Ingestion**.

1. Choose **Create pipeline**.

1. Select **Build using blueprint** and choose the **OpenTelemetry metrics to Amazon Prometheus** blueprint.

1. Configure the pipeline:
   + Enter your Amazon Managed Service for Prometheus workspace ID
   + Specify the pipeline role ARN
   + Configure source and processor settings as needed

1. Review and create the pipeline.

#### Using the AWS CLI
<a name="prometheus-cli"></a>

Create a pipeline configuration file (for example, `amp-pipeline.yaml`) with your desired configuration, then run:

```
aws osis create-pipeline \
  --pipeline-name my-amp-pipeline \
  --min-units 2 \
  --max-units 4 \
  --pipeline-configuration-body file://amp-pipeline.yaml
```

#### Using AWS CloudFormation
<a name="prometheus-cfn"></a>

```
Resources:
  MyAMPPipeline:
    Type: AWS::OSIS::Pipeline
    Properties:
      PipelineName: my-amp-pipeline
      MinUnits: 2
      MaxUnits: 4
      PipelineConfigurationBody: |
        version: "2"
        source:
          otel_metrics_source:
            path: "/v1/metrics"
            output_format: otel
        sink:
          - prometheus:
              url: "https://aps-workspaces.us-east-1.amazonaws.com/workspaces/ws-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/api/v1/remote_write"
              aws:
                region: "us-east-1"
```

## Monitoring and troubleshooting
<a name="prometheus-monitoring"></a>

### CloudWatch metrics
<a name="prometheus-cloudwatch-metrics"></a>

Monitor your pipeline's performance using CloudWatch metrics:
+ `DocumentsWritten`: Number of metrics successfully written to Amazon Managed Service for Prometheus
+ `DocumentsWriteFailed`: Number of metrics that failed to write
+ `RequestLatency`: Latency of remote write requests

### Common issues
<a name="prometheus-troubleshooting"></a>

**Issue**: Pipeline fails to write to Amazon Managed Service for Prometheus

**Solutions**:
+ Verify the workspace ID and region in the URL are correct
+ Ensure the pipeline role has `aps:RemoteWrite` permission
+ Check that the workspace uses service-managed AWS KMS keys
+ Verify the pipeline and workspace are in the same AWS account

**Issue**: Authentication errors

**Solutions**:
+ Verify the trust relationship allows `osis-pipelines.amazonaws.com` to assume the pipeline role
+ Ensure the pipeline role has the required `aps:RemoteWrite` permission

**Issue**: High latency or throttling

**Solutions**:
+ Increase pipeline capacity units
+ Implement batching in the processor
+ Review Amazon Managed Service for Prometheus service quotas

## Limitations
<a name="prometheus-limitations"></a>

Consider the following limitations when you set up an OpenSearch Ingestion pipeline for Amazon Managed Service for Prometheus:
+ Amazon Managed Service for Prometheus workspaces must use AWS service-managed AWS KMS keys. Customer-managed AWS KMS keys are not currently supported.
+ The pipeline and Amazon Managed Service for Prometheus workspace must be in the same AWS account.

## Best practices
<a name="prometheus-best-practices"></a>
+ **Use the same IAM role**: The Prometheus sink automatically uses the pipeline role. If other sinks are used, ensure the `sts_role_arn` is the same as the pipeline role
+ **Monitor metrics**: Set up CloudWatch alarms for failed writes and high latency
+ **Implement filtering**: Use processors to filter unnecessary metrics before sending to Amazon Managed Service for Prometheus
+ **Right-size capacity**: Start with minimum capacity and scale based on metrics volume
+ **Use blueprints**: Leverage pre-configured blueprints for common use cases