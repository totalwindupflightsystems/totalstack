---
id: "@specs/aws/opensearchserverless/docs/concurrent-segment-search"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Concurrent segment search"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Concurrent segment search

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/concurrent-segment-search
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Concurrent segment search in Amazon OpenSearch Service
<a name="concurrent-segment-search"></a>

Starting with OpenSearch version 2.17, concurrent segment search uses a new setting to control concurrent search behavior.
+ New domains created with version 2.17 have default concurrent segment search set to **auto** mode by default on nodes that are 2xl or above. 
+ Existing domains upgrading to 2.17 have default concurrent segment search set to **auto** based on instance type for all nodes that are 2xl or above, and if the overall CPU utilization of the cluster is below 45% in the past 1 week.
+ For more information, see [Concurrent segment search version 2.17](https://opensearch.org/docs/2.17/search-plugins/concurrent-segment-search/). 

Starting with OpenSearch version 2.13, you can use concurrent segment search to help you search segments in parallel during the query phase. For full documentation of concurrent segment search, see [Concurrent segment search](https://opensearch.org/docs/latest/search-plugins/concurrent-segment-search/) in the open source OpenSearch documentation. For information about Amazon CloudWatch metrics related to concurrent segment search, see [Instance metrics](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-cloudwatchmetrics.html#managedomains-cloudwatchmetrics-instance-metrics) and [UltraWarm metrics](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-cloudwatchmetrics.html#managedomains-cloudwatchmetrics-uw).

There are a few additional limitations that apply when you use current segment search with Amazon OpenSearch Service:
+ By default, OpenSearch Service uses a count of 2 slices with the max slice count mechanism.