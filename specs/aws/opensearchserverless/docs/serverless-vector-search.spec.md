---
id: "@specs/aws/opensearchserverless/docs/serverless-vector-search"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Working with vector search collections"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Working with vector search collections

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/serverless-vector-search
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Working with vector search collections
<a name="serverless-vector-search"></a>

With the *vector search* collection type in OpenSearch Serverless, you can perform scalable, high-performing similarity searches. You can build modern machine learning (ML) augmented search experiences and generative artificial intelligence (AI) applications without managing the underlying vector database infrastructure. 

Use cases for vector search collections include image searches, document searches, music retrieval, product recommendations, video searches, location-based searches, fraud detection, and anomaly detection. 

The vector engine for OpenSearch Serverless uses the [k-nearest neighbor (k-NN) search feature](https://opensearch.org/docs/latest/search-plugins/knn/index/) in OpenSearch. You get the same functionality with the simplicity of a serverless environment. The engine supports the [k-NN plugin API](https://opensearch.org/docs/latest/search-plugins/knn/api/). With these operations, you can use full-text search, advanced filtering, aggregations, geospatial queries, and nested queries for faster data retrieval and enhanced search results.

The vector engine provides distance metrics such as Euclidean distance, cosine similarity, and dot product similarity, and can accommodate 16,000 dimensions. You can store fields with various data types for metadata, such as numbers, Booleans, dates, keywords, and geopoints. You can also store fields with text for descriptive information to add more context to stored vectors. Colocating the data types reduces complexity, increases maintainability, and avoids data duplication, version compatibility challenges, and licensing issues. 

## NextGen vector search collections
<a name="serverless-vector-nextgen-features"></a>

NextGen vector search scales on demand based on workload to optimize the balance between cost and performance. Only the data blocks required to serve active search requests are loaded into memory, and workers scale dynamically based on required memory and CPU resources. When the collection is idle with no ongoing requests, both indexing and search scale to zero, providing additional cost savings. By default, NextGen includes built-in optimizations that improve recall while reducing cost and latency.
+ **Custom doc ID** – Custom document IDs are supported in NextGen collections, making it easier for customers to perform updates or index documents with user-provided IDs.
+ **32x compression indices** – All indexes are created with advanced 32x compression technique by default. You can override the default compression level and select any supported compression level: 1x, 2x, 8x, 16x, or 32x (default).
+ **Index build acceleration** – GPU acceleration is enabled by default to help build large scale vector indexes faster and more efficiently. It reduces the time needed to index data into vector indexes, providing a high throughput indexing experience and cost savings. GPU resources are provisioned only when needed during index build operations. You can control GPU usage on a per index basis using the setting `index.knn.remote_index_build.enabled`. For more information, see [GPU-acceleration for vector indexing](gpu-acceleration-vector-index.md).
+ **Simplified API** – NextGen vector search collections do not require the `engine` and `mode` parameters in index mappings. The system automatically determines the optimal configuration internally, reducing the complexity of index creation.
+ **Optimized search response** – By default, search responses in NextGen vector collections exclude the original vector from the results. This reduces end to end search latency and response payload size. To include vectors in the search response, see [Retrieve full document with vectors](#serverless-vector-index-full-source).
+ NextGen vector collections have a read-after-write latency (`refresh_interval`) of 10 seconds.

## Getting started with vector search collections
<a name="serverless-vector-tutorial"></a>

In this tutorial, you complete the following steps to store, search, and retrieve vector embeddings in real time:

1. [Configure permissions](#serverless-vector-permissions)

1. [Create a collection](#serverless-vector-create)

1. [Upload and search data](#serverless-vector-index)

1. [Delete the collection](#serverless-vector-delete)

### Step 1: Configure permissions
<a name="serverless-vector-permissions"></a>

To complete this tutorial (and to use OpenSearch Serverless in general), you must have the correct AWS Identity and Access Management (IAM) permissions. In this tutorial, you create a collection, upload and search data, and then delete the collection.

Your user or role must have an attached [identity-based policy](security-iam-serverless.md#security-iam-serverless-id-based-policies) with the following minimum permissions:

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Action": [
        "aoss:CreateCollection",
        "aoss:ListCollections",
        "aoss:BatchGetCollection",
        "aoss:DeleteCollection",
        "aoss:CreateAccessPolicy",
        "aoss:ListAccessPolicies",
        "aoss:UpdateAccessPolicy",
        "aoss:CreateSecurityPolicy",
        "iam:ListUsers",
        "iam:ListRoles"
      ],
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}
```

------

For more information about OpenSearch Serverless IAM permissions, see [Identity and Access Management for Amazon OpenSearch Serverless](security-iam-serverless.md).

### Step 2: Create a collection
<a name="serverless-vector-create"></a>

To create a new collection, follow the unified collection creation flow (NextGen Express Create), which automatically configures encryption, network, and data access policies. For instructions, see [Create a NextGen collection (Express Create)](serverless-create.md#serverless-create-nextgen-easy).

For the rest of this tutorial, the example collection is named `housing` and is a NextGen vector search collection.

**Note**  
If you choose to create a Classic vector collection instead, see [Working with Classic vector collections](#serverless-vector-classic) for procedures specific to Classic collections.

### Step 3: Upload and search data
<a name="serverless-vector-index"></a>

An *index* is a collection of documents with a common data schema that provides a way for you to store, search, and retrieve your vector embeddings and other fields. You can create and upload data to indexes in an OpenSearch Serverless collection by using the [Dev Tools](https://opensearch.org/docs/latest/dashboards/dev-tools/index-dev/) console in OpenSearch Dashboards, or an HTTP tool such as [Postman](https://www.postman.com/downloads/) or [awscurl](https://github.com/okigan/awscurl). This tutorial uses Dev Tools. For programmatic access using the Python SDK, see [Ingesting data into Amazon OpenSearch Serverless collections](serverless-clients.md).

**To index and search data in the housing collection**

1. To create an index for your new collection, send the following request in the [Dev Tools](https://opensearch.org/docs/latest/dashboards/dev-tools/index-dev/) console. By default, this creates an index with Euclidean distance and 32x compression.

   ```
   PUT housing-index
   {
     "settings": {
       "index.knn": true
     },
     "mappings": {
       "properties": {
         "housing-vector": {
           "type": "knn_vector",
           "dimension": 3,
           "space_type": "l2"
         },
         "title": {
           "type": "text"
         },
         "price": {
           "type": "long"
         },
         "location": {
           "type": "geo_point"
         }
       }
     }
   }
   ```

1. To use a different compression level, set `compression_level` in the field mapping. The following example creates an index with `compression_level` set to 1x.

   ```
   PUT housing-index-1x
   {
     "settings": {
       "index.knn": true
     },
     "mappings": {
       "properties": {
         "housing-vector": {
           "type": "knn_vector",
           "dimension": 3,
           "compression_level": "1x",
           "space_type": "l2"
         },
         "title": {
           "type": "text"
         },
         "price": {
           "type": "long"
         },
         "location": {
           "type": "geo_point"
         }
       }
     }
   }
   ```

   Supported compression levels are 1x, 2x, 8x, 16x, and 32x.

1. To index documents into `housing-index`, you can use a system-generated ID (POST) or a user-provided ID (PUT).

   ```
   # System-generated document ID
   POST housing-index/_doc
   {
     "housing-vector": [10, 20, 30],
     "title": "2 bedroom in downtown Seattle",
     "price": "2800",
     "location": "47.71, 122.00"
   }
   
   # User-provided document ID
   PUT housing-index/_doc/100
   {
     "housing-vector": [10, 20, 30],
     "title": "2 bedroom in downtown Seattle",
     "price": "2800",
     "location": "47.71, 122.00"
   }
   ```

1. To search for properties similar to the ones in your index, send the following query. By default, the search response excludes the original vector from `_source` to reduce latency and payload size.

   ```
   GET housing-index/_search
   {
     "size": 5,
     "query": {
       "knn": {
         "housing-vector": {
           "vector": [10, 20, 30],
           "k": 2
         }
       }
     }
   }
   ```

   The response excludes the `housing-vector` field from `_source`:

   ```
   {
     "took": 10,
     "timed_out": false,
     "_shards": {
       "total": 0,
       "successful": 0,
       "skipped": 0,
       "failed": 0
     },
     "hits": {
       "total": {
         "value": 1,
         "relation": "eq"
       },
       "max_score": 1,
       "hits": [
         {
           "_index": "housing-index",
           "_id": "100",
           "_score": 1,
           "_source": {
             "price": "2800",
             "location": "47.71, 122.00",
             "title": "2 bedroom in downtown Seattle"
           }
         }
       ]
     }
   }
   ```

#### Retrieve full document with vectors
<a name="serverless-vector-index-full-source"></a>

To override the default behavior, set `_source` to `true` in the search request. You can also use the `includes`/`excludes` options of `_source` to retrieve specific fields.

```
GET housing-index/_search
{
  "size": 5,
  "_source": true,
  "query": {
    "knn": {
      "housing-vector": {
        "vector": [10, 20, 30],
        "k": 2
      }
    }
  }
}
```

The response now includes the `housing-vector` field in `_source`:

```
{
  "took": 10,
  "timed_out": false,
  "_shards": {
    "total": 0,
    "successful": 0,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 1,
      "relation": "eq"
    },
    "max_score": 1,
    "hits": [
      {
        "_index": "housing-index",
        "_id": "100",
        "_score": 1,
        "_source": {
          "housing-vector": [10, 20, 30],
          "price": "2800",
          "location": "47.71, 122.00",
          "title": "2 bedroom in downtown Seattle"
        }
      }
    ]
  }
}
```

### Step 4: Delete the collection
<a name="serverless-vector-delete"></a>

Because the *housing* collection is for test purposes, delete it when you're done experimenting.

**To delete an OpenSearch Serverless collection**

1. Open the Amazon OpenSearch Service console.

1. In the left navigation pane, choose **Collections** and select the **housing** collection.

1. Choose **Delete** and confirm the deletion.

## Filtered search
<a name="serverless-vector-filter"></a>

You can use filters to refine your semantic search results. To create an index and perform a filtered search on your documents, substitute [Upload and search data](#serverless-vector-index) in the previous tutorial with the following instructions. The other steps remain the same. For more information about filters, see [k-NN search with filters](https://opensearch.org/docs/latest/search-plugins/knn/filter-search-knn/).

**To index and search data in the housing collection**

1. To create a single index for your collection, send the following request in the [Dev Tools](https://opensearch.org/docs/latest/dashboards/dev-tools/index-dev/) console:

   ```
   PUT housing-index-filtered
   {
     "settings": {
       "index.knn": true
     },
     "mappings": {
       "properties": {
         "housing-vector": {
           "type": "knn_vector",
           "dimension": 3,
           "space_type": "l2",
           "method": {
             "name": "hnsw"
           }
         },
         "title": {
           "type": "text"
         },
         "price": {
           "type": "long"
         },
         "location": {
           "type": "geo_point"
         }
       }
     }
   }
   ```

1. To index a single document into *housing-index-filtered*, send the following request:

   ```
   POST housing-index-filtered/_doc
   {
     "housing-vector": [
       10,
       20,
       30
     ],
     "title": "2 bedroom in downtown Seattle",
     "price": "2800",
     "location": "47.71, 122.00"
   }
   ```

1. To search your data for an apartment in Seattle under a given price and within a given distance of a geographical point, send the following request:

   ```
   GET housing-index-filtered/_search
   {
     "size": 5,
     "query": {
       "knn": {
         "housing-vector": {
           "vector": [
             0.1,
             0.2,
             0.3
           ],
           "k": 5,
           "filter": {
             "bool": {
               "must": [
                 {
                   "query_string": {
                     "query": "Find me 2 bedroom apartment in Seattle under $3000 ",
                     "fields": [
                       "title"
                     ]
                   }
                 },
                 {
                   "range": {
                     "price": {
                       "lte": 3000
                     }
                   }
                 },
                 {
                   "geo_distance": {
                     "distance": "100miles",
                     "location": {
                       "lat": 48,
                       "lon": 121
                     }
                   }
                 }
               ]
             }
           }
         }
       }
     }
   }
   ```

## Limitations
<a name="serverless-vector-limitations"></a>
+ Radial search isn't supported on NextGen vector indexes that use 32x compression.

## Working with Classic vector collections
<a name="serverless-vector-classic"></a>

Classic vector collections are the original generation of OpenSearch Serverless vector search. Use the procedures in this section if you have an existing Classic vector collection. For new collections, we recommend NextGen — see [Creating collections](serverless-create.md) to create a NextGen vector collection.

**Note**  
Amazon OpenSearch Serverless Classic collections support Faiss 16-bit scalar quantization, which performs conversions between 32-bit floating and 16-bit vectors. To learn more, see [ Faiss 16-bit scalar quantization](https://opensearch.org/docs/latest/search-plugins/knn/knn-vector-quantization/#faiss-16-bit-scalar-quantization). You can also use binary vectors to reduce memory costs. For more information, see [Binary vectors](https://opensearch.org/docs/latest/field-types/supported-field-types/knn-vector#binary-vectors).
Amazon OpenSearch Serverless Classic collections support disk-based vector search, which significantly reduces the operational costs for vector workloads in low-memory environments. For more information, see [Disk-based vector search](https://docs.opensearch.org/2.19/vector-search/optimizing-storage/disk-based-vector-search/).

### Upload and search data (Classic)
<a name="serverless-vector-classic-index"></a>

The following examples apply to Classic vector collections, which use the `nmslib` engine by default and include the original vector in search responses.

**To index and search data in a Classic housing collection**

1. To create an index for your Classic collection, send the following request in the [Dev Tools](https://opensearch.org/docs/latest/dashboards/dev-tools/index-dev/) console. By default, this creates an index with the `nmslib` engine and Euclidean distance.

   ```
   PUT housing-index
   {
      "settings": {
         "index.knn": true
      },
      "mappings": {
         "properties": {
            "housing-vector": {
               "type": "knn_vector",
               "dimension": 3
            },
            "title": {
               "type": "text"
            },
            "price": {
               "type": "long"
            },
            "location": {
               "type": "geo_point"
            }
         }
      }
   }
   ```

1. To index a single document into *housing-index*, send the following request:

   ```
   POST housing-index/_doc
   {
     "housing-vector": [
       10,
       20,
       30
     ],
     "title": "2 bedroom in downtown Seattle",
     "price": "2800",
     "location": "47.71, 122.00"
   }
   ```

1. To search for properties similar to the ones in your index, send the following query:

   ```
   GET housing-index/_search
   {
       "size": 5,
       "query": {
           "knn": {
               "housing-vector": {
                   "vector": [
                       10,
                       20,
                       30
                   ],
                   "k": 5
               }
           }
       }
   }
   ```

### Filtered search (Classic)
<a name="serverless-vector-classic-filter"></a>

To create an index and perform a filtered search, use the following examples. For more information about filters, see [k-NN search with filters](https://opensearch.org/docs/latest/search-plugins/knn/filter-search-knn/).

**To index and perform a filtered search on a Classic housing collection**

1. To create a single index for your collection, send the following request in the [Dev Tools](https://opensearch.org/docs/latest/dashboards/dev-tools/index-dev/) console:

   ```
   PUT housing-index-filtered
   {
     "settings": {
       "index.knn": true
     },
     "mappings": {
       "properties": {
         "housing-vector": {
           "type": "knn_vector",
           "dimension": 3,
           "method": {
             "engine": "faiss",
             "name": "hnsw"
           }
         },
         "title": {
           "type": "text"
         },
         "price": {
           "type": "long"
         },
         "location": {
           "type": "geo_point"
         }
       }
     }
   }
   ```

1. To index a single document into *housing-index-filtered*, send the following request:

   ```
   POST housing-index-filtered/_doc
   {
     "housing-vector": [
       10,
       20,
       30
     ],
     "title": "2 bedroom in downtown Seattle",
     "price": "2800",
     "location": "47.71, 122.00"
   }
   ```

1. To search your data for an apartment in Seattle under a given price and within a given distance of a geographical point, send the following request:

   ```
   GET housing-index-filtered/_search
   {
     "size": 5,
     "query": {
       "knn": {
         "housing-vector": {
           "vector": [
             0.1,
             0.2,
             0.3
           ],
           "k": 5,
           "filter": {
             "bool": {
               "must": [
                 {
                   "query_string": {
                     "query": "Find me 2 bedroom apartment in Seattle under $3000 ",
                     "fields": [
                       "title"
                     ]
                   }
                 },
                 {
                   "range": {
                     "price": {
                       "lte": 3000
                     }
                   }
                 },
                 {
                   "geo_distance": {
                     "distance": "100miles",
                     "location": {
                       "lat": 48,
                       "lon": 121
                     }
                   }
                 }
               ]
             }
           }
         }
       }
     }
   }
   ```

### Limitations (Classic)
<a name="serverless-vector-classic-limitations"></a>

Classic vector collections have the following limitations:
+ Vector search collections don't support the Apache Lucene ANN engine.
+ Vector search collections support only the HNSW algorithm with Faiss. They don't support IVF or IVFQ.
+ Vector search collections don't support the warmup, stats, and model training API operations.
+ Vector search collections don't support inline or stored scripts.
+ Index count information isn't available in the AWS Management Console for vector search collections. 
+ The refresh interval for indexes on vector search collections is 60 seconds.

### Billion-scale workloads
<a name="serverless-vector-billion"></a>

Classic vector search collections support workloads with billions of vectors. You don't need to reindex for scaling purposes because auto scaling does this for you. If you have millions of vectors (or more) with a high number of dimensions and need more than 200 OCUs, contact [AWS Support](https://aws.amazon.com/premiumsupport/) to raise the maximum OpenSearch Compute Units (OCUs) for your account. 

## Next steps
<a name="serverless-vector-next"></a>

Now that you know how to create a vector search collection and index data, you can try the following exercises:
+ Use the OpenSearch Python client to work with vector search collections. See this tutorial on [GitHub](https://github.com/opensearch-project/opensearch-py/blob/main/guides/plugins/knn.md). 
+ Use the OpenSearch Java client to work with vector search collections. See this tutorial on [GitHub](https://github.com/opensearch-project/opensearch-java/blob/main/guides/plugins/knn.md). 
+ Set up LangChain to use OpenSearch as a vector store. LangChain is an open source framework for developing applications powered by language models. For more information, see the [LangChain documentation](https://python.langchain.com/docs/integrations/vectorstores/opensearch).