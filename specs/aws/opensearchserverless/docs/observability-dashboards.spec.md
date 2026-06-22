---
id: "@specs/aws/opensearchserverless/docs/observability-dashboards"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Dashboards"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Dashboards

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/observability-dashboards
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Dashboards
<a name="observability-dashboards"></a>

Dashboards combine visualizations from logs, traces, and metrics into a single view. You can use dashboards to monitor operational health, respond to incidents, and track resource utilization across your distributed system.

The following table describes common use cases for dashboards.


| Use case | Example | 
| --- | --- | 
| Operational monitoring | Track service health, throughput, and error rates in real time. | 
| Incident response | Correlate logs, traces, and metrics during an active incident. | 
| Capacity planning | Monitor resource utilization trends to plan for scaling. | 
| Availability tracking | Measure uptime and availability against service-level objectives. | 
| Post-incident review | Analyze historical data to understand the root cause of past incidents. | 

![Dashboard showing business metrics and telemetry including product reviews, cart additions, average charge, app availability gauge, request status codes, fault rates, throughput, and API calls.](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/otel-dashboard.png)


## Dashboard structure
<a name="observability-dashboards-structure"></a>

A dashboard is a collection of panels arranged on a grid. Each panel consists of the following components.
+ **Data source** – The OpenSearch index or Amazon Managed Service for Prometheus data source that the panel queries.
+ **Query** – A PPL or PromQL query that retrieves the data for the panel.
+ **Visualization type** – The chart type used to render the query results, such as line, bar, or metric value.
+ **Optional configuration** – Axes, legends, thresholds, and formatting options.

The time range picker at the top of the dashboard applies to all panels. You can override the time range for individual panels when needed.

## Building dashboards from Discover
<a name="observability-dashboards-discover"></a>

The recommended workflow for building dashboards starts in Discover. This workflow is consistent across logs, traces, and metrics.

1. **Query your data in Discover** – Navigate to Discover Logs, Discover Traces, or Discover Metrics and write a query using PPL (for logs and traces) or PromQL (for metrics).

1. **Build a visualization** – When your query returns results, use the visualization tab to choose a chart type and configure the display. For log and trace queries, aggregation commands like `stats` automatically switch to the visualization view.

1. **Save to a dashboard** – Choose **Add to dashboard** to save the visualization to a new or existing dashboard. The panel stays live, updating as new data arrives.

1. **Iterate** – Repeat for each question you want the dashboard to answer. When something looks wrong on a dashboard, choose any panel to open the underlying query in Discover for further investigation.

**Important**  
Visualizations created through the **Visualizations** page in OpenSearch UI use DQL (Dashboards Query Language) and DSL (Domain Specific Language), which do not support Piped Processing Language (PPL) at this time. To create PPL-based visualizations, use the Discover workflow described above.

## Dashboard filters
<a name="observability-dashboards-filters"></a>

Filters let you narrow the data displayed across all panels on a dashboard without editing individual queries.

**To add a filter**

1. Open the dashboard you want to filter.

1. Choose **Add filter** in the filter bar.

1. Select a field name from the dropdown list.

1. Select an operator and enter a value.

1. Choose **Save**.

The following table describes common filter use cases.


| Scenario | Field | Operator | Value | 
| --- | --- | --- | --- | 
| View a single environment | environment | is | production | 
| Isolate errors | status\_code | is greater than or equal to | 400 | 
| Focus on a specific service | service.name | is | order-service | 
| Exclude health checks | http.url | is not | /health | 

**Pinned compared to unpinned filters** – A pinned filter persists when you navigate between dashboards. An unpinned filter applies only to the current dashboard. To pin a filter, choose the pin icon next to the filter badge.

## Building dashboards
<a name="observability-dashboards-build"></a>

### Visualization types
<a name="observability-dashboards-build-viz-types"></a>

The following table describes the visualization types available for dashboard panels.


| Type | Use case | 
| --- | --- | 
| Line | Trends over time, such as request rates or latency | 
| Area | Volume over time with stacked breakdowns | 
| Bar | Comparing values across categories | 
| Horizontal bar | Ranked comparisons, such as top services by error count | 
| Data table | Tabular data with sorting and pagination | 
| Metric value | Single key performance indicators, such as total requests | 
| Gauge | Progress toward a threshold, such as CPU utilization | 
| Pie | Composition and proportions, such as traffic by region | 
| Heat map | Density and distribution patterns over two dimensions | 
| Tag cloud | Relative frequency of terms, such as common error messages | 

### Configuring panels
<a name="observability-dashboards-build-configure"></a>

Each panel has a query editor where you write PPL or PromQL queries. The following examples show common panel queries.

Error count by service (PPL):

```
source = logs-dataset |
    where severity_text = 'ERROR' |
    stats count() as error_count by service_name, span(timestamp, 5m)
```

CPU utilization rate (PromQL):

```
rate(container_cpu_usage_seconds_total{namespace="production"}[5m])
```

You can also configure the following panel options.
+ **Axes** – Set axis labels, scales (linear or logarithmic), and value ranges.
+ **Legends** – Control legend position and which series to display.
+ **Thresholds** – Add horizontal threshold lines to highlight warning or critical levels.

### Layout tips
<a name="observability-dashboards-build-layout"></a>

Use the following tips to organize your dashboard panels effectively.
+ Place high-level summary panels (metric values, gauges) at the top of the dashboard.
+ Group related panels together, such as all panels for a single service.
+ Use consistent widths for panels in the same row.
+ Drag panel edges to resize, and drag panel headers to reposition.

### Recommended layouts
<a name="observability-dashboards-build-recommended"></a>

The following tables describe recommended panel layouts for common dashboard types.

**Service health dashboard**


| Panel | Visualization type | 
| --- | --- | 
| Request rate | Line | 
| Error rate | Line | 
| P99 latency | Line | 
| Active alerts | Metric value | 
| Top errors by service | Horizontal bar | 

**Incident response dashboard**


| Panel | Visualization type | 
| --- | --- | 
| Error logs | Data table | 
| Error count over time | Area | 
| Affected services | Pie | 
| Latency spikes | Line | 

**Resource utilization dashboard**


| Panel | Visualization type | 
| --- | --- | 
| CPU utilization | Gauge | 
| Memory usage over time | Area | 
| Disk I/O | Line | 
| Network throughput | Line | 

### Time range controls
<a name="observability-dashboards-build-time-range"></a>

The time range picker at the top of the dashboard controls the time window for all panels. You can select a preset range (such as **Last 15 minutes** or **Last 24 hours**) or specify a custom absolute range.

To enable auto-refresh, choose the refresh interval dropdown next to the time range picker and select an interval. Auto-refresh re-runs all panel queries at the specified interval so that your dashboard displays the latest data.

## Sharing dashboards
<a name="observability-dashboards-sharing"></a>

You can share dashboards with other users in your organization through URLs, snapshots, and exports.

### Share through URL
<a name="observability-dashboards-sharing-url"></a>

Copy the dashboard URL from your browser address bar and share it directly. The URL preserves the current time range and filters. You can include dashboard links in bookmarks, runbooks, or incident response documentation.

### Snapshots
<a name="observability-dashboards-sharing-snapshots"></a>

A snapshot captures the current state of a dashboard, including all panel data, at a specific point in time. Snapshots are read-only and do not update when the underlying data changes. Use snapshots to preserve a record of dashboard state during incidents or reviews.

### Import and export definitions
<a name="observability-dashboards-sharing-import-export"></a>

You can export a dashboard definition as JSON and import it into another workspace or environment. This approach is useful for promoting dashboards from development to production or sharing standard layouts across teams.

### Best practices for sharing
<a name="observability-dashboards-sharing-best-practices"></a>
+ **Audience** – Design dashboards for a specific audience, such as on-call engineers or leadership.
+ **Focus** – Limit each dashboard to a single purpose or workflow.
+ **Conventions** – Use consistent naming conventions for dashboards and panels across your organization.
+ **Version control** – Export dashboard JSON definitions and store them in version control to track changes over time.

## Troubleshooting dashboards
<a name="observability-dashboards-troubleshooting"></a>

This section describes common dashboard issues and how to resolve them.

### No data in a panel
<a name="observability-dashboards-troubleshooting-no-data"></a>

If a panel displays no data, check the following common causes.


| Cause | Check | Fix | 
| --- | --- | --- | 
| Time range too narrow | Verify that the dashboard time range covers the period when data was ingested. | Expand the time range or select Last 24 hours. | 
| Active filter excluding data | Review the filter bar for filters that might exclude all matching documents. | Remove or adjust the filter, then verify that data appears. | 
| Incorrect index pattern | Confirm that the panel data source points to an index that contains data. | Update the data source to the correct index pattern in the panel editor. | 
| Query syntax error | Look for error messages in the panel header or query editor. | Correct the PPL or PromQL syntax and re-run the query. | 

### Wrong data in a panel
<a name="observability-dashboards-troubleshooting-wrong-data"></a>

If a panel displays unexpected results, try the following steps.
+ Verify that the query returns the expected fields by running it in Discover first.
+ Check that the visualization type matches the data shape (for example, use a line chart for time-series data).
+ Confirm that the correct data source is selected in the panel editor.

### Stale data
<a name="observability-dashboards-troubleshooting-stale-data"></a>

If dashboard panels display outdated information, try the following steps.
+ Choose the refresh icon in the toolbar to manually refresh all panels.
+ Verify that auto-refresh is enabled and set to an appropriate interval.
+ Confirm that your ingestion pipeline is actively sending data to the configured indexes.

### Performance issues
<a name="observability-dashboards-troubleshooting-performance"></a>

The following tips can help you resolve common performance issues.
+ **Slow dashboard** – Reduce the number of panels or narrow the time range. Dashboards with many panels run multiple queries simultaneously, which can increase load times.
+ **Slow panel** – Simplify the panel query. Avoid using wildcard patterns in PPL `where` clauses and limit the number of aggregation buckets.
+ **Browser lag** – Reduce the data density in visualizations. For example, increase the time span interval in `stats` commands to produce fewer data points.

### Filter issues
<a name="observability-dashboards-troubleshooting-filters"></a>

If filters do not behave as expected, try the following steps.
+ Verify that the field name in the filter matches the field name in the index mapping.
+ Check whether a pinned filter from another dashboard is affecting results.
+ Remove all filters and add them back one at a time to isolate the issue.

### Inspect a panel
<a name="observability-dashboards-troubleshooting-inspect"></a>

The panel inspector helps you debug data and query issues. To open the inspector, choose the panel menu (three dots) and select **Inspect**. The inspector provides the following tabs.
+ **Data** – Displays the raw data returned by the query in tabular format.
+ **Request** – Shows the query sent to the data source, including the full PPL or PromQL statement.
+ **Response** – Shows the raw response from the data source, including timing and status information.

### Browser developer tools
<a name="observability-dashboards-troubleshooting-browser"></a>

For advanced troubleshooting, use your browser developer tools to inspect network requests. Open the **Network** tab, filter for API calls, and look for failed requests or slow responses. Check the response body for error messages that can help you identify the root cause.