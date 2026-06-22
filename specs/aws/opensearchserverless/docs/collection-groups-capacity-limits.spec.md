---
id: "@specs/aws/opensearchserverless/docs/collection-groups-capacity-limits"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Collection group capacity limits"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Collection group capacity limits

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/collection-groups-capacity-limits
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Collection group capacity limits
<a name="collection-groups-capacity-limits"></a>

Collection groups provide granular control over resource allocation through minimum and maximum OCU limits. These limits apply to all collections within the group and operate independently from account-level capacity settings.

By default, there is a service quota (limit) for the number of collections in a collection group, the number of indexes in a collection, and the number of OCUs in a collection group. For more information, see [OpenSearch Serverless quotas](https://docs.aws.amazon.com/general/latest/gr/opensearch-service.html#opensearch-limits-serverless).

## Collection group capacity limits overview
<a name="collection-groups-capacity-overview"></a>

You can configure minimum and maximum OCU limits for both indexing and search operations at the collection group level. These limits control how OpenSearch Serverless scales resources for collections in the group:
+ **Minimum OCU** – The minimum number of OCUs that OpenSearch Serverless maintains for the collection group, ensuring consistent baseline performance.
  + If the workload requires fewer OCUs than the specified minimum value, OpenSearch Serverless still maintains the specified minimum number of OCUs, and billing reflects that minimum.
  + If the workload requires more OCUs than the specified minimum value, OpenSearch Serverless maintains the number of OCUs that the workload requires, and billing reflects the higher OCU utilization.
+ **Maximum OCU** – The maximum number of OCUs that OpenSearch Serverless can scale up to for the collection group, helping you control costs.

Collection group capacity limits operate independently from account-level limits. Account-level maximum OCU settings apply only to collections not associated with any collection group, while collection group maximum OCU settings apply to collections within that specific group.

## Valid capacity limit values
<a name="collection-groups-capacity-values"></a>

When setting minimum and maximum OCU limits for a collection group, you can only use values from the following set: 1, 2, 4, 8, 16, and multiples of 16 (such as 32, 48, 64, 80, 96) up to a maximum of 1,696 OCUs.

Both minimum and maximum OCU limits are optional when you create a collection group. If you don't specify a maximum OCU limit, OpenSearch Serverless uses a default value of 96 OCUs.

The minimum OCU limit must be less than or equal to the maximum OCU limit.

## Account-level and collection group OCU limits
<a name="collection-groups-capacity-relationship"></a>

When you plan your OpenSearch Serverless capacity, understand how account-level OCU limits and collection group OCU limits interact. The sum of the maximum OCU settings across all collection groups plus the maximum OCU setting at the account level must be less than or equal to the service quota limit per account. For current limit values, see [OpenSearch Serverless quotas](https://docs.aws.amazon.com/general/latest/gr/opensearch-service.html#opensearch-limits-serverless).

**Note**  
Account-level maximum OCU settings apply only to collections not associated with any collection group. Collections within collection groups are governed by their respective collection group limits, not the account-level limits.

This constraint applies to both indexing and search OCUs independently. For example, if you configure account-level settings and collection groups, you must ensure the total doesn't exceed the service quota limit for indexing OCUs and separately doesn't exceed the service quota limit for search OCUs. Additionally, you can create a maximum of 300 collection groups per account.

**Example: Planning capacity with account-level and collection group limits**  
If you set the account-level maximum search OCU to 500 and the service quota limit is 1,700:
+ And create 2 collection groups, the sum of the maximum OCU for the 2 collection groups must be no more than 1,200 (1,700 - 500)
+ You could leave each collection group at the default maximum OCU of 96 (96 \+ 96 \+ 500 = 692), leaving headroom for future growth
+ Or you could increase each collection group's maximum to 600 (600 \+ 600 \+ 500 = 1,700), using the full capacity allowed by the service quota

This relationship is essential for capacity planning. Before you create new collection groups or increase maximum OCU limits, verify that your total allocation doesn't exceed the service quota limit. If you reach this limit, you must either reduce the maximum OCU settings on existing collection groups or decrease your account-level maximum OCU settings to make room for new allocations.

## Configure capacity limits
<a name="collection-groups-capacity-configure"></a>

You can set capacity limits when you create a collection group or update them later. To configure capacity limits using the AWS CLI, use the [CreateCollectionGroup](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CreateCollectionGroup.html) or [UpdateCollectionGroup](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_UpdateCollectionGroup.html) commands:

```
aws opensearchserverless create-collection-group \
    --name {{my-collection-group}} \
    --capacity-limits maxIndexingCapacityInOCU={{32}},maxSearchCapacityInOCU={{32}},minIndexingCapacityInOCU={{4}},minSearchCapacityInOCU={{4}}
```

To update capacity limits for an existing collection group:

```
aws opensearchserverless update-collection-group \
    --id {{abcdef123456}} \
    --capacity-limits maxIndexingCapacityInOCU={{48}},maxSearchCapacityInOCU={{48}},minIndexingCapacityInOCU={{8}},minSearchCapacityInOCU={{8}}
```

## Monitor collection group capacity
<a name="collection-groups-capacity-monitoring"></a>

OpenSearch Serverless emits the following Amazon CloudWatch Logs metrics at one-minute intervals to help you monitor OCU utilization and capacity limits at the collection group level:
+ `IndexingOCU` – The number of indexing OCUs currently in use by the collection group.
+ `SearchOCU` – The number of search OCUs currently in use by the collection group.

OpenSearch Serverless also emits OCU metrics at the account level for collections not associated with any collection group. You can aggregate these metrics in CloudWatch to visualize the sum of OCUs across all collection groups and account-level collections.

You can configure alarms to receive notifications when your collection group approaches its capacity limits so that you can adjust settings as needed. For more information about OpenSearch Serverless metrics, see [Monitoring Amazon OpenSearch Serverless](serverless-monitoring.md).

## Capacity limit enforcement
<a name="collection-groups-capacity-enforcement"></a>

OpenSearch Serverless enforces collection group capacity limits during scaling operations. When your collections need additional resources, OpenSearch Serverless scales up to the maximum OCU limit. When demand decreases, OpenSearch Serverless scales down but maintains at least the minimum OCU limit to ensure consistent performance.

OpenSearch Serverless enforces capacity limits only when the collection group contains at least one collection. Empty collection groups do not consume OCUs or enforce capacity limits.

If a scaling operation would exceed the maximum OCU limit or violate the minimum OCU requirement, OpenSearch Serverless rejects the operation to maintain compliance with your configured limits.