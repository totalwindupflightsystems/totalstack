---
id: "@specs/aws/opensearchserverless/docs/insights-catalog"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Insights Catalog"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Insights Catalog

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/insights-catalog
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Insights Catalog
<a name="insights-catalog"></a>

Cluster Insights delivers the following actionable insights on impacted Clusters


| Insights | Description | 
| --- | --- | 
| Low Disk |  A High severity insight is generated when the cluster’s FreeStorage drops below 25% of total capacity or 25GB, whichever threshold is reached first.  | 
| Cluster Write Blocked |  A Critical severity insight is generated when the cluster’s FreeStorage drops below 20% of total capacity or 20GB, whichever threshold is reached first.  | 
| Large Shard |  An insight with Low severity is generated when the shard size is between 50GB and 100GB. The severity escalates to Medium when the shard size is between 100GB and 200GB, and further escalates to High when the shard size exceeds 200GB.  | 
| Shard Count |  A High severity insight is generated when the cluster exceeds 25 shards per GB of configured Heap, or when the number of shards per node reaches or exceeds 900. For OpenSearch version 2.17 and above, this insight will be generated based on cluster manager configuration as detailed in this [documentation](managedomains-dedicatedmasternodes.md#dedicatedmasternodes-instance).  | 
| Cluster Status Red |  A Critical severity insight is generated when the replacement of a degraded node on the OpenSearch cluster results in a Red cluster status. This requires immediate action to restore the cluster to a Green state.  | 
| Cluster Status Yellow |  A Medium severity insight is generated when the replacement of a degraded node on the OpenSearch cluster results in a Yellow cluster status.  | 
| Misconfigured Replica |  A Medium severity insight is generated when the cluster has no replicas configured, or when the number of replicas exceeds the total number of data nodes.  | 
| KMS Key Inaccessible |  A Critical severity insight is generated when the OpenSearch cluster loses access to the KMS key used for encryption at rest. This prevents the cluster from accessing encrypted data and impacts cluster operations, requiring immediate action to restore access.  | 
| Misconfigured Index Settings |  A Medium severity insight is generated when the index setting "index.routing.allocation.require/include/exclude.<attribute>" exists on any index in the OpenSearch cluster. This setting can prevent successful blue-green deployments during cluster updates.  | 
| Incorrect Cluster Manager Configuration |  A Critical severity insight is generated when the OpenSearch cluster has either 2 data nodes without dedicated cluster manager nodes, or 2 dedicated cluster manager nodes. These configurations create a risk of quorum loss and cluster instability.  | 
| Suboptimal Sharding Strategy |  (a) A medium-severity insight is generated indicating that one or more indices have shard counts less than 80% of your data nodes. This can result in suboptimal workload distribution across the cluster. <br /> (b) A medium-severity insight is generated indicating that one or more indices have shards with 20% more data than the average shard size per node. This can result in suboptimal workload distribution across the cluster.  | 
| Cluster Overload |  (a) A high-severity insight for cluster overload indicates that more than 70% of the data nodes in the cluster are experiencing elevated utilization in CPU, memory, disk I/O, disk throughput, or disk utilization. This indicates the cluster may be approaching capacity limits. <br /> (b) A critical-severity insight indicates that more than 70% of the data nodes are experiencing high resource utilization in CPU, memory, disk I/O, disk throughput, or disk utilization, and request throttling or rejections are observed. This requires immediate action to scale the cluster.  | 
| Unused Indices |  This insight is triggered when one or more indices in an OpenSearch cluster have had zero search and indexing activity over the past 30 days. Unused indices consume storage, increase shard count, and add unnecessary cluster overhead. The insight surfaces the affected index names, displays the total count of unused indices relative to the domain's overall index count, and shows their combined storage footprint. Actionable recommendations are provided to help customers reclaim resources and reduce costs.  | 