---
id: "@specs/aws/opensearchserverless/docs/serverless-scale-to-zero"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Scale to zero"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Scale to zero

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/serverless-scale-to-zero
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Scale to zero for Amazon OpenSearch Serverless
<a name="serverless-scale-to-zero"></a>

**Note**  
Scale to zero is only available for NextGen collections that are part of a collection group. For more information, see [Amazon OpenSearch Serverless collection groups](serverless-collection-groups.md).

Scale to zero automatically shuts down compute resources when all collections in a collection group are idle. This eliminates charges for unused capacity. When no collection in the group has incoming requests for 10 minutes, search and indexing workers scale down to zero OCU and billing stops. When traffic resumes to any collection in the group, workers are automatically provisioned and autoscaling resumes based on your request pattern.

This is ideal for development environments, batch processing workloads, and applications with predictable idle periods.

## Scale to zero behavior
<a name="serverless-scale-to-zero-behavior"></a>

The following describes how scale to zero works for your collections:
+ NextGen collection groups default to a minimum OCU of 0 for both indexing and search unless otherwise specified.
+ After 10 minutes of no incoming requests across all collections in the group, compute resources scale to zero OCU. This idle period is not configurable.
+ Search and indexing scale to zero and wake independently. Each component remains at zero until it receives its own traffic.
+ When traffic resumes, OpenSearch Serverless provisions workers at the same tier as before scale-to-zero:
  + Search requests — two search workers
  + Indexing requests — one indexing worker
+ Expect 10–30 seconds of latency on the first request to each component while capacity is restored.

## Enabling scale to zero
<a name="serverless-scale-to-zero-enable"></a>

To enable scale to zero, create a collection group with a minimum OCU of 0 for both indexing and search, then create a collection within that group.

**Enabling scale to zero**

1. Create a collection group with zero minimum OCU:

   ```
   aws opensearchserverless create-collection-group \
       --name {{collection-group-name}} \
       --standby-replicas ENABLED \
       --generation NEXTGEN \
       --capacity-limits '{
           "maxIndexingCapacityInOCU": 8,
           "maxSearchCapacityInOCU": 8,
           "minIndexingCapacityInOCU": 0,
           "minSearchCapacityInOCU": 0
       }'
   ```

1. Create a collection in the group:

   ```
   aws opensearchserverless create-collection \
       --name {{collection-name}} \
       --type {{collection-type}} \
       --collection-group-name {{collection-group-name}} \
       --standby-replicas ENABLED
   ```

## Opting out of scale to zero
<a name="serverless-scale-to-zero-disable"></a>

If you don't want your collection capacities to scale to zero, make sure they are part of a collection group with minimum capacity set to a non-zero value.