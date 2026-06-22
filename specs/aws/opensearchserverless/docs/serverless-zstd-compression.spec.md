---
id: "@specs/aws/opensearchserverless/docs/serverless-zstd-compression"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Zstandard Codec Support in Amazon OpenSearch Serverless"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Zstandard Codec Support in Amazon OpenSearch Serverless

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/serverless-zstd-compression
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Zstandard Codec Support in Amazon OpenSearch Serverless
<a name="serverless-zstd-compression"></a>

Index codecs determine how an index's stored fields are compressed and stored on disk and in S3. The index codec is controlled by the static `index.codec` setting that specifies the compression algorithm. This setting impacts both index shard size and index operation performance.

By default, indexes in OpenSearch Serverless use the default codec with the LZ4 compression algorithm. OpenSearch Serverless also supports `zstd` and `zstd_no_dict` codecs with configurable compression levels from 1 to 6.

**Important**  
Since `index.codec` is a static setting, it cannot be changed after index creation.

For more details, refer to the [OpenSearch Index Codecs documentation](https://opensearch.org/docs/latest/im-plugin/index-codecs/).

## Creating an index with ZSTD codec
<a name="serverless-zstd-create-index"></a>

You can specify the ZSTD codec during index creation using the `index.codec` setting:

```
PUT /your_index
{
  "settings": {
    "index.codec": "zstd"
  }
}
```

## Compression levels
<a name="serverless-zstd-compression-levels"></a>

ZSTD codecs support optional compression levels via the `index.codec.compression_level` setting, accepting integers in the range [1, 6]. Higher compression levels result in better compression ratios (smaller storage) but slower compression and decompression speeds. The default compression level is 3.

```
PUT /your_index
{
  "settings": {
    "index.codec": "zstd",
    "index.codec.compression_level": 2
  }
}
```

## Performance benchmarking
<a name="serverless-zstd-performance"></a>

Based on benchmark testing with the nyc\_taxi dataset, ZSTD compression achieved 26-32% better compression compared to baseline across different combinations of `zstd`, `zstd_no_dict`, and compression levels.


| Metric | ZSTD L1 | ZSTD L6 | ZSTD\_NO\_DICT L1 | ZSTD\_NO\_DICT L6 | 
| --- | --- | --- | --- | --- | 
| Index Size Reduction | 28.10% | 32% | 26.90% | 28.70% | 
| Indexing Throughput Change | -0.50% | -23.80% | -0.50% | -5.30% | 
| Match-all Query p90 Latency Improvement | -16.40% | 29.50% | -16.40% | 23.40% | 
| Range Query p90 Latency Improvement | 90.90% | 92.40% | -282.90% | 92.50% | 
| Distance Amount p90 Agg Latency Improvement | 2% | 24.70% | 2% | 13.80% | 

For more details, refer to the [AWS OpenSearch blog](https://aws.amazon.com/blogs/big-data/optimize-storage-costs-in-amazon-opensearch-service-using-zstandard-compression/).