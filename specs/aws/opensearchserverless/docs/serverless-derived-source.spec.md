---
id: "@specs/aws/opensearchserverless/docs/serverless-derived-source"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Save Storage by Using Derived Source"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Save Storage by Using Derived Source

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/serverless-derived-source
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Save Storage by Using Derived Source
<a name="serverless-derived-source"></a>

By default, OpenSearch Serverless stores each ingested document in the `_source` field, which contains the original JSON document body, and indexes individual fields for search. While the `_source` field is not searchable, it is retained so that the full document can be returned when executing fetch requests, such as get and search. When derived source is enabled, OpenSearch Serverless skips storing the `_source` field and instead reconstructs it dynamically on demand — for example, during search, get, mget, reindex, or update operations. Using the derived source setting can reduce storage usage by up to 50%.

## Configuration
<a name="serverless-derived-source-config"></a>

To configure derived source for your index, create the index using the `index.derived_source.enabled` setting:

```
PUT my-index1
{
  "settings": {
    "index": {
      "derived_source": {
        "enabled": true
      }
    }
  }
}
```

## Important considerations
<a name="serverless-derived-source-considerations"></a>
+ Only certain field types are supported. For a list of supported fields and limitations, refer to the [OpenSearch documentation](https://docs.opensearch.org/latest/mappings/metadata-fields/source/#supported-fields-and-parameters). If you create an index with derived source and an unsupported field, index creation will fail. If you attempt to ingest a document with an unsupported field in a derived source-enabled index, ingestion will fail. Use this feature only when you are aware of the field types that will be added to your index.
+ The setting `index.derived_source.enabled` is a static setting. This cannot be changed after the index is created.

## Limitations on query responses
<a name="serverless-derived-source-limitations"></a>

When derived source is enabled, it imposes certain limitations on how query responses are generated and returned.
+ Date fields with multiple formats specified always use the first format in the list for all requested documents, regardless of the original ingested format.
+ Geopoint values are returned in a fixed `{"lat": lat_val, "lon": lon_val}` format and may lose some precision.
+ Multi-value arrays may be sorted, and keyword fields may be deduplicated.

For more details, refer to the [OpenSearch blog](https://opensearch.org/blog/save-up-to-2x-on-storage-with-derived-source/).

## Performance benchmarking
<a name="serverless-derived-source-performance"></a>

Based on benchmark testing with the nyc\_taxi dataset, derived source achieved 58% reduction in index size compared to baseline.


| Metric | Derived Source | 
| --- | --- | 
| Index Size Reduction | 58.3% | 
| Indexing Throughput Change | 3.7% | 
| Indexing p90 Latency Change | 6.9% | 
| Match-all Query p90 Latency Improvement | 19% | 
| Range Query p90 Latency Improvement | -18.8% | 
| Distance Amount p90 Agg Latency Improvement | -7.3% | 

For more details, refer to the [OpenSearch blog](https://opensearch.org/blog/save-up-to-2x-on-storage-with-derived-source/).