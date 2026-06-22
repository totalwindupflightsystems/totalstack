---
id: "@specs/aws/opensearchserverless/docs/observability-datasets"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Datasets"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Datasets

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/observability-datasets
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Datasets
<a name="observability-datasets"></a>

Datasets are collections of indexes that represent a logical grouping of your observability data. You use datasets to organize logs and traces data so that you can query and analyze related indexes together in the Discover experience. Each dataset maps to one or more indexes in your OpenSearch Service domain and defines the data type, time field, and query language for the Discover page.

## Dataset types
<a name="observability-datasets-types"></a>

The following table describes the dataset types that you can create.


| Type | Description | Query language | 
| --- | --- | --- | 
| Logs | Groups one or more log indexes for querying and visualization in the Discover Logs page. | PPL | 
| Traces | Groups trace span indexes for querying and visualization in the Discover Traces page. | PPL | 

**Note**  
Metrics do not require a dataset because metric data is not stored in OpenSearch. Metrics are queried directly from Amazon Managed Service for Prometheus using PromQL.

## To create a logs dataset
<a name="observability-datasets-create-logs"></a>

Complete the following steps to create a logs dataset in OpenSearch UI.

1. In your observability workspace, expand **Discover** in the left navigation and choose **Logs**.

1. Choose **Create dataset**.

1. Select a data source from the list of available OpenSearch Service connections.  
![Data source selection dialog showing OpenSearch 3.4 with logs-otel-v1 wildcard pattern and one matching index.](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/datasets/datasets-select-data-source.png)

1. Configure the dataset by entering a name, selecting the index, and specifying the timestamp field.  
![Dataset configuration dialog showing fields for dataset name, language, time field, and OTel logs schema mappings including trace ID, span ID, service name, and timestamp.](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/datasets/datasets-configure-logs.png)

1. Choose **Create dataset** to save the configuration.

## To create a traces dataset
<a name="observability-datasets-create-traces"></a>

Complete the following steps to create a traces dataset in OpenSearch UI.

1. In your observability workspace, expand **Discover** in the left navigation and choose **Traces**.

1. Choose **Create dataset**.

1. Select a data source from the list of available OpenSearch Service connections.

1. Configure the dataset by entering a name, selecting the span index, and specifying the timestamp field.  
![Configure Dataset dialog with fields for dataset name, description, data source, language, and time field.](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/datasets/datasets-configure-traces.png)

1. Choose **Create dataset** to save the configuration.

## To view datasets
<a name="observability-datasets-view"></a>

You can view all configured datasets from the dataset selector on the Discover Logs or Discover Traces page. The dataset list shows the name, type, data source, and timestamp field for each dataset.

![Workspace datasets table showing Logs Dataset and Trace Dataset with their types and data sources.](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/datasets/datasets-list.png)


## Analyzing datasets in Discover
<a name="observability-datasets-analyze"></a>

After you create a dataset, you can analyze it in the corresponding Discover page.

### Logs
<a name="observability-datasets-analyze-logs"></a>

Select a logs dataset from the dataset selector on the Discover Logs page to query and visualize your log data using PPL. For more information, see [Discover Logs](observability-analyze-logs.md).

### Traces
<a name="observability-datasets-analyze-traces"></a>

Select a traces dataset from the dataset selector on the Discover Traces page to explore trace spans, view RED metrics, and drill into individual traces. For more information, see [Discover Traces](observability-analyze-traces.md).