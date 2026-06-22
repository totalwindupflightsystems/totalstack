---
id: "@specs/aws/opensearchserverless/docs/direct-query-security-lake-configure"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Configuring a Security Lake data source"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Configuring a Security Lake data source

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/direct-query-security-lake-configure
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Configuring and querying a Security Lake data source in OpenSearch Dashboards
<a name="direct-query-security-lake-configure"></a>

Now that you've created your data source, you can set it up in OpenSearch Dashboards. 

**Note**  
DirectQuery in Discover is only supported when logging into the OpenSearch UI application with IAM authentication. IAM Identity Center (IAM Identity Center) is not supported for DirectQuery. Since DirectQuery Security Lake can only be used from Discover, customers using IAM Identity Center cannot use DirectQuery Security Lake.

This section walks you through various use cases with your data source in OpenSearch Dashboards before you query your data. To get started, you need to navigate to your data source in OpenSearch Dashboards. In the left-hand menu, under **Management**, choose **Data sources**. Then, select the name of the data source that you created earlier in the OpenSearch Service console.

## Query Security Lake tables from Discover
<a name="direct-query-security-lake-query-from-discover"></a>

If you have created tables based on your Security Lake logs, you can now query those tables directly from OpenSearch Discover. This enables you to seamlessly access and analyze data stored in Security Lake, directly from the familiar Discover interface. By querying Security Lake directly from Discover, you can avoid the need to manually extract, transform, and load the data into a separate search index. To quickly get started analyzing your logs, Discover includes a set of PPL and SQL saved queries.

Start by selecting the data source that you configured. Select the associated database and table you want to query, then use the search bar to write queries against your tables. To understand what statements, commands, and limitations are supported for the Security Lake integration, see [Supported SQL and PPL commands](direct-query-supported-commands.md). 

To take advantage of the pre-built queries that are available for Security Lake, go to **...** on the top right hand side of Discover, choose **Open Query** and then choose **Templates**. There are many pre-built queries available for log sources supported in Security Lake. Search for the templates that match your use case, copy the query to use in the search bar, and replace templated fields (such as Region and action) with your own information.

## Accelerate data from Discover
<a name="accelerate-security-lake-data-from-discover"></a>

To enhance performance and enable faster subsequent queries and analysis in OpenSearch, you can ingest the results of your query from Discover into an OpenSearch indexed view. 

**To create an indexed view**

1. From Discover, choose **Create Indexed View**. 

1. In the query editor, enter your desired query. You can create a new query here or use an existing one from your previous searches.

1. Specify a name for your new indexed view. Choose a descriptive name that will help you identify the view later.

1. Configure the data retention settings for your indexed view. You can specify how long the data should be kept in the index, allowing you to balance performance with storage costs.

1. Create the indexed view. After it's created, your indexed view will be available for faster querying and analysis.

If you've previously created indexed views, you can access them from Discover.

**To use an existing index view**

1. From Discover, choose **Select Indexed View** to see a list of your existing indexed views for Security Lake.

1. Choose the indexed view you want to use. This will apply the view to your current query, potentially significantly speeding up your data retrieval and analysis.

## Create a dashboard view for your data source
<a name="direct-query-security-lake-create-dashboard"></a>

When you use OpenSearch Service, you can analyze popular AWS log types using pre-built dashboard templates. For Security Lake there are templates for VPC, CloudTrail, and WAF logs. These templates allow you to create a dashboard tailored to your specific data. They include pre-built queries and dashboards tailored for that specific log type. This enables you to quickly get up and running with analyzing these popular AWS log sources, without having to build everything from scratch.

**Note**  
Dashboards use indexed views, which ingest data from Security Lake and contribute to direct query and collection compute.

Follow these steps to create a dashboard using one of these pre-built templates, so you can start exploring and analyzing your data right away.

**To create a dashboard view**

1. Navigate to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/](https://console.aws.amazon.com/aos/).

1. From the left navigation pane, choose **Central management**, then **Connected data sources**. 

1. Select the data source to open the details page. 

1. Choose **Create dashboard**.

1. Choose which type of dashboard you want to create.

1. Enter a name for your dashboard.

1. Enter an optional description for your dashboard.

1. Select one or more AWS Glue tables to view on your dashboard.

1. Choose how often you want to refresh the data in your dashboard.

1. Choose which OpenSearch workspace you want to use. 

   1. To create a new workspace, select **Create new workspace**.

   1. To use an existing workspace, select **Select existing workspace**.

1. Enter a name for your workspace.

1. Choose **Create dashboard**.

## Troubleshooting
<a name="security-lake-troubleshooting"></a>

There might be instances when results don’t return as expected. If you experience any issues, make sure that you're following the [Recommendations](direct-query-security-lake-overview.md#direct-query-security-lake-recommendations).