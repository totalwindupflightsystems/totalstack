---
id: "@specs/aws/opensearchserverless/docs/knn"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS k-NN search"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# k-NN search

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/knn
> **target_lang:** meta — documentation tier. ALL sections preserved.



# k-Nearest Neighbor (k-NN) search in Amazon OpenSearch Service
<a name="knn"></a>

Short for its associated *k-nearest neighbors* algorithm, k-NN for Amazon OpenSearch Service lets you search for points in a vector space and find the "nearest neighbors" for those points by Euclidean distance or cosine similarity. Use cases include recommendations (for example, an "other songs you might like" feature in a music application), image recognition, and fraud detection.

**Note**  
This documentation provides a brief overview of the k-NN plugin, as well as limitations when using the plugin with managed OpenSearch Service. For comprehensive documentation of the k-NN plugin, including simple and complex examples, parameter references, and the complete API reference, see the open source [OpenSearch documentation](https://opensearch.org/docs/latest/search-plugins/knn/index/). The open source documentation also covers performance tuning and k-NN-specific cluster settings. 

## Getting started with k-NN
<a name="knn-gs"></a>

To use k-NN, you must create an index with the `index.knn` setting and add one or more fields of the `knn_vector` data type.

```
PUT my-index

{
  "settings": {
    "index.knn": true
  },
  "mappings": {
    "properties": {
      "{{my_vector1}}": {
        "type": "knn_vector",
        "dimension": 2
      },
      "{{my_vector2}}": {
        "type": "knn_vector",
        "dimension": 4
      }
    }
  }
}
```

The `knn_vector` data type supports a single list of up to 10,000 floats, with the number of floats defined by the required `dimension` parameter. After you create the index, add some data to it.

```
POST _bulk

{ "index": { "_index": "my-index", "_id": "1" } }
{ "my_vector1": [1.5, 2.5], "price": 12.2 }
{ "index": { "_index": "my-index", "_id": "2" } }
{ "my_vector1": [2.5, 3.5], "price": 7.1 }
{ "index": { "_index": "my-index", "_id": "3" } }
{ "my_vector1": [3.5, 4.5], "price": 12.9 }
{ "index": { "_index": "my-index", "_id": "4" } }
{ "my_vector1": [5.5, 6.5], "price": 1.2 }
{ "index": { "_index": "my-index", "_id": "5" } }
{ "my_vector1": [4.5, 5.5], "price": 3.7 }
{ "index": { "_index": "my-index", "_id": "6" } }
{ "my_vector2": [1.5, 5.5, 4.5, 6.4], "price": 10.3 }
{ "index": { "_index": "my-index", "_id": "7" } }
{ "my_vector2": [2.5, 3.5, 5.6, 6.7], "price": 5.5 }
{ "index": { "_index": "my-index", "_id": "8" } }
{ "my_vector2": [4.5, 5.5, 6.7, 3.7], "price": 4.4 }
{ "index": { "_index": "my-index", "_id": "9" } }
{ "my_vector2": [1.5, 5.5, 4.5, 6.4], "price": 8.9 }
```

Then you can search the data using the `knn` query type.

```
GET my-index/_search
{
  "size": 2,
  "query": {
    "knn": {
      "{{my_vector2}}": {
        "vector": [2, 3, 5, 6],
        "k": 2
      }
    }
  }
}
```

In this case, `k` is the number of neighbors you want the query to return, but you must also include the `size` option. Otherwise, you get `k` results for each shard (and each segment) rather than `k` results for the entire query. k-NN supports a maximum `k` value of 10,000.

If you mix the `knn` query with other clauses, you might receive fewer than `k` results. In this example, the `post_filter` clause reduces the number of results from 2 to 1.

```
GET my-index/_search

{
  "size": 2,
  "query": {
    "knn": {
      "{{my_vector2}}": {
        "vector": [2, 3, 5, 6],
        "k": 2
      }
    }
  },
  "post_filter": {
    "range": {
      "{{price}}": {
        "gte": 6,
        "lte": 10
      }
    }
  }
}
```

If you need to handle a large volume of queries while maintaining optimal performance, you can use the [https://opensearch.org/docs/latest/api-reference/multi-search/](https://opensearch.org/docs/latest/api-reference/multi-search/) API to construct a bulk search with JSON and send a single request to perform multiple searches:

```
GET _msearch

{ "index": "my-index"}
{ "query": { "knn": {"my_vector2":{"vector": [2, 3, 5, 6],"k":2 }} } }
{ "index": "my-index", "search_type": "dfs_query_then_fetch"}
{ "query": { "knn": {"my_vector1":{"vector": [2, 3],"k":2 }} } }
```

The following video demonstrates how to set up bulk vector searches for K-NN queries.

[![AWS Videos](http://img.youtube.com/vi/Umi67JCfCbU/0.jpg)](http://www.youtube.com/watch?v=Umi67JCfCbU)


## k-NN differences, tuning, and limitations
<a name="knn-settings"></a>

OpenSearch lets you modify all [k-NN settings](https://docs.opensearch.org/latest/vector-search/settings/) using the `_cluster/settings` API. On OpenSearch Service, you can change all settings except `knn.memory.circuit_breaker.enabled` and `knn.circuit_breaker.triggered`. k-NN statistics are included as [Amazon CloudWatch metrics](managedomains-cloudwatchmetrics.md).

In particular, check the `KNNGraphMemoryUsage` metric on each data node against the `knn.memory.circuit_breaker.limit` statistic and the available RAM for the instance type. OpenSearch Service uses half of an instance's RAM for the Java heap (up to a heap size of 32 GiB). By default, k-NN uses up to 50% of the remaining half, so an instance type with 32 GiB of RAM can accommodate 8 GiB of graphs (32 \* 0.5 \* 0.5). Performance can suffer if graph memory usage exceeds this value.

You can migrate a k-NN index created on version 2.x or later to [UltraWarm](ultrawarm.md) or [cold storage](cold-storage.md) on a domain with version 2.17 or later.

Clear cache api and warmup apis for k-NN indices are blocked for warm indices. When the first query is initiated for the index, it downloads the graph files from Amazon S3 and loads the graph to memory. Similarly, when TTL is expired for the graphs, the files are automatically evicted from memory.