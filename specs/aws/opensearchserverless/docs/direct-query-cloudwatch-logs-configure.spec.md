---
id: "@specs/aws/opensearchserverless/docs/direct-query-cloudwatch-logs-configure"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Configuring a CloudWatch Logs data source"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Configuring a CloudWatch Logs data source

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/direct-query-cloudwatch-logs-configure
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Configuring and querying a CloudWatch Logs data source in OpenSearch Dashboards
<a name="direct-query-cloudwatch-logs-configure"></a>

Now that you've created your data source, you can get started with it OpenSearch Dashboards. This section walks you through various use cases with your data source in OpenSearch Dashboards.

## Query log groups from the Discover page
<a name="direct-query-cloudwatch-logs-query-from-discover"></a>

In the OpenSearch Discover page, you can use the new direct query data source you configured to query your CloudWatch Logs log groups. To do this, choose **Explore logs**, then use the search bar to build your query using SQL or PPL. You can filter, sort, and visualize the data returned from your log groups. To understand what statements, commands, and limitations are supported for the CloudWatch Logs integration, see [Supported SQL and PPL commands](direct-query-supported-commands.md).

## Create a dashboard view for your data source
<a name="direct-query-cloudwatch-logs-setup-integration"></a>

When you use OpenSearch Service, you can quickly analyze popular AWS log types using pre-built dashboard templates. For CloudWatch Logs there are templates for VPC, CloudTrail, AWS WAF, and Network Firewall logs. These templates allow you to quickly create a dashboard tailored to your specific data. They include dashboards tailored for that specific log type. This enables you to quickly get up and running with analyzing these popular AWS log sources, without having to build everything from scratch.

**Note**  
Dashboards use indexed views, which ingest data from CloudWatch Logs using direct query OpenSearch Compute Units (OCUs) as well as serverless collection indexingOCUs, searchingOCUs, and storage.

Follow these steps to create a dashboard using one of these pre-built templates, so you can start exploring and analyzing your data right away.

**To create a dashboard view**

1. Navigate to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/](https://console.aws.amazon.com/aos/).

1. From the left navigation pane, choose **Central management**, then **Connected data sources**. 

1. Select the data source to open the details page. 

1. Choose **Create dashboard**.

1. Choose which type of dashboard you want to create.

1. Enter a name for your dashboard.

1. Enter an optional description for your dashboard.

1. Select one or more log groups to view on your dashboard.

1. Choose how often you want to refresh the data in your dashboard.

1. Choose which OpenSearch workspace you want to use. 

   1. To create a new workspace, select **Create new workspace** and enter a name.

   1. To use an existing workspace, select **Select existing workspace**.

1. Choose **Create dashboard**.

## Querying CloudWatch Logs data in OpenSearch Discover
<a name="direct-querying-cloudwatch-logs-query"></a>

To query your data, select your data source from the drop-down menu. If you're using CloudWatch Logs, navigate to Discover from your Essentials workspace and start querying data using OpenSearch SQL or Piped Processing Language (PPL). For a list of supported commands, see [Supported SQL and PPL commands](direct-query-supported-commands.md).

**Note**  
If you’ve created a materialized view, you can use DQL to query your data given that you’ve indexed it within.

### Troubleshooting
<a name="cloudwatch-logs-troubleshooting"></a>

There might be instances when results don’t return as expected. If you experience any issues, make sure that you're following the [Recommendations](direct-query-cloudwatch-logs-overview.md#direct-query-cloudwatch-logs-recommendations).