---
id: "@specs/aws/opensearchserverless/docs/direct-query-managing-data-sources"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Managing a data source"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Managing a data source

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/direct-query-managing-data-sources
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Managing a data source in Amazon OpenSearch Service
<a name="direct-query-managing-data-sources"></a>

Managing your data source is an important part of maintaining the reliability, availability, and performance of direct query data sources and your other AWS solutions. AWS provides the following tools to monitor, report when something is wrong, and take automatic actions when appropriate.

**Topics**
+ [Monitoring with CloudWatch metrics data sources](#monitoring-cloudwatch-metrics)
+ [Enabling and disabling data sources](#direct-query-s3-enabling-disabling-data)
+ [Monitoring with AWS Budget](#direct-query-s3-enabling-budget)
+ [Deleting a data source](#direct-query-s3-delete)

## Monitoring with CloudWatch metrics data sources
<a name="monitoring-cloudwatch-metrics"></a>

You can monitor direct query using CloudWatch. CloudWatch collects raw data and processes it into readable, near real-time metrics. These statistics are kept for 15 months, so that you can access historical information and gain a better perspective on how your web application or service is performing.

You can also set alarms to monitor certain thresholds, and send notifications or take actions when those thresholds are met. For more information, see [What is Amazon CloudWatch.](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)

Amazon S3 reports the following metrics:


| Metric | Description | 
| --- | --- | 
| AsyncQueryCreateAPI | The total number of requests made to the API for creating asynchronous queries.<br />**Relevant statistics**: Average, Maximum, Sum<br />**Dimensions**: `ClientId`,`DomainName`<br />**Frequency**: 60 seconds | 
| AsyncQueryGetApiRequestCount | The total number of requests made to the API for retrieving asynchronous query results.<br />**Relevant statistics**: Average, Maximum, Sum<br />**Dimensions**: `ClientId`, `DomainName`<br />**Frequency**: 60 seconds | 
| AsyncQueryCancelApiRequestCount | The total number of requests made to the API for canceling asynchronous queries.<br />**Relevant statistics**: Average, Maximum, Sum<br />**Dimensions**: `ClientId`, `DomainName`<br />**Frequency**: 60 seconds | 
| AsyncQueryGetApiFailedRequestCusErrCount | The number of failed requests when retrieving asynchronous query results due to customer-related errors (e.g., invalid query ID).<br />**Relevant statistics**: Average, Maximum, Sum<br />**Dimensions**: `ClientId`, `DomainName`<br />**Frequency**: 60 seconds | 
| AsyncQueryCancelApiFailedRequestCusErrCount | The number of failed requests when retrieving asynchronous query results due to customer-related errors (e.g., invalid query ID).<br />**Relevant statistics**: Average, Maximum, Sum<br />**Dimensions**: `ClientId`,`DomainName`<br />**Frequency**: 60 seconds | 
| AsyncQueryCancelApiFailedRequestSysErrCount | The number of failed requests when creating asynchronous queries due to customer-related errors.<br />**Relevant statistics**: Average, Maximum, Sum<br />**Dimensions**: `ClientId`, `DomainName`<br />**Frequency**: 60 seconds | 
| AsyncQueryGetApiFailedRequestSysErrCount | The number of failed requests when retrieving asynchronous query results due to system-related errors.<br />**Relevant statistics**: Average, Maximum, Sum<br />**Dimensions**: `ClientId`, `DomainName`<br />**Frequency**: 60 seconds | 

CloudWatch Logs and Security Lake report the following metrics:


| Metric | Description | 
| --- | --- | 
| DirectQueryRate | The rate of requests made against the data sources.<br />**Relevant statistics**: Sum, Maximum, Minimum, Average<br />**Dimensions**: `DataSourceName`<br />**Frequency**: 60 seconds | 
| DirectQueryLatency | The latency observed for running queries on the data sources.<br />**Relevant statistics**: Average, P90, P99, Sum, Minimum, Maximum<br />**Dimensions**: `DataSourceName`<br />**Frequency**: 60 seconds | 
| FailedDirectQueries | The total number of query failures that are observed on the data source queries.<br />**Relevant statistics**: Sum, Maximum, Minimum, Average<br />**Dimensions**: `DataSourceName`<br />**Frequency**: 60 seconds | 
| DirectQueryConsumedOCU | The number of OCUs that are consumed for running the queries on the data sources.<br />**Relevant statistics**: Average, P90, P99, Sum, Minimum, Maximum<br />**Dimensions**: `DataSourceName`<br />**Frequency**: 60 seconds | 

## Enabling and disabling data sources
<a name="direct-query-s3-enabling-disabling-data"></a>

**Note**  
The following information is only applicable to Amazon S3 data sources.

For circumstances when you want to halt direct query usage for a data source, you can opt to disable the data source. Disabling a data source will finish executing existing queries and halt all new queries from being executed.

Accelerations setup to boost query performance such as skipping indexes, materialized views, covering indexes will be set to manual once a data source is disabled. Once a data source is set to active after being disabled, user queries will run as expected. Accelerations which were previously setup and set to manual, will need to be manually configured to run on a schedule again.

## Monitoring with AWS Budget
<a name="direct-query-s3-enabling-budget"></a>

Amazon OpenSearch Service is populating OCU usage data at the account level into Billing and Cost Management's Cost Explorer. You can account for OCU usage at the account level and set thresholds and alerts when thresholds have been crossed. 

The format of the usage type to filter on in Cost Explorer looks like RegionCode-DirectQueryOCU (OCU-hours). If you want to be notified when DirectQueryOCU (OCU-Hours) usage meets your threshold, you can create an AWS Budgets account and configure an alert based on the threshold you set. Optionally for Amazon S3, you can set up an Amazon SNS topic, which will turn off a data source in the event a threshold criteria is met. 

**Note**  
Usage data in AWS Budgets is not real-time and may be delayed up to 8 hours.

## Deleting a data source
<a name="direct-query-s3-delete"></a>

When you delete a data source, Amazon OpenSearch Service removes it from your domain or your collection. OpenSearch Service also removes indexes associated with the data source. Your transactional data isn't deleted from the other AWS service, but the other AWS service doesn't send new data to OpenSearch Service.

You can delete a data source integration using the AWS Management Console or the OpenSearch Service API.

### AWS Management Console
<a name="direct-query-s3-console-delete"></a>

**To delete an Amazon S3 data source**

1. Navigate to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/](https://console.aws.amazon.com/aos/).

1. From the left navigation pane, choose **Domains**. 

1. Select the domain that you want to delete a data source for. This opens the domain details page. Choose the **Connections** tab below the general information and find the **Direct query** section.

1. Select the data source you want to delete, choose **Delete**, and confirm deletion. 

**To delete a CloudWatch Logs or Security Lake data source**

1. Navigate to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/](https://console.aws.amazon.com/aos/).

1. From the left navigation pane, choose **Central management**, then **Connected data sources**. 

1. Select the data source you want to delete, choose **Delete**, and confirm deletion. 

### OpenSearch Service API
<a name="creating-direct-query-s3-api-delete"></a>

To delete an Amazon S3 data source, use the [DeleteDataSource](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DeleteDataSource.html) API operation.

```
POST https://es.{{region}}.amazonaws.com/2021-01-01/opensearch/domain/{{domain-name}}/dataSource/{{data-source-name}}
```

To delete a CloudWatch Logs or Security Lake data source, use the [DeleteDirectQueryDataSource](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DeleteDirectQueryDataSource.html) API operation.