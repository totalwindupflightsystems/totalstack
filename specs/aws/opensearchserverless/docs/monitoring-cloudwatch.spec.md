---
id: "@specs/aws/opensearchserverless/docs/monitoring-cloudwatch"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Monitoring with CloudWatch"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Monitoring with CloudWatch

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/monitoring-cloudwatch
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Monitoring OpenSearch Serverless with Amazon CloudWatch
<a name="monitoring-cloudwatch"></a>

You can monitor Amazon OpenSearch Serverless using CloudWatch, which collects raw data and processes it into readable, near real-time metrics. These statistics are kept for 15 months, so that you can access historical information and gain a better perspective on how your web application or service is performing. 

You can also set alarms that watch for certain thresholds, and send notifications or take actions when those thresholds are met. For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).

OpenSearch Serverless reports the following metrics in the `AWS/AOSS` namespace.


| Metric | Description | 
| --- | --- | 
| ActiveCollection | Indicates whether a collection is active. A value of 1 means that the collection is in an `ACTIVE` state. This value is emitted upon successful creation of a collection and remains 1 until you delete the collection. The metric can't have a value of 0.<br />**Relevant statistics**: Max<br />**Dimensions**: `ClientId`, `CollectionId`, `CollectionName`<br />**Frequency**: 60 seconds | 
| DeletedDocuments | The total number of deleted documents.<br />**Relevant statistics**: Average, Sum<br />**Dimensions**: `ClientId`, `CollectionId`, `CollectionName`, `IndexId`, `IndexName`<br />**Frequency**: 60 seconds | 
| IndexingOCU | The number of OpenSearch Compute Units (OCUs) used to ingest collection data. This metric applies at the account level. Represents usage only for collections that are not part of any collection group.<br />**Relevant statistics**: Sum<br />**Dimensions**: `ClientId`<br />**Frequency**: 60 seconds | 
| IndexingOCU | The number of OpenSearch Compute Units (OCUs) used to ingest collection data. This metric applies at the collection group level.<br />**Relevant statistics**: Sum<br />**Dimensions**: `ClientId`, `CollectionGroupId`, `CollectionGroupName`<br />**Frequency**: 60 seconds | 
| IngestionDataRate | The indexing rate in GiB per second to a collection or index. This metric only applies to bulk indexing requests.<br />**Relevant statistics**: Sum<br />**Dimensions**: `ClientId`, `CollectionId`, `CollectionName`, `IndexId`, `IndexName`<br />**Frequency**: 60 seconds | 
| IngestionDocumentErrors | The total number of document errors during ingestion for a collection or index. After a successful bulk indexing request, writers process the request and emit errors for all failed documents within the request.<br />**Relevant statistics**: Sum<br />**Dimensions**: `ClientId`, `CollectionId`, `CollectionName`, `IndexId`, `IndexName`<br />**Frequency**: 60 seconds | 
| IngestionDocumentRate | The rate per second at which documents are being ingested to a collection or index. This metric only applies to bulk indexing requests.<br />**Relevant statistics**: Sum<br />**Dimensions**: `ClientId`, `CollectionId`, `CollectionName`, `IndexId`, `IndexName`<br />**Frequency**: 60 seconds | 
| IngestionRequestErrors | The total number of bulk indexing request errors to a collection. OpenSearch Serverless emits this metric when a bulk indexing request fails for any reason, such as an authentication or availability issue.<br />**Relevant statistics**: Sum<br />**Dimensions**: `ClientId`, `CollectionId`, `CollectionName`<br />**Frequency**: 60 seconds | 
| IngestionRequestLatency | The latency, in seconds, for bulk write operations to a collection.<br />**Relevant statistics**: Minimum, Maximum, Average<br />**Dimensions**: `ClientId`, `CollectionId`, `CollectionName`<br />**Frequency**: 60 seconds | 
| IngestionRequestRate | The total number of bulk write operations received by a collection.<br />**Relevant statistics**: Minimum, Maximum, Average<br />**Dimensions**: `ClientId`, `CollectionId`, `CollectionName`<br />**Frequency**: 60 seconds | 
| IngestionRequestSuccess | The total number of successful indexing operations to a collection.<br />**Relevant statistics**: Sum<br />**Dimensions**: `ClientId`, `CollectionId`, `CollectionName`<br />**Frequency**: 60 seconds | 
| SearchableDocuments | The total number of searchable documents in a collection or index.<br />**Relevant statistics**: Sum<br />**Dimensions**: `ClientId`, `CollectionId`, `CollectionName`, `IndexId`, `IndexName`<br />**Frequency**: 60 seconds | 
| SearchRequestErrors | The total number of query errors per minute for a collection.<br />**Relevant statistics**: Sum<br />**Dimensions**: `ClientId`, `CollectionId`, `CollectionName`<br />**Frequency**: 60 seconds | 
| SearchRequestLatency | The average time, in milliseconds, that it takes to complete a search operation against a collection.<br />**Relevant statistics**: Minimum, Maximum, Average<br />**Dimensions**: `ClientId`, `CollectionId`, `CollectionName`<br />**Frequency**: 60 seconds | 
| SearchOCU | The number of OpenSearch Compute Units (OCUs) used to search collection data. This metric applies at the account level. Represents usage only for collections that are not part of any collection group.<br />**Relevant statistics**: Sum<br />**Dimensions**: `ClientId`<br />**Frequency**: 60 seconds | 
| SearchOCU | The number of OpenSearch Compute Units (OCUs) used to search collection data. This metric applies at the collection group level.<br />**Relevant statistics**: Sum<br />**Dimensions**: `ClientId`, `CollectionGroupId`, `CollectionGroupName`<br />**Frequency**: 60 seconds | 
| SearchRequestRate | The total number of search requests per minute to a collection.<br />**Relevant statistics**: Average, Maximum, Sum<br />**Dimensions**: `ClientId`, `CollectionId`, `CollectionName`<br />**Frequency**: 60 seconds | 
| StorageUsedInS3 | The amount, in bytes, of Amazon S3 storage used. OpenSearch Serverless stores indexed data in Amazon S3. You must select the period at one minute to get an accurate value. This value represents the total physical S3 storage consumed, which includes overhead for replication, metadata, and internal indexing structures. It may differ from the logical index size reported by `GET _cat/indices` or the Total size shown in the management console.<br />**Relevant statistics**: Sum<br />**Dimensions**: `ClientId`, `CollectionId`, `CollectionName`, `IndexId`, `IndexName`<br />**Frequency**: 60 seconds | 
| VectorIndexBuildAccelerationOCU | The number of OpenSearch Compute Units (OCUs) used to accelerate vector indexing. This metric applies at the collection level.<br />**Relevant statistics**: Sum<br />**Dimensions**: `ClientId`, `CollectionId`<br />**Frequency**: 60 seconds | 
| 2xx, 3xx, 4xx, 5xx | The number of requests to the collection that resulted in the given HTTP response code (2*xx*, 3*xx*, 4*xx*, 5*xx*).<br />**Relevant statistics**: Sum<br />**Dimensions**: `ClientId`, `CollectionId`, `CollectionName`<br />**Frequency**: 60 seconds | 