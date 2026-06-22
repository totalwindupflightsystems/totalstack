---
id: "@specs/aws/opensearchserverless/docs/direct-query-s3-configure"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Configuring an S3 data source"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Configuring an S3 data source

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/direct-query-s3-configure
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Configuring and querying an S3 data source in OpenSearch Dashboards
<a name="direct-query-s3-configure"></a>

Now that you've created your data source, you can configure security settings, define your Amazon S3 tables, or set up accelerated data indexing. This section walks you through various use cases with your data source in OpenSearch Dashboards before you query your data.

To configure the following sections, you must first navigate to your data source in OpenSearch Dashboards. In the left-hand navigation, under **Management**, choose **Data sources**. Under **Manage data sources**, select the name of the data source that you created in the console. 

## Create Spark Tables using Query Workbench
<a name="direct-query-s3-configure-tables"></a>

Direct queries from OpenSearch Service to Amazon S3 use Spark tables within the AWS Glue Data Catalog. You can create tables from within the Query Workbench without having to leave OpenSearch Dashboards. 

To manage existing databases and tables in your data source, or to create new tables that you want to use direct queries on, choose **Query Workbench** from the left navigation and select the Amazon S3 data source from the data source drop down.

To set up a table for VPC Flow logs stored in S3 in Parquet format, run the following query: 

```
CREATE TABLE 
{{datasourcename.gluedatabasename.vpclogstable}} (version INT, account_id STRING, interface_id STRING, 
srcaddr STRING, dstaddr STRING, srcport INT, dstport INT, protocol INT, packets BIGINT, 
bytes BIGINT, start BIGINT, end BIGINT, action STRING, log_status STRING, 
`aws-account-id` STRING, `aws-service` STRING, `aws-region` STRING, year STRING, 
month STRING, day STRING, hour STRING) 

USING parquet PARTITIONED BY (aws-account-id, aws-service, aws-region, year, month, 
day, hour) 

LOCATION "s3://{{accountnum-vpcflow}}/AWSLogs"
```

After creating the table, run the following query to ensure that it's compatible with direct queries:

```
MSCK REPAIR TABLE {{ datasourcename.databasename.vpclogstable}}
```

## Setup integrations for popular AWS log types
<a name="direct-query-s3-setup-integration"></a>

You can integrate AWS log types stored in Amazon S3 with OpenSearch Service. Use OpenSearch Dashboards to install integrations that create AWS Glue Data Catalog tables, saved queries, and dashboards. These integrations use indexed views to keep dashboards updated.

For instructions to install an integration, see [Installing an integration asset](https://opensearch.org/docs/latest/integrations/#installing-an-integration-asset) in the OpenSearch documentation.

When you select an integration, make sure it has the `S3 Glue` tag. 

When you set up the integration, specify **S3 Connection** for the connection type. Then, select the data source for the integration, the Amazon S3 location of the data, the checkpoint to manage acceleration indexing, and the assets required for your use case.

**Note**  
Make sure the S3 bucket for your checkpoint has write permissions for the checkpoint location. Without these permissions, the integration's accelerations will fail.

## Set up access control
<a name="direct-query-s3-configure-ac"></a>

On the details page for your data source, find the **Access controls** section and choose **Edit**. If the domain has fine-grained access control enabled, choose **Restricted** and select which roles you want to provide with access to the new data source. You can also choose **Admin only** if you only want the administrator to have access to the data source.

**Important**  
Indexes are used for any queries against the data source. A user with read access to the request index for a given data source can read *all* queries against that data source. A user with read access to the result index can read results for *all* queries against that data source.

## Querying S3 data in OpenSearch Discover
<a name="direct-querying-s3-query"></a>

After you set up your tables and configure your desired optional query acceleration, you can start analyzing your data. To query your data, select your data source from the drop-down menu. If you're using Amazon S3 and OpenSearch Dashboards, go to Discover and select the data source name. 

If you're using a skipping index or haven't created an index, you can use SQL or PPL to query your data. If you've configured a materialized view or a covering index, you already have an index and can use Dashboards Query Language (DQL) throughout Dashboards. You can also use PPL with the Observability plugin, and SQL with the Query Workbench plugin. Currently, only the Observability and Query Workbench plugins support PPL and SQL. For querying data using the OpenSearch Service API, refer to the [async API documentation](https://github.com/opensearch-project/sql/blob/main/docs/user/interfaces/asyncqueryinterface.rst).

**Note**  
Not all SQL and PPL statements, commands and functions are supported. For a list of supported commands, see [Supported SQL and PPL commands](direct-query-supported-commands.md).  
If you’ve created a materialized view or covering index, you can use DQL to query your data given that you’ve indexed it within.

## Troubleshooting
<a name="s3-troubleshooting"></a>

There might be instances when results don’t return as expected. If you experience any issues, make sure that you're following the [Recommendations](direct-query-s3-overview.md#direct-query-s3-recommendations).