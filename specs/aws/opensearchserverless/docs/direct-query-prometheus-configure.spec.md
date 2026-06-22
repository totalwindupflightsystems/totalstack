---
id: "@specs/aws/opensearchserverless/docs/direct-query-prometheus-configure"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Configuring and querying a Managed Prometheus data source"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Configuring and querying a Managed Prometheus data source

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/direct-query-prometheus-configure
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Querying Prometheus metrics
<a name="direct-query-prometheus-configure"></a>

Amazon OpenSearch Service allows you to query your Prometheus data using PromQL (Prometheus Query Language) directly from the Observability interface. When you execute a PromQL query against the Prometheus data source, OpenSearch Service passes the query directly to your workspace API for execution.

## Running a PromQL query
<a name="direct-query-prometheus-query"></a>

To run a query:

1. Open your OpenSearch UI application and observability workspace.

1. Navigate to **Observability** and select **Discover Metrics**.

1. In the data source drop-down, select your Prometheus data source.

1. Enter your PromQL query in the query bar.

For example, to find the average per-second CPU usage over a 5-minute window for a specific pod:

```
avg(rate(container_cpu_usage_seconds_total{pod="payment-service-pod"}[5m])) by (pod)
```

**Note**  
Set your time picker to a narrow, relevant window (for example, the last 1 hour) to optimize API performance and prevent timeouts.

## Visualizing metrics in dashboards
<a name="direct-query-prometheus-dashboards"></a>

You can add PromQL-driven metric visualizations to your existing observability dashboards to correlate them with your log and trace data.

1. Navigate to **Discover Metrics**, select your Prometheus workspace from the data source drop-down, and run your PromQL query.

1. Use the visualization tab in **Discover Metrics** to create a visualization and define your visualization type.

1. Save the visualization to your dashboard.

**Note**  
Metric visualizations can only be added from **Discover Metrics**. Visualizations found on the visualizations tab are only optimized for logs.