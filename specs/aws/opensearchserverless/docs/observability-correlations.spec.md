---
id: "@specs/aws/opensearchserverless/docs/observability-correlations"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Correlations"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Correlations

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/observability-correlations
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Correlations
<a name="observability-correlations"></a>

Correlations link a traces dataset to a logs dataset so that you can view related log entries when you investigate trace spans. By defining a correlation, you enable the Discover Traces page to display logs that occurred during a span's execution, helping you diagnose issues faster without switching between pages.

## Correlation requirements
<a name="observability-correlations-requirements"></a>

To create a correlation, your log and trace data must contain matching fields. The following table describes the fields that the correlation uses to join trace and log data.


| Field | Description | Required | 
| --- | --- | --- | 
| Trace ID | The unique identifier for the trace. Must exist in both the trace span index and the log index. | Yes | 
| Span ID | The unique identifier for the span. Used to match logs to a specific span within a trace. | No | 
| Service name | The name of the service that generated the telemetry. Used to filter related logs by service. | No | 
| Timestamp | The time field used to scope related logs to the span's time range. | Yes | 

## To create a trace-to-logs correlation
<a name="observability-correlations-create"></a>

Complete the following steps to create a correlation between a traces dataset and a logs dataset.

1. In your observability workspace, expand **Discover** in the left navigation and choose **Traces**.

1. Select the traces dataset that you want to correlate.

1. Choose the **Correlations** tab in the dataset configuration panel.  
![Correlated datasets tab showing no correlations exist with option to create correlation.](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/datasets/correlations-trace-dataset-tab.png)

1. Choose **Create correlation**.

1. In the configuration dialog, select the target logs dataset and map the required correlation fields (trace ID and timestamp). Optionally, map span ID and service name for more precise matching.  
![Configure correlation dialog showing Logs Dataset mapped to trace fields including time, traceId, spanId, and service name.](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/datasets/correlations-configure-dialog.png)

1. Choose **Create** to save the correlation.

1. Verify that the correlation appears in the correlations table.  
![Correlations table showing Trace-to-logs correlation type linking Trace Dataset to Logs Dataset.](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/datasets/correlations-created-table.png)

## Viewing correlations in logs datasets
<a name="observability-correlations-view-logs"></a>

After you create a correlation, you can also view it from the logs dataset side. Navigate to the Discover Logs page, select the correlated logs dataset, and choose the **Correlations** tab to see the linked traces dataset.

![Correlated traces tab showing Trace-to-logs correlation type linking Trace Dataset to Logs Dataset.](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/datasets/correlations-logs-dataset-tab.png)


## Using correlations in the Traces page
<a name="observability-correlations-use-traces"></a>

When a correlation exists, the Discover Traces page displays related logs in the span details view. Choose a span in the span table to open the details flyout, then choose the **Related logs** tab to view correlated log entries.

![Span details view showing Related logs tab with a log entry for GetCartAsync operation.](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/datasets/correlations-span-details-logs.png)


## Managing correlations
<a name="observability-correlations-manage"></a>

You can edit or remove correlations from the **Correlations** tab of either the traces or logs dataset.
+ **Editing** – Choose the correlation in the table and choose **Edit** to update the field mappings or target dataset.
+ **Removing** – Choose the correlation in the table and choose **Delete** to remove the correlation. Removing a correlation does not delete any data.